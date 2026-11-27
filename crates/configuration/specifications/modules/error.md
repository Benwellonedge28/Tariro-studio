# Stable load failures

**ZIP-CONFIGURATION-ERROR-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/error.rs`

## Required implementation behavior

ConfigError::{UnsupportedSchema, UnknownKey, DuplicateKey, InvalidType, Oversize, PolicyConflict, Io, MigrationRequired}; include only registry key and origin class; layer read failures map to Io.

## Acceptance

**ZIP-CONFIGURATION-ERROR-T01.** Inject synthetic sensitive values into a parse failure and assert they are absent from errors.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
