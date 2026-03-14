Status: INFORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Temporal Conformance Appendix

This appendix records the conformance boundary for the temporal Behavior
binding.

This document is **Informative**.

---

## 1. Authority

Core temporal conformance is defined by:

- [Paperhat Temporal](/Users/guy/Workspace/@paperhat/specifications/paperhat-temporal/spec/1.0.0/index.md)

The temporal Behavior binding does not define an independent temporal algebra,
independent temporal diagnostics, or independent temporal test vectors.

---

## 2. No Independent Vectors

This appendix currently defines no standalone test vector corpus.

Any implementation that claims conformance for Behavior temporal bindings MUST
conform to `paperhat-temporal` itself and MUST expose no conflicting temporal
surface.

If a future derived convenience layer is specified for Behavior temporal
functions, that layer MUST provide its own separate conformance vectors and
MUST NOT redefine the core temporal rules.

---

**End of Temporal Conformance Appendix v1.0.0**
