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
| policy | UNLOCKED | Complete — 6 artifacts. Imports: jurisdiction |
| tier | UNLOCKED | Complete — 6 artifacts |
| procedure | UNLOCKED | Complete — 6 artifacts |
| step | UNLOCKED | Complete — 6 artifacts |
| contract | UNLOCKED | Complete — 6 artifacts. Imports: jurisdiction |
| clause | UNLOCKED | Complete — 6 artifacts |
| publication | UNLOCKED | Complete — 6 artifacts |
| release | UNLOCKED | Complete — 6 artifacts |
| learning-offering | UNLOCKED | Complete — 6 artifacts |

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
| EffectivePeriod | REJECTED | Temporal already handles date ranges. A separate concept for start/end date pairs duplicates existing capability. |
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
| specification | UNLOCKED | Complete — 6 artifacts. Has: Specification, Section, Paragraph, OrderedList, UnorderedList, ListItem, CodeBlock, Requirement, RequirementSet, Definition, Note, TermBinding, Issue, OpenQuestion, SectionReference, ExternalReference. Imports: citation, admonition, code, example, figure, list, relation, text, specbase. |
| specification-foundation | UNLOCKED | Complete — 6 artifacts. Shared traits and enumerations for specification schemas. Includes DraftItemStatus enum and traits for source, status, resolution, answer. |
| specification-rfc2119 | UNLOCKED | Complete — 6 artifacts. Full RFC 2119 variant with all modality keywords. Same concept set as specification. |

### Proposed Concepts — Gap Analysis

| Proposed Concept | Existing Coverage | Gap Status |
|---|---|---|
| Specification | Exists in `specification` | Covered |
| NormativeStatement | Requirement concept with modality trait | Covered |
| DefinitionEntry | Definition concept with `term` trait | Covered |
| RequirementSet | RequirementSet concept in both specification schemas | Covered |
| Example | `example` schema exists (separate package, LOCKED), imported by specification schemas | Covered via import |
| Appendix / Annex | Section with `division=$Appendix` trait | Covered |
| Reference / BibliographyEntry | ExternalReference + Reference leaf + Citation (imported as `cite:Citation` child of Section) | REJECTED — Citation covers bibliographic references fully. A bibliography is a Section containing Citation children. |
| ConformanceRequirement | Requirement with `modality` trait + Section's `conformance` trait | REJECTED — Requirement with modality covers this. Conformance is a property of context (Section), not a separate concept type. |
| FormalNote / InformativeNote | Note concept exists | Covered |
| TermBinding | TermBinding concept in both specification schemas | Covered |
| Issue / OpenQuestion | Issue and OpenQuestion concepts in both specification schemas, with DraftItemStatus enum | Covered |

### Stage 2 Checklist

- [x] specification — exists, UNLOCKED, 6/6
- [x] specification-foundation — exists, UNLOCKED, 6/6
- [x] specification-rfc2119 — exists, UNLOCKED, 6/6
- [x] RequirementSet — committed
- [x] TermBinding — committed
- [x] Issue / OpenQuestion — committed
- [x] ~~Reference / BibliographyEntry~~ — rejected (Citation covers this)
- [x] ~~ConformanceRequirement~~ — rejected (Requirement with modality covers this)
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
| Table | Relation (RelationType + RelationInstance) models tabular data semantically | REJECTED — "Table" is a presentation surface. Relation handles structured data. |
| Footnote / Endnote | Notes/Note exists, LOCKED | Covered |
| Series | Exists, LOCKED | Covered |
| PublicationEvent | Event exists (LOCKED, 6/6) with `eventKind` trait | REJECTED — A publication event is an Event with `eventKind=$Publication`. |
| Contributor | Citation:Contributor exists. Work has `author`. Role handles named functions. | REJECTED — Already covered by existing schemas. |

### Stage 3 Checklist

- [x] white-paper — LOCKED, 6/6
- [x] essay — LOCKED, 6/6
- [x] narrative — LOCKED, 6/6
- [x] document-metadata — LOCKED, 6/6
- [x] notes — LOCKED, 6/6
- [x] figure — LOCKED, 6/6
- [x] series — LOCKED, 6/6
- [x] citation — LOCKED, 6/6
- [x] ~~Table~~ — rejected (Relation covers tabular data; "Table" is a presentation surface)
- [x] ~~PublicationEvent~~ — rejected (Event with `eventKind=$Publication`)
- [x] ~~Contributor~~ — rejected (Citation:Contributor + Work + Role cover this)
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
| brand | UNLOCKED | Complete — 6 artifacts. |

### Proposed Concepts — Triage Results

| Proposed Concept | Decision | Rationale |
|---|---|---|
| Brand | CREATED | `brand` package exists (6/6). Real entity with identity referenced by products, marketing, and legal documents. |
| ProductLine | REJECTED | Defer to Stage 6. Grouping handled by Series and Tags. If Stage 6 needs it, create it then. |
| AuthorityAssignment | REJECTED | Role with `roleKind` and `scope` covers authority assignment. If Stage 5 policy modeling reveals a gap, create a policy-specific concept there. |
| Membership / Assignment | REJECTED | Role with `roleKind=$member` or `$assignee` and scope handles this. Higher-level composers will compose Role + Temporal as children of Organization. |
| Relationship (cross-entity) | REJECTED | Do not create a second generic relationship package. Use `relation`, `reference`, or domain-specific semantics where appropriate. |
| Domain / Property / Asset | REJECTED | Too broad. Domain names are Identifiers. Physical/digital assets are covered by MediaAsset and Product. Create focused leaves if a specific asset type proves necessary. |

### Stage 4 Checklist

- [x] organization — complete, 6/6
- [x] person — complete, 6/6
- [x] project — complete, 6/6
- [x] role — complete, 6/6
- [x] OrganizationalUnit — created as `organizational-unit` (Stage 1 leaf)
- [x] Repository — created as `repository` (Stage 1 leaf)
- [x] Brand — created as `brand`
- [x] ~~ProductLine~~ — rejected (defer to Stage 6)
- [x] ~~AuthorityAssignment~~ — rejected (Role covers this)
- [x] ~~Membership / Assignment~~ — rejected (Role covers this)
- [x] ~~Relationship (cross-entity)~~ — rejected (too generic)
- [x] ~~Domain / Property / Asset~~ — rejected (too broad)
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

### Proposed Concepts — Triage Results

| Proposed Concept | Decision | Rationale |
|---|---|---|
| Policy | CREATED | `policy` package exists (6/6). Core institutional concept with stable identity. Imports jurisdiction as child. |
| PolicyDocument | REJECTED | `Work` already models documents; a policy document is a Work with `workKind=$Policy`. |
| Rule | REJECTED | No separate universal `Rule` package yet. Policy semantics still need internal machine-actionable structure, but the current corpus does not yet justify a standalone universal leaf package. |
| Obligation | REJECTED | Not a separate top-level package. Obligation is a deontic statement kind inside policy structure, not just free prose and not a standalone universal leaf. |
| Permission | REJECTED | Not a separate top-level package. Permission is a deontic statement kind inside policy structure, not just free prose and not a standalone universal leaf. |
| Prohibition | REJECTED | Not a separate top-level package. Prohibition is a deontic statement kind inside policy structure, not just free prose and not a standalone universal leaf. |
| Condition | REJECTED | No separate universal package yet. Conditions belong inside explicit policy structure unless a shared cross-domain condition model is proven necessary. |
| Exception | REJECTED | No separate universal package yet. Exceptions belong inside explicit policy structure unless a shared cross-domain model is proven necessary. |
| Scope | REJECTED | A trait on Policy (jurisdiction + prose), not a standalone concept. Jurisdiction already exists for geographic/legal scope. |
| ResponsibleParty | REJECTED | Covered by Role + Relation patterns. A role assignment with `roleKind=$PolicyOwner` handles this. |
| Enforcement / Consequence | REJECTED | No separate universal package yet. Enforcement semantics belong inside explicit policy structure unless a shared cross-domain model is proven necessary. |
| ReviewRequirement | REJECTED | A property of a policy (trait-level), not its own entity. |
| ApprovalRequirement | REJECTED | A property of a policy (trait-level), not its own entity. Role covers who approves. |

### Stage 5 Checklist

- [x] jurisdiction — LOCKED, 6/6
- [x] Policy — CREATED, 6/6
- [x] ~~PolicyDocument~~ — rejected
- [x] ~~Rule~~ — rejected
- [x] ~~Obligation~~ — rejected
- [x] ~~Permission~~ — rejected
- [x] ~~Prohibition~~ — rejected
- [x] ~~Condition~~ — rejected
- [x] ~~Exception~~ — rejected
- [x] ~~Scope~~ — rejected
- [x] ~~ResponsibleParty~~ — rejected
- [x] ~~Enforcement / Consequence~~ — rejected
- [x] ~~ReviewRequirement~~ — rejected
- [x] ~~ApprovalRequirement~~ — rejected
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

### Proposed Concepts — Triage Results

| Proposed Concept | Decision | Rationale |
|---|---|---|
| Tier / Plan | CREATED | `tier` package exists (6/6). Named packaging level (FOSS/Pro/Premium) with stable identity, distinct from Product. |
| Service | REJECTED | Product with `productKind=$Service` covers current known needs. Reopen only if real corpus work proves a service-only trait surface that Product cannot express cleanly. |
| Offering | REJECTED | Union type over product-or-service. Same reasoning as Party rejection — adds indirection without semantic value. |
| Feature | REJECTED | Descriptive content within a tier or product. Express as Description/List children, not a standalone entity. |
| Capability | REJECTED | Synonym for Feature. Same reasoning. |
| Eligibility | REJECTED | A trait or prose within Tier/Product/Offer, not a standalone entity. Too abstract. |
| Dependency / Prerequisite | REJECTED | Relation with `relationKind=$Requires` covers inter-tier/inter-product dependencies. |
| Deliverable | REJECTED | A deliverable is a Product, Work, or prose content. No distinct identity or trait set. |
| SupportEntitlement | REJECTED | A Tier with `tierKind=$Support` or Product with `productKind=$Support`. No unique trait set. |
| PriceModel | REJECTED | Offer already models pricing. Price model type is a trait on Offer, not a standalone entity. |
| SubscriptionTerm | REJECTED | A trait on Offer or Tier (`billingPeriod=$Monthly`). Duration already exists for time spans. |

### Stage 6 Checklist

- [x] product — LOCKED, 6/6
- [x] offer — LOCKED, 6/6
- [x] Tier / Plan — CREATED, 6/6
- [x] ~~Service~~ — rejected
- [x] ~~Offering~~ — rejected
- [x] ~~Feature~~ — rejected
- [x] ~~Capability~~ — rejected
- [x] ~~Eligibility~~ — rejected
- [x] ~~Dependency / Prerequisite~~ — rejected
- [x] ~~Deliverable~~ — rejected
- [x] ~~SupportEntitlement~~ — rejected
- [x] ~~PriceModel~~ — rejected
- [x] ~~SubscriptionTerm~~ — rejected
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

### Proposed Concepts — Triage Results

| Proposed Concept | Decision | Rationale |
|---|---|---|
| Procedure | CREATED | `procedure` package exists (6/6). Distinct semantic concept: an executable instruction sequence, not a narrative work. `$MustBeEntity`. |
| Step | CREATED | `step` package exists (6/6). Semantically distinct from ListItem: an action in a procedure, not a typographic bullet. `$MustNotBeEntity`, `RequiresContent`. |
| Guide | REJECTED | Work with `workKind=$Guide`. No unique traits beyond what Work provides. Structural content comes from composing Section, Paragraph, Step, etc. |
| Task | REJECTED | Overlaps with Procedure. A task is a goal; a procedure is its execution. One concept suffices. |
| Prerequisite | REJECTED | Content within a procedure (a section or admonition), not a standalone concept. |
| Outcome | REJECTED | A trait on Step or content within a procedure. No independent identity needed. |
| TroubleshootingItem | REJECTED | Pattern (symptom/cause/resolution) is thin — three text traits. KB articles are Works; troubleshooting entries are content within them. |
| KnownIssue | REJECTED | Specification schema already defines Issue and OpenQuestion. If standalone known-issue tracking is needed, extract later. |
| ReferenceEntry | REJECTED | TermEntry covers term + definition pairs. API-specific reference structure is too specialized for a generic schema. |
| Environment / Platform | REJECTED | Borderline — has version constraints Tags do not model. But too specialized for v1.0.0. Add later if platform requirements become a recurring pattern. |
| ChecklistItem | REJECTED | Checked/unchecked is runtime state, not schema structure. A checklist is a List with semantic annotation. |

### Stage 7 Checklist

- [x] Procedure — CREATED, 6/6
- [x] Step — CREATED, 6/6
- [x] ~~Guide~~ — rejected
- [x] ~~Task~~ — rejected
- [x] ~~Prerequisite~~ — rejected
- [x] ~~Outcome~~ — rejected
- [x] ~~TroubleshootingItem~~ — rejected
- [x] ~~KnownIssue~~ — rejected
- [x] ~~ReferenceEntry~~ — rejected
- [x] ~~Environment / Platform~~ — rejected
- [x] ~~ChecklistItem~~ — rejected
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

### Proposed Concepts — Triage Results

| Proposed Concept | Decision | Rationale |
|---|---|---|
| Contract | CREATED | `contract` package exists (6/6). Core institutional entity for binding agreements. Imports jurisdiction. `$MustBeEntity`. |
| Clause | CREATED | `clause` package exists (6/6). Fundamental semantic building block of contracts. `clauseKind` absorbs Obligation, Right, PaymentTerm, ServiceLevel, Renewal, Termination. `$MayBeEntity`, `RequiresContent`. |
| Agreement | REJECTED | `contractKind=$MOU` or `$LetterOfIntent` covers non-binding agreements. Having both Contract and Agreement creates ambiguity. |
| Party | REJECTED | Union type. Import Person and Organization directly where needed. |
| Definition (legal) | REJECTED | TermEntry already models term + definition pairs. Legal definitions are term entries. |
| Obligation | REJECTED | A Clause with `clauseKind=$Obligation`. Deontic modality expressed in clause text, not as separate entity. |
| Right | REJECTED | A Clause with `clauseKind=$Grant`. Mirror of Obligation. |
| Condition | REJECTED | Content within a Clause ("If X, then Y"). Prose, not entity. |
| Exception | REJECTED | Content within a Clause ("Except for..."). Prose, not entity. |
| Deliverable | REJECTED | A Product, Tier, or Work. No distinct trait set. Same reasoning as Stage 6. |
| PaymentTerm | REJECTED | A Clause with `clauseKind=$Payment`. MonetaryAmount and Duration exist for structured parts. |
| ServiceLevel | REJECTED | A Clause with `clauseKind=$ServiceLevel`. SLA metrics expressed in clause content. |
| Term | REJECTED | Duration already exists. Contract term is a Duration child or trait. |
| Renewal | REJECTED | A Clause with `clauseKind=$Renewal`. |
| Termination | REJECTED | A Clause with `clauseKind=$Termination`. |
| Jurisdiction | EXISTS | Already exists from Stage 1. Imported by Contract as child. |
| ApprovalState | REJECTED | This is `contractStatus` on Contract — an enumerated token value, not a concept. |
| ClauseLibraryEntry | REJECTED | Application-level concept (template management), not a schema concept. |
| Variant | REJECTED | Application-level versioning/templating, not a schema concern. |

### Stage 8 Checklist

- [x] Contract — CREATED, 6/6
- [x] Clause — CREATED, 6/6
- [x] ~~Agreement~~ — rejected
- [x] ~~Party~~ — rejected
- [x] ~~Definition (legal)~~ — rejected
- [x] ~~Obligation~~ — rejected
- [x] ~~Right~~ — rejected
- [x] ~~Condition~~ — rejected
- [x] ~~Exception~~ — rejected
- [x] ~~Deliverable~~ — rejected
- [x] ~~PaymentTerm~~ — rejected
- [x] ~~ServiceLevel~~ — rejected
- [x] ~~Term~~ — rejected
- [x] ~~Renewal~~ — rejected
- [x] ~~Termination~~ — rejected
- [x] ~~ApprovalState~~ — rejected
- [x] ~~ClauseLibraryEntry~~ — rejected
- [x] ~~Variant~~ — rejected
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

### Proposed Concepts — Triage Results

| Proposed Concept | Decision | Rationale |
|---|---|---|
| Publication | CREATED | `publication` package exists (6/6). General published work entity. Fills gap between Work (descriptor, $MustNotBeEntity) and WhitePaper/Essay (specialized composers). `$MustBeEntity`. |
| Release | CREATED | `release` package exists (6/6). Versioned product artifact snapshot. Unique traits: releaseKind, releaseStatus, product reference. Distinct from Publication. `$MustBeEntity`. |
| Book | REJECTED | `publicationKind=$Book` on Publication. No unique structural requirements that warrant a separate schema. |
| Edition | REJECTED | Separate Publication instances linked by Relation. Work.version + Identifier (ISBN) handle edition metadata. |
| Contributor | REJECTED | Citation:Contributor + Role + DocumentMetadata already cover authorship/contribution three ways. |
| FormatVariant | REJECTED | MediaAsset children on Publication. Different-ISBN variants are separate Publication instances linked by Relation. |
| RightsStatement | REJECTED | Work.license for simple cases. Policy + Clause for complex licensing terms. Description for prose notices. |
| CoverAsset | REJECTED | MediaAsset with `assetKind=$Cover`. No unique traits. |
| PublicationEvent | REJECTED | Already rejected in Stage 3. Event with `eventKind=$Publication`. |

### Stage 9 Checklist

- [x] series — LOCKED, 6/6
- [x] media-reference — LOCKED, 6/6
- [x] media-asset — UNLOCKED, 6/6 (Stage 1 leaf)
- [x] Publication — CREATED, 6/6
- [x] Release — CREATED, 6/6
- [x] ~~Book~~ — rejected
- [x] ~~Edition~~ — rejected
- [x] ~~Contributor~~ — rejected
- [x] ~~FormatVariant~~ — rejected
- [x] ~~RightsStatement~~ — rejected
- [x] ~~CoverAsset~~ — rejected
- [x] ~~PublicationEvent~~ — rejected
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

Praxis owns the deeper learning engine, but Lexis still holds semantically useful descriptive and publishing layers.

### Purpose

Represent training offerings, learning materials, and public learning descriptions in a way that interoperates with Praxis later.

### Existing Schemas

None.

### Proposed Concepts — Triage Results

| Proposed Concept | Decision | Rationale |
|---|---|---|
| LearningOffering | CREATED | `learning-offering` package exists (6/6). Training catalog entity with unique `deliveryMode` trait. Product does not cover this (wrong traits, LOCKED). `$MustBeEntity`. |
| Module | REJECTED | Section with `sectionKind=$Module`. Deeper module semantics belong in Praxis. |
| LearningObjective | REJECTED | List items for the descriptive layer. Pedagogical metadata (Bloom's taxonomy) belongs in Praxis. |
| Prerequisite | REJECTED | Description for text prerequisites. Relation with `relationKind=$Requires` for structured references. Already rejected in Stage 7. |
| Artifact | REJECTED | MediaAsset with appropriate `assetKind` values. Work/Publication for metadata. |
| Assessment | REJECTED | Description content for the catalog layer. Assessment structure belongs in Praxis. |
| CompetencyReference / CapabilityReference | REJECTED | Tags for skill labels. Reference for links to Praxis competency entities. |
| Duration / EffortEstimate | REJECTED | Duration already exists (LOCKED, 6/6). Context (elapsed vs. effort) provided by composition. |
| CertificationPreparation | REJECTED | Relation with `relationKind=$PreparesFor` + Description content. |

### Stage 10 Checklist

- [x] LearningOffering — CREATED, 6/6
- [x] ~~Module~~ — rejected
- [x] ~~LearningObjective~~ — rejected
- [x] ~~Prerequisite~~ — rejected
- [x] ~~Artifact~~ — rejected
- [x] ~~Assessment~~ — rejected
- [x] ~~CompetencyReference / CapabilityReference~~ — rejected
- [x] ~~Duration / EffortEstimate~~ — rejected
- [x] ~~CertificationPreparation~~ — rejected
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

## Stage 11. Prism / Color Governance Application Schema Family

### Purpose

Represent Codex-native Prism project repositories and Prism result bundles as semantic color-governance artifacts.

This stage does not define retained color value semantics. `paperhat-color` owns retained color value semantics. This stage defines the authored document shapes that Prism, CLI surfaces, Lexis, and foundries consume above the Color substrate and extension-family crates.

### Proposed Package Set — Triage Results

| Proposed Package | Decision | Boundary |
|---|---|---|
| `paperhat-color-governance` | CREATED | Durable authored color-governance truth inside Prism project documents: `ColorSystem`, `Palette`, `PaletteMember`, `TokenSet`, `Token`, `SemanticRoleAssignment`, variant families, and publication-intent attachments. Owns authored organization of retained colors. Does not own derived audit findings, proof comparisons, or publication bundles. |
| `paperhat-color-policy` | CREATED | Durable authored policy objects referenced by Prism project documents: `AccessibilityPolicy`, `ContrastPolicy`, color-vision-deficiency simulation policy, `ProofPolicy`, `GamutMappingPolicy`, and governance approval rules. Owns thresholds, mapping strategy, and approval logic. Does not own derived findings or rendered outputs. |
| `paperhat-prism-project` | CREATED | Root Prism project-document composer. Imports generic Paperhat packages plus `paperhat-color-governance` and `paperhat-color-policy`. Owns `PrismProject`, project-scoped source references, review dispositions that are durable semantic governance state, and top-level publication scopes. Does not duplicate inner color-governance or policy concept definitions. |
| `paperhat-prism-result-bundle` | CREATED | Root Prism result-bundle package. Owns derived workflow outputs: accessibility audit bundles, proof bundles, export bundles, semantic-change bundles, and governance bundles with provenance snapshot, policy snapshot, and source references. Result bundles are not project authority. |
| `paperhat-color-audit` | REJECTED | Audit findings, repair suggestions, and regression entries belong inside Prism result bundles. A standalone audit package splits one workflow family across two authorities with no semantic gain. |
| `paperhat-color-proof` | REJECTED | Authored proof policy belongs in `paperhat-color-policy`. Derived proof outputs belong in `paperhat-prism-result-bundle`. A separate proof package cuts one coherent proof workflow in half. |
| `paperhat-color-role-graph` | REJECTED | Role graph and role assignment are inseparable from color-governance truth and belong inside `paperhat-color-governance`. |

### Package Boundary Rule

The Stage 11 package family follows one hard boundary:

- authored, durable semantic truth belongs in `paperhat-color-governance`, `paperhat-color-policy`, and `paperhat-prism-project`
- derived workflow outputs belong in `paperhat-prism-result-bundle`

No Stage 11 package defines view-shaped, pane-shaped, or foundry-shaped structures as primary truth.

### Stage 11 Checklist

- [x] `paperhat-color-governance` — author 6 artifacts
- [x] `paperhat-color-policy` — author 6 artifacts
- [x] `paperhat-prism-project` — author 6 artifacts
- [ ] `paperhat-prism-result-bundle` — author 6 artifacts
- [x] ~~paperhat-color-audit~~ — rejected
- [x] ~~paperhat-color-proof~~ — rejected
- [x] ~~paperhat-color-role-graph~~ — rejected
- [ ] Gate: Prism project documents and Prism result bundles validate as external schema packages in `schemas/paperhat-schemas`, and `prism-spec` references those packages rather than redefining them inline.

### Dependencies

* Stage 1 foundational vocabulary
* Stage 5 policy / governance / rule schema family
* Stage 9 publishing / media asset schema family

### First Paperhat Examples

* a brand palette project with semantic roles and accessibility policy
* an imported design-token set under explicit contrast and proof policy
* a cross-medium proof bundle for screen and print targets
* a semantic change bundle with role drift and contrast regression
* a governance bundle with approval outcome and policy snapshot

---

# Recommended Dependency Order

1. **Foundational vocabulary** (Stage 1)
2. **Specification** (Stage 2)
3. **White Paper / Article / Publication** (Stage 3)
4. **Organization / Governance structure** (Stage 4)
5. **Policy / Governance / Rules** (Stage 5)
6. **Prism / Color Governance application schemas** (Stage 11)
7. **Product / Service / Offering** (Stage 6)
8. **Documentation / Guide / Procedure** (Stage 7)
9. **Contract / Agreement** (Stage 8)
10. **Publishing / Book / Media asset** (Stage 9)
11. **Training / Learning linkage** (Stage 10)

---

# Priority Bands

## Band A — must exist early

* foundational vocabulary (Stage 1)
* specification (Stage 2)
* white paper / publication (Stage 3)
* organization (Stage 4)
* policy / governance (Stage 5)
* Prism / color governance application schemas (Stage 11)

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

All currently committed domain packages are complete (6/6 artifacts). The planned Prism / color governance application schema family in Stage 11 is not authored yet.

## Vocabulary Packages

All 21 vocabulary packages are complete per the amended Package Completeness Definition (4 artifacts: manifest.cdx, vocabulary.cdx, README.md, localizations/en.cdx). No vocabulary package gaps remain.

## Behavior Packages (0 incomplete)

| Package | manifest | schema | README | localizations | examples | templates | Score |
|---|---|---|---|---|---|---|---|
| behavior-expression-schema | Y | Y | Y | Y | Y | Y | 6/6 |
| behavior-shape-schema | Y | Y | Y | Y | Y | Y | 6/6 |

- [x] behavior-expression-schema — added README.md, examples/basic/example.cdx, templates/basic/template.cdx
- [x] behavior-shape-schema — added README.md, examples/basic/example.cdx, templates/basic/template.cdx

---

# The Key Architectural Rule

At every stage, ask:

**Is this schema modeling a real institutional entity, or just a presentation surface?**

If it is only a presentation surface, it is a projection or composition schema, not primary truth.

That one rule will keep Lexis from collapsing into a CMS-shaped architecture.
