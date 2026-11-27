# Pinned document inventory

**ZIP-DOCUMENTATION-INVENTORY-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/inventory.rs`

## Required implementation behavior

Capture normalized docs and immutable source objects, stated role, current status, and dependency edges. Preserve snapshot identity across planning.

## Acceptance

**ZIP-DOCUMENTATION-INVENTORY-T01.** Repository move after pin cannot alter analyzed inventory.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
