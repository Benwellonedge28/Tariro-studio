# Qualified formal verification boundary

**ZIP-VERIFICATION-FORMAL-MOD-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/formal/mod.rs`

## Required implementation behavior

Route specification, invariant and proof requests through supported checking adapters. Unsupported proof format remains unavailable.

## Acceptance

**ZIP-VERIFICATION-FORMAL-MOD-T01.** No textual proof claim can become observed formal evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
