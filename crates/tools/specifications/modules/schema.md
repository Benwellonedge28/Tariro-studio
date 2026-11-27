# Schema and adapter version constraints

**ZIP-TOOLS-SCHEMA-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/schema.rs`

## Required implementation behavior

Advertise supported value shapes and negotiated major/minor. Reject unsupported mandatory fields and unknown effect classes before invocation.

## Acceptance

**ZIP-TOOLS-SCHEMA-T01.** Valid response on incompatible major cannot enter runtime.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
