# Reviewed layout restructuring

**ZIP-ENGINEERING-REFACTORING-RESTRUCTURING-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/refactoring/restructuring.rs`

## Required implementation behavior

Inventory moved paths, public API impact and cross-links. Require explicit move/deletion scope and revalidate old/new identities.

## Acceptance

**ZIP-ENGINEERING-REFACTORING-RESTRUCTURING-T01.** Move outside approved parent scope fails before staging.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
