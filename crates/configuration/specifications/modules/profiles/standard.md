# Standard profile rules

**ZIP-CONFIGURATION-PROFILES-STANDARD-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/profiles/standard.rs`

## Required implementation behavior

Use resource-admitted concurrency with bounded active assignments. Admit model and agent slots by finite per-unit demand and observed capacity, then intersect mandatory caps. Profile name does not imply physical capacity.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-STANDARD-T01.** Same manifest on two host fixtures yields different admitted concurrency.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
