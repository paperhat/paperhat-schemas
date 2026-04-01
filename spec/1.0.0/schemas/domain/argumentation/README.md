Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Argumentation

Formal argumentation primitives for modeling logical structure. An Argument contains Premises, an optional Inference, and a Claim.

## When to Use

Use these concepts to model formal or semi-formal reasoning in academic papers, policy documents, legal briefs, philosophical texts, and any context where the logical structure of an argument is semantically meaningful. An Argument is a container that organizes Premises (supporting propositions), an optional Inference (the logical step), and a Claim (the conclusion).

## Concepts

| Concept | Kind | Entity Eligibility | Content | Children | Description |
|---|---|---|---|---|---|
| Argument | $Semantic | $MustNotBeEntity | ForbidsContent | Premise (1+), Inference (0-1), Claim (1) | A logical argument composed of premises, inference, and claim. |
| Claim | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | A proposition asserted as true — the conclusion of an argument. |
| Premise | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | A supporting proposition that grounds the argument. |
| Inference | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | The logical step connecting premises to the claim. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | no | A stable identifier for cross-referencing. |
| label | $Text | no | A display label for numbering, such as "Argument 2.1". |
| language | $LanguageTag | no | BCP 47 language tag. |

## Constraints

- An Argument must contain at least one Premise.

## Design Notes

- Argument is an ordered collection. The conventional structure is premises followed by inference followed by claim, but the schema does not enforce a specific ordering — that is a discourse convention, not a semantic constraint.
- Inference is optional because many arguments are enthymematic (the logical step is implicit).
- Claim, Premise, and Inference all use flow content for Gloss span binding support.
- Pure leaf package with no imports. Composing schemas wire Argument as a child concept where formal reasoning is permitted.

---

**End of Argumentation v1.0.0**
