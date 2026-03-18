Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# ContactPoint

A method of contact such as email address, phone number, or website, with optional temporal validity.

**Package:** `paperhat-contact-point`
**Schema ID:** `paperhat:domain:contact-point`

---

## When to Use

Use ContactPoint whenever you need to represent a way to reach a person, organization, or other entity. A single entity has multiple ContactPoint instances to capture work contacts, personal contacts, emergency contacts, and other variants.

ContactPoint is a leaf concept with no concept dependencies. It is designed to be composed into higher-level schemas such as Person or Organization.

---

## Traits

### contactKind

A token classifying the role this contact point plays. Common values include `$work`, `$personal`, `$home`, `$emergency`, `$billing`, `$support`.

This is an open vocabulary — any token value is valid. The consuming schema constrains which values are accepted.

### emailAddress

An email address. Note: this is the *address*, not the email itself. An email is a document; an email address is a reachable endpoint.

### phoneNumber

A phone number. Note: this is the *number*, not the phone itself. A phone is a device; a phone number is a reachable endpoint. Include the country code for international numbers.

### website

An IRI (Internationalized Resource Identifier) for a website. Uses the $Iri value type, which requires an absolute address.

### effectiveFrom / effectiveTo

PlainDate values defining the period during which this contact point is valid. Useful for temporary assignments, seasonal contacts, or archived records.

A contact point with no dates is assumed to be current and unbounded.

---

## Constraints

At least one of `emailAddress`, `phoneNumber`, or `website` must be present. A ContactPoint with only metadata (contactKind, dates) and no actual contact method is invalid.

---

## Design Notes

**Why emailAddress and not email?** Precision matters. An email is a document you read. An email address is where you send it. Codex does not tolerate sloppy terminology.

**Why phoneNumber and not phone?** Same principle. A phone is a device. A phone number is a reachable identifier.

**Why $Iri for website?** A website is an absolute address. Relative references are meaningless as a contact method. $Iri enforces this.

**Why contactKind and not just kind?** Follows the naming pattern established by PersonName's `nameKind`. The prefix disambiguates when traits are discussed outside their concept context.

**End of ContactPoint v1.0.0**
