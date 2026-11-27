# Documentation failure taxonomy

**ZIP-DOCUMENTATION-ERROR-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/error.rs`

## Required implementation behavior

Distinguish missing source, denied scope, invalid section, broken link, unsupported claim, unverifiable evidence and batch mismatch. Record safe path and requirement refs.

## Acceptance

**ZIP-DOCUMENTATION-ERROR-T01.** A blocked factual claim does not become successful prose generation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
