# Paperhat Internal Schema Roadmap

This is an implementation-order roadmap for Lexis coverage of Paperhat itself. It is organized to maximize immediate utility, architectural proof, and reuse. The rule throughout is: **model the real thing first; pages, PDFs, websites, and other outputs are projections.**

## Governing Principles

### Deduplication Rule

Concepts that appear in multiple stages are defined once as leaf packages and imported everywhere else. No concept is duplicated across packages. If two stages need the same concept, that concept lives in one leaf package with one schema definition and is imported via SchemaImport by every composer that uses it.

### Package Completeness Definition

A complete schema package has all of the following artifacts:

1. `manifest.cdx` — DomainPackageManifest with correct metadata, dependencies, and hashes
2. `schema.cdx` — Full ConceptDefinitions, TraitDefinitions, ConstraintDefinitions
3. `README.md` — Status/Lock State/Version header, concept table, trait table, constraints, design notes
4. `localizations/en.cdx` — English baseline with ConceptLocalization and TraitLocalization for every concept and trait
5. `examples/<name>/example.cdx` — At least one realistic example
6. `templates/<name>/template.cdx` — At least one authoring template

Vocabulary packages are reference token sets, not authoring schemas. They require manifest.cdx, vocabulary.cdx, README.md, and localizations/en.cdx. They do not require examples/ or templates/ — tokens are referenced from within other schemas, not authored as standalone instances.

### Hash Policy

Every manifest.cdx must contain a SHA-256 content hash and a Merkle-closure hash. These are computed via the `codex identity` CLI command. During initial authoring, hashes are marked `PENDING-HASH` and batch-computed once the CLI builds.

---

## Stage 1. Foundational Cross-Domain Vocabulary

This begins immediately and continues alongside all domain-schema work. These are the shared primitives that prevent duplication and drift across later schema families.

### Purpose

Provide the common semantic substrate used by specifications, white papers, policies, products, contracts, and organizational records.

### Existing Schemas (all LOCKED unless noted)

| Schema | Lock State | Status |
|---|---|---|
| person | LOCKED | Complete — 6 artifacts |
| person-name | LOCKED | Complete — 6 artifacts |
| organization | LOCKED | Complete — 6 artifacts |
| contact-point | LOCKED | Complete — 6 artifacts |
| identifier | LOCKED | Complete — 6 artifacts |
| location | LOCKED | Complete — 6 artifacts |
| geographic-location | LOCKED | Complete — 6 artifacts |
| work | LOCKED | Complete — 6 artifacts |
| description | LOCKED | Complete — 6 artifacts |
| summary | LOCKED | Complete — 6 artifacts |
| tags | LOCKED | Complete — 6 artifacts |
| audience | LOCKED | Complete — 6 artifacts |
| rating | LOCKED | Complete — 6 artifacts |
| offer | LOCKED | Complete — 6 artifacts |
| media-reference | LOCKED | Complete — 6 artifacts |
| reference | LOCKED | Complete — 6 artifacts |
| accessibility | LOCKED | Complete — 6 artifacts |
| operating-schedule | LOCKED | Complete — 6 artifacts |
| temporal | LOCKED | Complete — 6 artifacts |
| duration | LOCKED | Complete — 6 artifacts |
| monetary-amount | LOCKED | Complete — 6 artifacts |
| text | LOCKED | Complete — 6 artifacts |
| list | LOCKED | Complete — 6 artifacts |
| section | LOCKED | Complete — 6 artifacts |
| notes | LOCKED | Complete — 6 artifacts |
| rubric | LOCKED | Complete — 6 artifacts |
| relation | UNLOCKED | Complete — 6 artifacts |
| series | LOCKED | Complete — 6 artifacts |
| admonition | LOCKED | Complete — 6 artifacts |
| code | LOCKED | Complete — 6 artifacts |
| editorial-markup | LOCKED | Complete — 6 artifacts |
| foreign-term | LOCKED | Complete — 6 artifacts |
| linguistic-annotation | LOCKED | Complete — 6 artifacts |
| tone | LOCKED | Complete — 6 artifacts |
| figure | LOCKED | Complete — 6 artifacts |
| example | LOCKED | Complete — 6 artifacts |
| narrative | LOCKED | Complete — 6 artifacts |
| measure | LOCKED | Complete — 6 artifacts |
| event | LOCKED | Complete — 6 artifacts |
| project | LOCKED | Complete — 6 artifacts |
| role | LOCKED | Complete — 6 artifacts |
| jurisdiction | LOCKED | Complete — 6 artifacts |
| citation | LOCKED | Complete — 6 artifacts |
| term-entry | LOCKED | Complete — 6 artifacts |
| document-metadata | LOCKED | Complete — 6 artifacts |
| energy-measure | LOCKED | Complete — 6 artifacts |
| mass-measure | LOCKED | Complete — 6 artifacts |
| time-measure | LOCKED | Complete — 6 artifacts |
| volume-measure | LOCKED | Complete — 6 artifacts |
| material | UNLOCKED | Complete — 6 artifacts |
| organizational-unit | UNLOCKED | Complete — 6 artifacts |
| repository | UNLOCKED | Complete — 6 artifacts |
| media-asset | UNLOCKED | Complete — 6 artifacts |

### Proposed Concepts — Triage Results

| Proposed Concept | Decision | Rationale |
|---|---|---|
| Project | CREATED | `project` package exists (6/6). |
| Role | CREATED | `role` package exists (6/6). |
| Jurisdiction | CREATED | `jurisdiction` package exists (6/6). |
| Definition | CREATED | `term-entry` package exists (6/6). Provides term + definition pair. |
| Reference / Citation | CREATED | `citation` package exists (6/6). Reference also exists. |
| OrganizationalUnit | CREATED | `organizational-unit` package exists (6/6). |
| Repository | CREATED | `repository` package exists (6/6). |
| MediaAsset | CREATED | `media-asset` package exists (6/6). |
| Responsibility | REJECTED | Descriptive, not structural. Responsibilities are expressed through Description children on Role instances. |
| Authority | REJECTED | A property of a role assignment, not a standalone entity. If Stage 5 needs permission/prohibition modeling, that belongs in policy concepts. |
| Party | REJECTED | Union type that adds indirection without semantic value. Import Person and Organization separately where needed. |
| EffectivePeriod | REJECTED | Temporal already handles date ranges. A separate concept for start/end date pairs would duplicate existing capability. |
| Status | REJECTED | Status is a trait pattern, not an entity. Work has a `status` trait. Schemas define their own status trait with domain-appropriate tokens. |
| Document | REJECTED | DocumentMetadata already serves as the shared metadata container. An abstract Document base adds no compositional value. |
| StructuralUnit | REJECTED | Section covers hierarchical document structure. An abstraction over Section/Paragraph/ListItem carries no meaning of its own. |
| Name / Label | REJECTED | Non-person names are simple text traits. PersonName's complexity exists because person names have genuine internal structure. |

### Triage Checklist

- [x] Project — created as `project`
- [x] Role — created as `role`
- [x] Jurisdiction — created as `jurisdiction`
- [x] Definition — created as `term-entry`
- [x] Reference / Citation — created as `citation`
- [x] OrganizationalUnit — created as `organizational-unit`
- [x] Repository — created as `repository`
- [x] MediaAsset — created as `media-asset`
- [x] ~~Responsibility~~ — rejected
- [x] ~~Authority~~ — rejected
- [x] ~~Party~~ — rejected
- [x] ~~EffectivePeriod~~ — rejected
- [x] ~~Status~~ — rejected
- [x] ~~Document~~ — rejected
- [x] ~~StructuralUnit~~ — rejected
- [x] ~~Name / Label~~ — rejected

### Existing Vocabularies (all complete)

bcp-47-languages, e164-calling-codes, iana-time-zones, iso-3166-countries, iso-4217-currencies, food-categories, preparations, units-angle, units-area, units-data, units-electrical, units-energy, units-force, units-frequency, units-length, units-mass, units-pressure, units-speed, units-temperature, units-time, units-volume.

All 21 vocabulary packages have manifest.cdx, vocabulary.cdx, README.md, and localizations/en.cdx. Per the Package Completeness Definition, vocabulary packages do not require examples/ or templates/.

### Vocabulary Needs

New vocabularies will be identified during triage, potentially including: role-types, organization-kinds, jurisdiction-codes, document-status-values.

### Gate

A reusable shared vocabulary sufficient to stop inventing separate versions of person, role, organization, effective date, reference, and similar concepts inside each schema family.

### First Paperhat Examples

* Paperhat Limited
* Paperhat Institute
* Charles F. Munat
* Codex, Gloss, Lexis, Nexus, Praxis as projects/products
* GitHub repositories
* author/editor/maintainer roles
* domain names and publication identifiers

---

## Stage 2. Specification Schema Family

This is the first major domain schema and is core infrastructure, not merely content.

### Purpose

Represent normative and explanatory technical specifications as governed semantic artifacts.

### Existing Schemas

| Schema | Lock State | Status |
|---|---|---|
| specification | UNLOCKED | Complete — 6 artifacts. Has: Specification, Section, Paragraph, OrderedList, UnorderedList, ListItem, CodeBlock, Requirement, Definition, Note, SectionReference, ExternalReference. Uncommitted changes in working tree. |
| specification-foundation | UNLOCKED | Complete — 6 artifacts. Shared traits and enumerations for specification schemas. Uncommitted changes in working tree. |
| specification-rfc2119 | UNLOCKED | Complete — 6 artifacts. Full RFC 2119 variant with all modality keywords. Uncommitted changes in working tree. |

### Proposed Concepts — Gap Analysis

| Proposed Concept | Existing Coverage | Gap Status |
|---|---|---|
| Specification | Exists in `specification` | Covered |
| NormativeStatement | Requirement concept with modality trait | Covered |
| DefinitionEntry | Definition concept with `term` trait | Covered |
| RequirementSet | Uncommitted changes add this concept | In progress |
| Example | `example` schema exists (separate package, LOCKED) | Covered via import |
| Appendix / Annex | Section with `division=$Appendix` trait | Covered |
| Reference / BibliographyEntry | ExternalReference + Reference leaf + Citation leaf | NEEDS DECISION — is BibliographyEntry still needed? |
| ConformanceRequirement | Requirement with specific modality | NEEDS DECISION — separate concept or just a Requirement? |
| FormalNote / InformativeNote | Note concept exists | Covered |
| TermBinding | Uncommitted changes add this concept | In progress |
| Issue / OpenQuestion | Uncommitted changes add these concepts | In progress |

### Stage 2 Checklist

- [x] specification — exists, UNLOCKED, 6/6
- [x] specification-foundation — exists, UNLOCKED, 6/6
- [x] specification-rfc2119 — exists, UNLOCKED, 6/6
- [ ] RequirementSet — in progress (uncommitted)
- [ ] TermBinding — in progress (uncommitted)
- [ ] Issue / OpenQuestion — in progress (uncommitted)
- [ ] Reference / BibliographyEntry — needs decision
- [ ] ConformanceRequirement — needs decision
- [ ] Gate: author, validate, and project a real Paperhat specification end-to-end

### Dependencies

* Stage 1 foundational vocabulary
* Any new Stage 1 leaves identified during triage

### First Paperhat Examples

* Codex specification
* Gloss specification
* Canon specification
* Lexis architecture/specification
* Praxis capability model specification

---

## Stage 3. White Paper / Article / Publication Schema Family

This follows immediately after, or partly in parallel with, the specification family.

### Purpose

Represent long-form persuasive, explanatory, and analytical publications.

### Existing Schemas

| Schema | Lock State | Status |
|---|---|---|
| white-paper | LOCKED | Complete — 6 artifacts. Has: WhitePaper, Abstract, Conclusion. Imports: document-metadata, narrative, notes, series. |
| essay | LOCKED | Complete — 6 artifacts. Has: Essay. Imports: document-metadata, narrative, notes. |
| narrative | LOCKED | Complete — 6 artifacts. Composes Section and Text. |
| document-metadata | LOCKED | Complete — 6 artifacts. Composes Work, Description, Summary, Tags, Audience, Person, etc. |
| notes | LOCKED | Complete — 6 artifacts. Footnote/endnote support via keyed Notes/Note. |
| figure | LOCKED | Complete — 6 artifacts. Figure with caption. |
| series | LOCKED | Complete — 6 artifacts. SeriesInfo for series membership. |
| citation | LOCKED | Complete — 6 artifacts. Bibliographic citation support. |

### Proposed Concepts — Gap Analysis

| Proposed Concept | Existing Coverage | Gap Status |
|---|---|---|
| WhitePaper | Exists, LOCKED | Covered |
| Article / Essay | Essay exists, LOCKED | Covered |
| Abstract | Exists in WhitePaper | Covered |
| Claim / SupportingArgument / Evidence | Not present. WhitePaper design notes explicitly state these are rhetorical patterns within prose, not structural units. | Likely intentionally excluded |
| Citation / BibliographyEntry | Citation exists. Reference exists. Notes handles footnotes. | Covered |
| Figure | Exists, LOCKED | Covered |
| Table | Relation exists (UNLOCKED) for tabular data | NEEDS DECISION |
| Footnote / Endnote | Notes/Note exists, LOCKED | Covered |
| Series | Exists, LOCKED | Covered |
| PublicationEvent | Not present | NEEDS DECISION |
| Contributor | Person exists. Work has `author` trait. | NEEDS DECISION |

### Stage 3 Checklist

- [x] white-paper — LOCKED, 6/6
- [x] essay — LOCKED, 6/6
- [x] narrative — LOCKED, 6/6
- [x] document-metadata — LOCKED, 6/6
- [x] notes — LOCKED, 6/6
- [x] figure — LOCKED, 6/6
- [x] series — LOCKED, 6/6
- [x] citation — LOCKED, 6/6
- [ ] Table — needs decision (Relation exists but is it sufficient?)
- [ ] PublicationEvent — needs decision
- [ ] Contributor — needs decision
- [ ] Gate: represent existing Paperhat white papers semantically and project to web/PDF

### Dependencies

* Stage 1 foundational vocabulary
* WhitePaper and Essay are LOCKED — new concepts must be new packages, not modifications

### First Paperhat Examples

* Lexis track white papers
* Praxis track white papers
* Nexus/Canon position papers
* architecture rationale papers
* public essays/explainers

---

## Stage 4. Organization / Governance Structure Schema Family

This is early because many other schema families need institutional context.

### Purpose

Represent Paperhat as an institution: entities, projects, roles, ownership, authority, and relationships.

### Existing Schemas

| Schema | Lock State | Status |
|---|---|---|
| organization | LOCKED | Complete — 6 artifacts. Has: Organization with name, organizationKind, foundingDate, dissolutionDate traits. Children: Description, ContactPoint, Identifier, Location, Tags. |
| person | LOCKED | Complete — 6 artifacts. |
| project | LOCKED | Complete — 6 artifacts. |
| role | LOCKED | Complete — 6 artifacts. |
| organizational-unit | UNLOCKED | Complete — 6 artifacts. Leaf from Stage 1 triage. |
| repository | UNLOCKED | Complete — 6 artifacts. Leaf from Stage 1 triage. |

### Missing Schemas

These do not exist and were proposed in the original roadmap:

* Brand
* ProductLine
* AuthorityAssignment
* Membership / Assignment
* Relationship (cross-entity)
* Domain / Property / Asset

### Stage 4 Checklist

- [x] organization — complete, 6/6
- [x] person — complete, 6/6
- [x] project — complete, 6/6
- [x] role — complete, 6/6
- [x] OrganizationalUnit — created as `organizational-unit` (Stage 1 leaf)
- [x] Repository — created as `repository` (Stage 1 leaf)
- [ ] Brand — needs decision
- [ ] ProductLine — needs decision
- [ ] AuthorityAssignment — needs decision
- [ ] Membership / Assignment — needs decision
- [ ] Relationship (cross-entity) — needs decision
- [ ] Domain / Property / Asset — needs decision
- [ ] Gate: represent Paperhat's organizational and project structure canonically

### Dependencies

* Stage 1 foundational vocabulary (Role, Project, Jurisdiction, OrganizationalUnit, Repository all exist)

### First Paperhat Examples

* Paperhat Limited
* Paperhat Institute
* Lexis / Nexus / Praxis / Codex / Gloss / Canon
* websites and domains
* maintainer/author/editor roles
* product ownership / authority relationships

---

## Stage 5. Policy / Governance / Rule Schema Family

This is one of the most strategically important families and starts early.

### Purpose

Represent institutional rules and operational commitments as first-class semantic objects.

### Existing Schemas

| Schema | Lock State | Status |
|---|---|---|
| jurisdiction | LOCKED | Complete — 6 artifacts. Jurisdictional authority and scope. |

### Proposed Concepts

* PolicyDocument
* Policy
* Rule
* Obligation
* Permission
* Prohibition
* Condition
* Exception
* Scope
* ResponsibleParty
* Enforcement / Consequence
* ReviewRequirement
* ApprovalRequirement

### Stage 5 Checklist

- [x] jurisdiction — LOCKED, 6/6
- [ ] PolicyDocument — needs creation
- [ ] Policy — needs creation
- [ ] Rule — needs creation
- [ ] Obligation — needs creation
- [ ] Permission — needs creation
- [ ] Prohibition — needs creation
- [ ] Condition — needs creation
- [ ] Exception — needs creation
- [ ] Scope — needs creation
- [ ] ResponsibleParty — needs creation
- [ ] Enforcement / Consequence — needs creation
- [ ] ReviewRequirement — needs creation
- [ ] ApprovalRequirement — needs creation
- [ ] Gate: model Paperhat's own policies as semantic entities

### Dependencies

* Stage 1 foundational vocabulary
* Stage 4 organization/authority model

### First Paperhat Examples

* Terms of Use
* Privacy Policy
* Cookie Policy
* contributor rules
* licensing policy
* certification policy
* internal governance policies

---

## Stage 6. Product / Service / Offering Schema Family

### Purpose

Represent what Paperhat offers in a way that is reusable across web, documentation, contracts, pricing, and support materials.

### Existing Schemas

| Schema | Lock State | Status |
|---|---|---|
| product | LOCKED | Complete — 6 artifacts. General-purpose product schema. Has: name, brand, category, color, material, model, releaseDate. Children: Description, Offer, Identifier, Rating, Measure, MonetaryAmount, Tags, Work, Audience, Accessibility, NutritionInformation. |
| offer | LOCKED | Complete — 6 artifacts. Pricing and availability. |

### Proposed Additional Concepts

* Service (distinct from Product)
* Offering (abstract product-or-service)
* Tier / Plan
* Feature
* Capability
* Eligibility
* Dependency / Prerequisite
* Deliverable
* SupportEntitlement
* PriceModel
* SubscriptionTerm

### Stage 6 Checklist

- [x] product — LOCKED, 6/6
- [x] offer — LOCKED, 6/6
- [ ] Service — needs creation
- [ ] Offering — needs creation
- [ ] Tier / Plan — needs creation
- [ ] Feature — needs creation
- [ ] Capability — needs creation
- [ ] Eligibility — needs creation
- [ ] Dependency / Prerequisite — needs creation
- [ ] Deliverable — needs creation
- [ ] SupportEntitlement — needs creation
- [ ] PriceModel — needs creation
- [ ] SubscriptionTerm — needs creation
- [ ] Gate: describe Paperhat offerings consistently across sales pages, docs, proposals, agreements

### Dependencies

* Stage 1 foundational vocabulary
* Stage 4 organization/project model

### First Paperhat Examples

* Lexis FOSS / Pro / Premium
* Nexus FOSS / Pro / Premium
* support packages
* consulting offerings
* training offerings
* certification offerings

---

## Stage 7. Documentation / Guide / Procedure Schema Family

Operational knowledge rather than normative specification or public white paper.

### Purpose

Represent practical documentation, procedures, setup guides, and troubleshooting materials.

### Existing Schemas

None specific to documentation/guides. Will import from Stage 1 leaves, narrative, section, text, list, and other structural schemas.

### Proposed Concepts

* Guide
* Procedure
* Task
* Step
* Prerequisite
* Outcome
* TroubleshootingItem
* KnownIssue
* ReferenceEntry
* Environment / Platform
* ChecklistItem

### Stage 7 Checklist

- [ ] Guide — needs creation
- [ ] Procedure — needs creation
- [ ] Task — needs creation
- [ ] Step — needs creation
- [ ] Prerequisite — needs creation
- [ ] Outcome — needs creation
- [ ] TroubleshootingItem — needs creation
- [ ] KnownIssue — needs creation
- [ ] ReferenceEntry — needs creation
- [ ] Environment / Platform — needs creation
- [ ] ChecklistItem — needs creation
- [ ] Gate: maintain real user and internal operational documentation in Lexis

### Dependencies

* Stage 1 foundational vocabulary
* Stage 6 product/offering model
* Structural schemas (section, text, list, narrative)

### First Paperhat Examples

* install guides
* build instructions
* authoring guides
* projection/render workflow documentation
* release procedures
* support knowledge base articles

---

## Stage 8. Contract / Agreement Schema Family

This builds directly on policy/governance.

### Purpose

Represent binding agreements and commercial/legal commitments semantically.

### Existing Schemas

None.

### Proposed Concepts

* Contract
* Agreement
* Party (rejected as Stage 1 leaf — import Person and Organization directly)
* Clause
* Definition (legal definitions within a contract)
* Obligation
* Right
* Condition
* Exception
* Deliverable
* PaymentTerm
* ServiceLevel
* Term
* Renewal
* Termination
* Jurisdiction (from Stage 1 — exists)
* ApprovalState
* ClauseLibraryEntry
* Variant

### Stage 8 Checklist

- [ ] Contract — needs creation
- [ ] Agreement — needs creation
- [x] ~~Party~~ — rejected (import Person and Organization directly)
- [ ] Clause — needs creation
- [ ] Definition (legal) — needs creation
- [ ] Obligation — needs creation
- [ ] Right — needs creation
- [ ] Condition — needs creation
- [ ] Exception — needs creation
- [ ] Deliverable — needs creation
- [ ] PaymentTerm — needs creation
- [ ] ServiceLevel — needs creation
- [ ] Term — needs creation
- [ ] Renewal — needs creation
- [ ] Termination — needs creation
- [ ] ApprovalState — needs creation
- [ ] ClauseLibraryEntry — needs creation
- [ ] Variant — needs creation
- [ ] Gate: author and manage basic internal agreements through Lexis

### Dependencies

* Stage 5 policy/governance schema family
* Stage 4 organization/party/role models
* Stage 6 product/service/offering schema family

### First Paperhat Examples

* software license terms
* support agreements
* consulting agreements
* training agreements
* partnership/MOU templates
* certification terms

---

## Stage 9. Publishing / Media Asset Schema Family

### Purpose

Represent books, series, releases, downloadable assets, and publication metadata coherently.

### Existing Schemas

| Schema | Lock State | Status |
|---|---|---|
| series | LOCKED | Complete — 6 artifacts. SeriesInfo (title, position, track). |
| media-reference | LOCKED | Complete — 6 artifacts. Reference to a media resource by URI. |
| media-asset | UNLOCKED | Complete — 6 artifacts. The asset itself with identity. Leaf from Stage 1 triage. |

### Proposed Additional Concepts

* Publication
* Book
* Edition
* Release
* Contributor
* FormatVariant
* RightsStatement
* MediaAsset (exists as Stage 1 leaf — may need additional composition here)
* CoverAsset
* PublicationEvent

### Stage 9 Checklist

- [x] series — LOCKED, 6/6
- [x] media-reference — LOCKED, 6/6
- [ ] Publication — needs creation
- [ ] Book — needs creation
- [ ] Edition — needs creation
- [ ] Release — needs creation
- [ ] Contributor — needs creation
- [ ] FormatVariant — needs creation
- [ ] RightsStatement — needs creation
- [x] MediaAsset — created as `media-asset` (Stage 1 leaf)
- [ ] CoverAsset — needs creation
- [ ] PublicationEvent — needs creation
- [ ] Gate: represent books and publication assets as first-class semantic entities

### Dependencies

* Stage 3 white paper/article/publication model
* Stage 1 foundational vocabulary

### First Paperhat Examples

* book projects
* white paper series
* downloadable PDFs/EPUBs
* press kits
* cover and illustration assets
* publication releases

---

## Stage 10. Training / Learning Description Linkage

Praxis may own the deeper learning engine, but Lexis still holds semantically useful descriptive and publishing layers.

### Purpose

Represent training offerings, learning materials, and public learning descriptions in a way that interoperates with Praxis later.

### Existing Schemas

None.

### Proposed Concepts

* LearningOffering
* Module
* LearningObjective
* Prerequisite
* Artifact
* Assessment
* CompetencyReference / CapabilityReference
* Duration / EffortEstimate (Duration schema exists for time durations)
* CertificationPreparation

### Stage 10 Checklist

- [ ] LearningOffering — needs creation
- [ ] Module — needs creation
- [ ] LearningObjective — needs creation
- [ ] Prerequisite — needs creation
- [ ] Artifact — needs creation
- [ ] Assessment — needs creation
- [ ] CompetencyReference / CapabilityReference — needs creation
- [ ] Duration / EffortEstimate — needs decision (Duration exists)
- [ ] CertificationPreparation — needs creation
- [ ] Gate: describe training and learning offerings in Lexis

### Dependencies

* Stage 6 product/offering model
* Stage 3 publication model

### First Paperhat Examples

* Lexis training outline
* Nexus introductory training
* Codex authoring workshop description
* certification preparation materials
* learning pathway descriptions

---

# Recommended Dependency Order

1. **Foundational vocabulary** (Stage 1)
2. **Specification** (Stage 2)
3. **White Paper / Article / Publication** (Stage 3)
4. **Organization / Governance structure** (Stage 4)
5. **Policy / Governance / Rules** (Stage 5)
6. **Product / Service / Offering** (Stage 6)
7. **Documentation / Guide / Procedure** (Stage 7)
8. **Contract / Agreement** (Stage 8)
9. **Publishing / Book / Media asset** (Stage 9)
10. **Training / Learning linkage** (Stage 10)

---

# Priority Bands

## Band A — must exist early

* foundational vocabulary (Stage 1)
* specification (Stage 2)
* white paper / publication (Stage 3)
* organization (Stage 4)
* policy / governance (Stage 5)

These are essential for Paperhat to explain and govern itself.

## Band B — follows once A is workable

* product / offering (Stage 6)
* documentation / guides (Stage 7)

These are essential for public presence, operations, and commercialization.

## Band C — after A and B are stable

* contracts / agreements (Stage 8)
* publishing / books / media assets (Stage 9)
* training / learning linkage (Stage 10)

These are strategically important but depend on earlier coherence.

---

# Corpus Hygiene

## Domain Packages

All 69 committed domain packages are complete (6/6 artifacts). No domain package gaps remain.

## Vocabulary Packages

All 21 vocabulary packages are complete per the amended Package Completeness Definition (4 artifacts: manifest.cdx, vocabulary.cdx, README.md, localizations/en.cdx). No vocabulary package gaps remain.

## Behavior Packages (2 of 2 incomplete)

| Package | manifest | schema | README | localizations | examples | templates | Score |
|---|---|---|---|---|---|---|---|
| behavior-expression-schema | Y | Y | N | Y | N | N | 3/6 |
| behavior-shape-schema | Y | Y | N | Y | N | N | 3/6 |

- [ ] behavior-expression-schema — add README.md, examples/, templates/
- [ ] behavior-shape-schema — add README.md, examples/, templates/

---

# The Key Architectural Rule

At every stage, ask:

**Is this schema modeling a real institutional entity, or just a presentation surface?**

If it is only a presentation surface, it is a projection or composition schema, not primary truth.

That one rule will keep Lexis from collapsing into a CMS-shaped architecture.
