# Schema and adapter version constraints

**ZIP-TOOLS-SCHEMA-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/schema.rs`

## Boundary and inputs

Represent the supported versioned input and output shapes, mandatory fields, typed values, negotiated compatibility rules and effect class. Use a bounded qualified schema registry. Validate shapes before spawning, external transmission or interpreting a response. Unknown mandatory declarations or effect kinds deny.

## Behavior and failure handling

An accepted minor edition follows explicit compatibility rules and must preserve exact effect semantics and enforced constraints. An incompatible mandatory edition is unavailable. Store canonical descriptor digests with issuer and version. Distinguish response-shape parsing from evidence and permission validation.

## Acceptance

**ZIP-TOOLS-SCHEMA-T01.** Provide a valid-looking response from an incompatible major edition and verify it is unavailable for the owning operation. An unknown effect declaration must prevent invocation rather than be treated as read-only.
