# Behavior Expression Schema Split Plan

Charles F. Munat
16 April 2026

---

## 1. The Problem

The behavior-expression-schema is a single schema with ~390 ConceptDefinitions (780 lines counting open+close tags). Many concepts share natural names across different domains — `Element` appears in both core expression nodes and collection operations, `separator` appears in multiple text and collection operators, etc. The Codex processor enforces that `name` is unique within a Schema scope (§11.9.5.1). This validation fails with dozens of collisions.

This blocks the entire pipeline: the code-specification schema now imports behavior-expression-schema, and any code specification that uses the code-specification schema fails validation because the imported schema is invalid.

## 2. The Fix

Split the single behavior-expression-schema into multiple schemas, each with its own namespace. The existing GROUP sections already organize concepts by family. Each family becomes its own schema. Name collisions disappear because the same name in different schemas occupies different namespaces.

## 3. Current Consumers

Three schemas import the behavior-expression-schema:

1. `adaptive-plan/schema.cdx` — uses `behavior:Validation` and `behavior:Calculation`
2. `semantic-projection/schema.cdx` — uses `behavior:Validation`
3. `code-specification/schema.cdx` — uses `behavior:Validation`

All three use ONLY the two Expression Container concepts: `Validation` and `Calculation`. They do not directly reference any operator concepts (operators appear as children inside Validation/Calculation blocks in instance documents, not in schema child rules).

## 4. Proposed Schema Split

### 4.1 Core Schema (keeps the current namespace and hash)

**Package:** `behavior-expression-core`
**Namespace:** `behavior`
**Contains:**
- Expression Containers (Calculation, Validation) — 2 concepts
- Core Expression Nodes (Argument, Variable, Constant, FieldStep, Index, Source, Position, Absent) — 8 concepts
- Context and Input Nodes (Input, ThisNode, Field, Element, Parameter, Literal) — 6 concepts
- Generic Argument Wrappers (Referent, Comparator) — 2 concepts
- Semantic Argument Wrappers (all three groups) — 16 concepts

**Total:** ~34 concepts

This schema retains the `behavior` namespace so that all three current consumers (`behavior:Validation`, `behavior:Calculation`) continue to work with zero changes. The hash changes, but the namespace prefix is the same.

### 4.2 Operator Family Schemas

Each family gets its own schema. Each imports the core schema for access to argument wrapper concepts.

| Schema | Namespace | Groups Included | Estimated Concepts |
|---|---|---|---|
| `behavior-expression-math` | `behaviorMath` | Mathematical Constants, Complex Number Operations, Basic Arithmetic, Integer Arithmetic, Value Operations, Rounding, Powers/Roots/Exponentials | ~60 |
| `behavior-expression-trigonometry` | `behaviorTrig` | Trigonometry, Additional Trigonometry, Angle Conversion, Hyperbolic Functions, Angle Normalization | ~36 |
| `behavior-expression-relational` | `behaviorRel` | Comparison Operators, Logical Operators, Type Guards | ~17 |
| `behavior-expression-text` | `behaviorText` | All Text Operations groups | ~32 |
| `behavior-expression-temporal` | `behaviorTemporal` | All Temporal groups | ~34 |
| `behavior-expression-statistics` | `behaviorStats` | All Statistics groups | ~24 |
| `behavior-expression-combinatorics` | `behaviorCombi` | Combinatorics, Number Theory | ~11 |
| `behavior-expression-linear-algebra` | `behaviorLinalg` | All Linear Algebra groups | ~13 |
| `behavior-expression-classification` | `behaviorClass` | Classification, Interpolation | ~14 |
| `behavior-expression-collection` | `behaviorColl` | All Collection Operations, List, Set, Map, Record, Tuple, Collection Creation | ~72 |
| `behavior-expression-calculus` | `behaviorCalc` | Calculus - Numerical Methods | ~12 |
| `behavior-expression-special` | `behaviorSpecial` | Special Functions | ~17 |
| `behavior-expression-geometry` | `behaviorGeom` | All Geometry groups | ~31 |

**Total across all families:** ~390 concepts (matching the current schema)

### 4.3 Trait Definitions and Constraints

The current schema has trait definitions and constraint definitions (the groups with 0 concepts — "Text Traits", "Temporal Traits", etc.). These trait definitions belong in their corresponding family schema. Constraints go with the family they constrain.

### 4.4 Enumerated Value Sets

The current schema has 3 enumerated value sets (ArgumentPosition, RoundingMode, DisambiguationMode). These go in the core or the family that uses them:
- ArgumentPosition → core
- RoundingMode → math
- DisambiguationMode → temporal

## 5. Impact on Consumers

### Schema consumers (schemas that import behavior-expression-schema)

All three consumers use only `behavior:Validation` and `behavior:Calculation`. These stay in the core schema. The core schema keeps the `behavior` namespace. The consumers' `<SchemaImport namespace="behavior" reference=.../>` needs only a hash update. Zero concept selector changes.

### Instance document consumers (documents that use behavior expressions)

Instance documents (e.g., rdf-spec ValidationRules, typography-spec ValidationRules, behavior examples) use operator concepts like `behavior:IsGreaterThan`, `behavior:MatchesPattern`, `behavior:And`, `behavior:Input`, `behavior:Literal`.

After the split, these operators live in family schemas with different namespaces. BUT — in instance documents, the concepts are used as CHILDREN inside `behavior:Validation` blocks. Codex resolves child concept references based on the schema's import graph. The code-specification schema would need to import both the core schema AND the relevant family schemas.

This is the critical design question: does each consuming schema need to import every family it uses? Or does the core schema re-export the families?

**Option A: Each consumer imports the families it needs.**
The code-specification schema imports core + relational (for IsGreaterThan, MatchesPattern, And). The adaptive-plan schema imports core + whatever families its calculations use. Clean, explicit, minimal.

**Option B: A single "all" meta-schema re-exports everything.**
A `behavior-expression-all` schema imports all 14 schemas and re-exports them under the `behavior` namespace. Consumers import this one schema and get everything. Simpler for consumers, but defeats the purpose of splitting.

**Option C: The core schema imports and re-exports all families.**
Same as Option B but the core IS the meta-schema. Consumers see the same `behavior` namespace with the same concepts. The split is internal — for organization and uniqueness resolution only.

**Recommendation: Option C.** The core schema imports all family schemas. The split is for internal organization and name uniqueness. Consumers continue to import one schema (`behavior` namespace) and reference concepts with the `behavior:` prefix. Zero changes to instance documents. Zero changes to consumer schemas beyond the hash update.

The family schemas are independently valid (no internal name collisions). The core schema re-imports them all. The Codex processor validates each family schema independently (no name collisions within any single schema). Then the core schema's imports bring them all together under one namespace for consumers.

IMPORTANT: Verify that Codex supports this re-export pattern. If re-import does not make child concepts available under the importing schema's namespace, this approach does not work. In that case, fall back to Option A (explicit per-family imports).

## 6. Batch Structure

### Batch 0: Verify the Re-Export Pattern
- Write a minimal test: two tiny schemas (schema-a with concept Foo, schema-b with concept Bar). A third schema-c imports both. Verify that a document conforming to schema-c can use both Foo and Bar as children.
- If this works, proceed with Option C.
- If not, fall back to Option A and adjust the plan.

**Definition of done:** The re-export pattern is verified or rejected. The approach for all subsequent batches is locked.

### Batch 1: Extract Core Schema
- Create `behavior/behavior-expression-core/` with schema.cdx, manifest.cdx, README.md
- Move Expression Containers, Core Expression Nodes, Context and Input Nodes, Generic Argument Wrappers, Semantic Argument Wrappers, and the ArgumentPosition enumerated value set into the core schema
- Verify the core schema validates (zero name collisions in these ~34 concepts)
- Do NOT delete concepts from the original schema yet — both exist temporarily

**Definition of done:** Core schema validates. All 34 concepts have unique names within it.

### Batch 2: Extract Relational and Logic Family
- Create `behavior/behavior-expression-relational/` with Comparison Operators, Logical Operators, Type Guards
- This family is needed by the code-specification schema's ValidationRules (IsGreaterThan, MatchesPattern, And, etc.)
- Import the core schema (for Referent, Comparator, Input, Literal)
- Verify schema validates

**Definition of done:** Relational schema validates. All ~17 concepts have unique names.

### Batch 3: Extract Text Family
- Create `behavior/behavior-expression-text/` with all Text Operations groups
- Import core schema
- Verify validates

**Definition of done:** Text schema validates.

### Batch 4: Extract Math Family
- Create `behavior/behavior-expression-math/` with Mathematical Constants, Complex Number, Basic Arithmetic, Integer Arithmetic, Value Operations, Rounding, Powers/Roots/Exponentials
- Include RoundingMode enumerated value set
- Import core schema
- Verify validates

**Definition of done:** Math schema validates.

### Batch 5: Extract Temporal Family
- Create `behavior/behavior-expression-temporal/` with all Temporal groups
- Include DisambiguationMode enumerated value set
- Import core schema
- Verify validates

**Definition of done:** Temporal schema validates.

### Batch 6: Extract Collection Family
- Create `behavior/behavior-expression-collection/` with all Collection, List, Set, Map, Record, Tuple, Collection Creation groups
- Import core schema
- Verify validates — this family had the `Element` collision, which is now resolved

**Definition of done:** Collection schema validates. `Element` is unique within this schema.

### Batch 7: Extract Remaining Families
- Statistics, Combinatorics, Linear Algebra, Classification/Interpolation, Calculus, Special Functions, Geometry, Trigonometry
- Each gets its own schema directory
- Import core schema
- Verify each validates

**Definition of done:** All 13 family schemas validate independently.

### Batch 8: Rebuild the Core as Re-Exporter (Option C)
- Update the core schema to import all 13 family schemas
- If re-export works: the core schema exposes everything under the `behavior` namespace
- Update the manifest with the new closure hash
- Verify that the adaptive-plan, semantic-projection, and code-specification schemas validate when importing the rebuilt core

**Definition of done:** All three consumer schemas validate. The `behavior:Validation` and `behavior:Calculation` references still work.

### Batch 9: Update Instance Documents
- Update the code-specification schema's import hash
- Update the adaptive-plan schema's import hash
- Update the semantic-projection schema's import hash
- Verify that rdf-spec and typography-spec code specifications validate (they use behavior:IsGreaterThan etc. inside ValidationRule children)
- Verify that the Codex processor generates instance graphs from code specifications

**Definition of done:** The full pipeline works. `codex rdf` produces instance graphs from code specifications that contain behavior expression ValidationRules.

### Batch 10: Delete the Old Schema
- Remove the original monolithic `behavior-expression-schema/schema.cdx`
- Replace it with the core schema (or redirect to it)
- Update all manifests
- Final verification of the entire pipeline

**Definition of done:** The monolithic schema is gone. All consumers use the split schemas. The pipeline produces instance graphs. Both code foundries generate code from the instance graphs.

## 7. Progress Checklist

```
[ ] Batch 0: Verify re-export pattern
[ ] Batch 1: Extract core schema
[ ] Batch 2: Extract relational and logic family
[ ] Batch 3: Extract text family
[ ] Batch 4: Extract math family
[ ] Batch 5: Extract temporal family
[ ] Batch 6: Extract collection family
[ ] Batch 7: Extract remaining families (7 schemas)
[ ] Batch 8: Rebuild core as re-exporter
[ ] Batch 9: Update instance documents and verify pipeline
[ ] Batch 10: Delete old schema, final verification
```

## 8. Risk

The main risk is Batch 0: does Codex support the re-export pattern? If a schema imports another schema, do the imported schema's concepts become available in documents conforming to the importing schema? If not, Option C does not work and every consumer needs explicit per-family imports. This is testable before any real work begins.

## 9. Rules

- Zero possibility language
- No abbreviations
- American English
- Every family schema is independently valid (zero name collisions within any single schema)
- The split does not change the behavior of any existing instance document
- The split does not require changes to the Codex processor
- The pipeline must work end-to-end after the split: code specification → Codex processor → instance graph → code foundry → generated code
