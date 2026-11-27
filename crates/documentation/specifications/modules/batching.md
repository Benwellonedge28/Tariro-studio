# Scoped batch sealing

**ZIP-DOCUMENTATION-BATCHING-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/batching.rs`

## Required implementation behavior

Deduplicate normalized paths, apply authorized count, verify each candidate and persist deterministic sorted manifest. Short exact batch waits for revised authority.

## Acceptance

**ZIP-DOCUMENTATION-BATCHING-T01.** Thirty-file fixture rejects file 31; other approved counts work without static constants.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
