# Pinned repository client

**ZIP-SDK-REPOSITORIES-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/repositories.rs`

## Required implementation behavior

Require stable repository ID and revision for review, support writes only as scoped typed requests with reconcile fields.

## Acceptance

**ZIP-SDK-REPOSITORIES-T01.** Old approval for different reviewed head cannot push.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
