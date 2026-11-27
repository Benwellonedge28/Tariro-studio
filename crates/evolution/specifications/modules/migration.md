# Reviewed evolution migration

**ZIP-EVOLUTION-MIGRATION-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/migration.rs`

## Required implementation behavior

Stage validated compatible changes, verify state and qualified recovery under explicit scope; retain baseline until evidence permits transition.

## Acceptance

**ZIP-EVOLUTION-MIGRATION-T01.** Unknown persisted schema blocks activation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
