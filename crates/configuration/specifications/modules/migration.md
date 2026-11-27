# Configuration schema migration

**ZIP-CONFIGURATION-MIGRATION-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/migration.rs`

## Required implementation behavior

migrate(old: RawLayer, target: SchemaVersion, route: &MigrationChain) -> Result<RawLayer, ConfigError>. Validate each declared edge and stage converted bytes separately; refuse unknown edges and incompatible lossy downgrades. Caller adopts only after full version validation.

## Acceptance

**ZIP-CONFIGURATION-MIGRATION-T01.** Interrupt before activation and prove original file and snapshot remain valid.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
