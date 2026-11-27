# Protocol error vocabulary

**ZIP-INTEROPERABILITY-ERROR-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/error.rs`

## Required implementation behavior

Distinguish unsupported major, bad schema, denied capability, transport error, quota, timeout and unknown effect. Redact sensitive addresses and payloads.

## Acceptance

**ZIP-INTEROPERABILITY-ERROR-T01.** Unknown protocol does not map to implicit compatibility.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
