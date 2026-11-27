# Local staged model import

**ZIP-MODELS-IMPORT-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/import.rs`

## Required implementation behavior

Validate source scope and safe file identity, stage immutable assets, check all digests, format and license evidence, then register.

## Acceptance

**ZIP-MODELS-IMPORT-T01.** Corrupt shard yields no ready registration.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
