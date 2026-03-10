Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Step

A single action in a procedure — an instruction to be performed, with optional metadata indicating whether the step is required or optional.

## When to Use

Use `Step` inside a Procedure to represent an individual instruction. The step's text content is the instruction itself. Step is a semantic concept distinct from ListItem: a ListItem is a typographic primitive (an item in a list), while a Step is an executable action in a procedural sequence.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| isOptional | $Boolean | no | Whether this step is optional. Defaults to false (required) when omitted. |

## Content

Step requires text content (`RequiresContent whitespaceMode=$Flow`). The instruction text is the content of the Step element, following the same pattern as Paragraph, Requirement, and Note.

## Constraints

Text content is required. A step with no instruction is meaningless.

## Design Notes

- `$MustNotBeEntity` because steps are embedded within procedures, not cross-referenced independently.
- `RequiresContent` follows the same pattern as Paragraph and Requirement — the instruction text IS the content, not a trait.
- Pure leaf with no imports. The composing schema wires Step as a child of Procedure and can also wire substep nesting (Step within Step) or Admonition children for warnings mid-procedure.
- `isOptional` is the only trait because step semantics are minimal: the instruction text is content, and ordering comes from the parent's CollectionRules.

---

**End of Step v1.0.0**
