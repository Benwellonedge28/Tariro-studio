# Typed assignment client

**ZIP-SDK-ASSIGNMENTS-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/assignments.rs`

## Required implementation behavior

Expose scoped create/read/transition requests with IDs, revision guards and safe mutation receipts.

## Acceptance

**ZIP-SDK-ASSIGNMENTS-T01.** Lost response requires reconciliation, not automatic second create.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
