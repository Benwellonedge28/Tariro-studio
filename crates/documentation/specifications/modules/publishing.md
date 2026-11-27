# Approved documentation publication

**ZIP-DOCUMENTATION-PUBLISHING-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/publishing.rs`

## Required implementation behavior

Seal reviewed diff, compare exact scope/count/head and call repository mutation only with live authorization. Reconcile remote receipts and preserve draft status.

## Acceptance

**ZIP-DOCUMENTATION-PUBLISHING-T01.** Branch moved since preview blocks publication before push.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
