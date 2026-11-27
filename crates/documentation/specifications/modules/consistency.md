# Cross-document rule compatibility

**ZIP-DOCUMENTATION-CONSISTENCY-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/consistency.rs`

## Required implementation behavior

Compare normative IDs, authority and effective meanings at one revision. Flag conflicts instead of preferring whichever file was read last.

## Acceptance

**ZIP-DOCUMENTATION-CONSISTENCY-T01.** Two docs defining different mandatory limits produce a blocker.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
