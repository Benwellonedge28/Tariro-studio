# Effect intent/outcome taxonomy

**ZIP-AUDIT-OPERATION-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/operation.rs`

## Required implementation behavior

Bind effect kind and digest with local operation ID. Outcomes distinguish denied, pending, confirmed, failed and unresolved. Keep intent and result correlated.

## Acceptance

**ZIP-AUDIT-OPERATION-T01.** Lost remote response remains unresolved rather than success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
