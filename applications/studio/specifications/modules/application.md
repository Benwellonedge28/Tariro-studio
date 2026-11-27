# UI event and request supervisor

**ZIP-STUDIO-APPLICATION-001 · v1.0 · Owner:** Studio maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/studio/src/application.rs`

## Required implementation behavior

Bound incoming actions, dispatch versioned gateway requests and reduce ordered replies. On gap request snapshot; do not reuse stale authorization or conflict state.

## Acceptance

**ZIP-STUDIO-APPLICATION-T01.** Reconnect with a gap recovers exact projection without double approval.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
