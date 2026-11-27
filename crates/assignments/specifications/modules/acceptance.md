# Assignment final acceptance

**ZIP-ASSIGNMENTS-ACCEPTANCE-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/acceptance.rs`

## Required implementation behavior

Ask verification port to assess exact candidate, grant and requirement digest. Required evidence passes only if observed matching results exist. Failed or blocked evidence prevents Completed.

## Acceptance

**ZIP-ASSIGNMENTS-ACCEPTANCE-T01.** Change a file after review; acceptance rejects stale evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
