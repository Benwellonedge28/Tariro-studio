# Optional remote storage adapter

**ZIP-STORAGE-BACKENDS-REMOTE-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backends/remote.rs`

## Required implementation behavior

Negotiate scope, capability, durability and conditional mutations before use. Require explicit egress per workspace and classify unknown acknowledgements by durable operation ID. Avoid relying on enumeration of eventually consistent listings for confirmation.

## Acceptance

**ZIP-STORAGE-BACKENDS-REMOTE-T01.** Lost acknowledgement triggers exact-key reconciliation; offline mode emits no network request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
