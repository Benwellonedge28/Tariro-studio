# Immutable revision pinning

**ZIP-REPOSITORY-SNAPSHOT-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/snapshot.rs`

## Required implementation behavior

Resolve requested ref to immutable commit then read target tree. Preserve recorded reference and exact resolved ID. Later ref movement requires a new pin and revalidation.

## Acceptance

**ZIP-REPOSITORY-SNAPSHOT-T01.** Branch advance after pin cannot alter inspected content or candidate base.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
