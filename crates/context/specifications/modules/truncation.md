# Explicit optional omission

**ZIP-CONTEXT-TRUNCATION-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/truncation.rs`

## Required implementation behavior

Drop lowest-ranked optional items in stable order, record reason counts and preserve mandatory items. Reject any mandatory overflow.

## Acceptance

**ZIP-CONTEXT-TRUNCATION-T01.** Overfull mandatory bundle yields typed failure rather than clipping.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
