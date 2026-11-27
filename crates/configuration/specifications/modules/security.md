# Security configuration validation

**ZIP-CONFIGURATION-SECURITY-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/security.rs`

## Required implementation behavior

Validate mandatory isolation, owner authority, data classes and egress. Resolve credential references only in approved adapters, never in configuration snapshots.

## Acceptance

**ZIP-CONFIGURATION-SECURITY-T01.** Missing required sandbox capability disables affected operation; serialized snapshot contains no secret.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
