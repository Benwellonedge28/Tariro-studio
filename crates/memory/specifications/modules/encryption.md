# Scoped confidentiality envelope

**ZIP-MEMORY-ENCRYPTION-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/encryption.rs`

## Required implementation behavior

Use qualified authenticated encryption and scope/version binding. Resolve key reference only in adapter and reject failed verification.

## Acceptance

**ZIP-MEMORY-ENCRYPTION-T01.** Encrypted record from another tenant cannot decrypt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
