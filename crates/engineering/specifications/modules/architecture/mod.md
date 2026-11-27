# Architecture contract boundary

**ZIP-ENGINEERING-ARCHITECTURE-MOD-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/architecture/mod.rs`

## Required implementation behavior

Route system/component/interface/graph decisions through pinned reviewable DTOs. No feature implements itself by diagram update.

## Acceptance

**ZIP-ENGINEERING-ARCHITECTURE-MOD-T01.** Changing an architecture draft does not activate an adapter.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
