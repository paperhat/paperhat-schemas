Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Instruction

A standalone directive addressed to the reader or user. Distinct from Step, which is a sequential action within a Procedure.

## When to Use

Use `Instruction` for standalone directives that exist outside a procedural sequence. An Instruction is a self-contained imperative statement: "Do not use near open flame," "Store in a cool, dry place," "Consult your physician before beginning any exercise program." This is different from Step, which is one action in an ordered sequence within a Procedure.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | no | A stable identifier for cross-referencing this instruction. |
| language | $EnumeratedToken | no | BCP 47 language tag identifying the language of the instruction text. |

## Content

Instruction requires text content (`RequiresContent whitespaceMode=$Flow`). The directive text is the element's content, not a trait.

## Design Notes

- Instruction is a discourse-level concept representing a standalone imperative statement. Step is a procedural-level concept representing one action in an ordered sequence.
- `$MustNotBeEntity` because instructions are embedded within their parent context.
- Pure leaf with no imports. The composing schema wires Instruction as a child concept where standalone directives are permitted.

---

**End of Instruction v1.0.0**
