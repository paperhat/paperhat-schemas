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

Vocabulary packages follow the same pattern but use VocabularyPackageManifest and `vocabulary.cdx` instead of schema.cdx.

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

### Proposed Concepts — Needing Triage

These concepts were proposed in the original roadmap but do not exist as schema packages. Each must be triaged as: **create** (new leaf), **fold** (into an existing or new composite), or **reject** (not needed as standalone).

| Proposed Concept | Triage Decision | Rationale |
|---|---|---|
| OrganizationalUnit | NEEDS DECISION | Does not exist. Could be a leaf or a child within Organization. |
| Project | NEEDS DECISION | Does not exist. Needed for representing Codex, Gloss, Lexis, etc. |
| Repository | NEEDS DECISION | Does not exist. Could be a trait on Project or standalone. |
| Role | NEEDS DECISION | Does not exist. Needed for author/editor/maintainer assignments. |
| Responsibility | NEEDS DECISION | Does not exist. Could fold into Role. |
| Authority | NEEDS DECISION | Does not exist. Could fold into Role. |
| Party | NEEDS DECISION | Abstract person-or-organization. Could be a union concept or unnecessary if Person and Organization are imported separately. |
| Jurisdiction | NEEDS DECISION | Does not exist. Needed by Policy and Contract stages. |
| EffectivePeriod | NEEDS DECISION | Does not exist. Temporal exists (dates and ranges) — is it sufficient? |
| Status | NEEDS DECISION | Work already has a `status` trait. Is a standalone Status schema needed? |
| Document | NEEDS DECISION | Abstract base for all document types. Might be unnecessary given DocumentMetadata. |
| StructuralUnit | NEEDS DECISION | Section already exists and is LOCKED. Is a separate abstract concept needed? |
| Name / Label | NEEDS DECISION | PersonName exists. Is a general-purpose Name leaf needed for non-person names? |
| Definition | NEEDS DECISION | Description exists. Is a separate Definition concept needed (term + definition pair)? |
| MediaAsset | NEEDS DECISION | MediaReference exists (LOCKED). Is a separate MediaAsset (the asset itself vs. a reference to it) needed? |
| Reference / Citation | NEEDS DECISION | Reference exists (LOCKED). Is a separate Citation concept needed for bibliographic references? |

### Existing Vocabularies (all LOCKED)

bcp-47-languages, e164-calling-codes, iana-time-zones, iso-3166-countries, iso-4217-currencies, food-categories, preparations, units-angle, units-area, units-data, units-electrical, units-energy, units-force, units-frequency, units-length, units-mass, units-pressure, units-speed, units-temperature, units-time, units-volume.

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
| specification | UNLOCKED | Complete — 6 artifacts. Has: Specification, Section, Paragraph, OrderedList, UnorderedList, ListItem, CodeBlock, Requirement, Definition, Note, SectionReference, ExternalReference. |
| specification-foundation | UNLOCKED | Complete — 6 artifacts. Shared traits and enumerations for specification schemas. |
| specification-rfc2119 | UNLOCKED | Complete — 6 artifacts. Full RFC 2119 variant with all modality keywords. |

### Proposed Concepts — Needing Gap Analysis

| Proposed Concept | Existing Coverage | Gap Status |
|---|---|---|
| Specification | Exists in `specification` | Covered |
| NormativeStatement | Requirement concept with modality trait | Likely covered |
| DefinitionEntry | Definition concept with `term` trait | Likely covered |
| RequirementSet | No grouping concept exists | NEEDS DECISION |
| Example | `example` schema exists (separate package, LOCKED) | Likely covered via import |
| Appendix / Annex | Section with `division=$Appendix` trait | Likely covered |
| Reference / BibliographyEntry | ExternalReference + Reference leaf | NEEDS DECISION — is BibliographyEntry needed? |
| ConformanceRequirement | Requirement with specific modality | NEEDS DECISION — separate concept or just a Requirement? |
| FormalNote / InformativeNote | Note concept exists | Likely covered |
| TermBinding | No explicit concept | NEEDS DECISION |
| Issue / OpenQuestion | Not present | NEEDS DECISION |

### Dependencies

* Stage 1 foundational vocabulary
* Any new Stage 1 leaves identified during triage

### Gate

A real Paperhat specification can be authored, validated, and projected end-to-end in Lexis.

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

### Proposed Concepts — Needing Gap Analysis

| Proposed Concept | Existing Coverage | Gap Status |
|---|---|---|
| WhitePaper | Exists, LOCKED | Covered |
| Article / Essay | Essay exists, LOCKED | Covered |
| Abstract | Exists in WhitePaper | Covered |
| Claim / SupportingArgument / Evidence | Not present. WhitePaper design notes explicitly state these are rhetorical patterns within prose, not structural units. | Likely intentionally excluded |
| Citation / BibliographyEntry | Reference exists (LOCKED). Notes handles footnotes. | NEEDS DECISION |
| Figure | Exists, LOCKED | Covered |
| Table | Relation exists (UNLOCKED) for tabular data | NEEDS DECISION |
| Footnote / Endnote | Notes/Note exists, LOCKED | Covered |
| Series | Exists, LOCKED | Covered |
| PublicationEvent | Not present | NEEDS DECISION |
| Contributor | Person exists. Work has `author` trait. | NEEDS DECISION |

### Dependencies

* Stage 1 foundational vocabulary
* WhitePaper and Essay are LOCKED — new concepts must be new packages, not modifications

### Gate

Existing Paperhat white papers can be represented semantically and projected to web/PDF cleanly.

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

### Missing Schemas

These do not exist and were proposed in the original roadmap:

* OrganizationalUnit
* Project
* Brand
* ProductLine
* Repository
* Role
* Responsibility
* AuthorityAssignment
* Membership / Assignment
* Relationship (cross-entity)
* Domain / Property / Asset

### Dependencies

* Stage 1 foundational vocabulary (especially Role, Project, and other new leaves from Stage 1 triage)

### Gate

Paperhat's organizational and project structure can be represented canonically and reused elsewhere.

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

None specific to policy. Will import from Stage 1 leaves and Stage 4 organizational schemas.

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
* Jurisdiction (from Stage 1)
* EffectivePeriod (from Stage 1, or use Temporal)
* Enforcement / Consequence
* ReviewRequirement
* ApprovalRequirement

### Dependencies

* Stage 1 foundational vocabulary
* Stage 4 organization/authority model

### Gate

Paperhat can model its own policies as semantic entities rather than prose pages.

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

### Dependencies

* Stage 1 foundational vocabulary
* Stage 4 organization/project model

### Gate

Paperhat offerings can be described once and reused consistently across sales pages, documentation, proposals, and agreements.

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

### Dependencies

* Stage 1 foundational vocabulary
* Stage 6 product/offering model
* Structural schemas (section, text, list, narrative)

### Gate

Paperhat can maintain real user and internal operational documentation in Lexis.

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
* Party (imports from Stage 1 if created)
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
* Jurisdiction (from Stage 1)
* ApprovalState
* ClauseLibraryEntry
* Variant

### Dependencies

* Stage 5 policy/governance schema family
* Stage 4 organization/party/role models
* Stage 6 product/service/offering schema family

### Gate

Paperhat can author and manage at least basic internal agreements through Lexis.

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

### Proposed Additional Concepts

* Publication
* Book
* Edition
* Release
* Contributor
* FormatVariant
* RightsStatement
* MediaAsset (the asset itself, vs. MediaReference which is a pointer)
* CoverAsset
* PublicationEvent

### Dependencies

* Stage 3 white paper/article/publication model
* Stage 1 foundational vocabulary

### Gate

Books and other publication assets can be represented as first-class semantic entities and projected consistently.

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

### Dependencies

* Stage 6 product/offering model
* Stage 3 publication model

### Gate

Paperhat can describe training and learning offerings in Lexis even before Praxis fully operationalizes them.

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

# Incomplete Packages in Existing Corpus

The following existing packages are missing one or more of the six required artifacts:

| Schema | Missing Artifacts |
|---|---|
| paperhat-energy-measure | examples/, templates/ |
| paperhat-mass-measure | examples/, templates/ |
| paperhat-time-measure | examples/, templates/ |
| paperhat-volume-measure | examples/, templates/ |
| material | README.md, examples/, templates/ |
| sensory-profile | README.md, localizations/, examples/, templates/ |

These must be completed as part of general corpus hygiene, independent of stage progression.

---

# The Key Architectural Rule

At every stage, ask:

**Is this schema modeling a real institutional entity, or just a presentation surface?**

If it is only a presentation surface, it is a projection or composition schema, not primary truth.

That one rule will keep Lexis from collapsing into a CMS-shaped architecture.
