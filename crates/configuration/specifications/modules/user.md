# User preference overlay

**ZIP-CONFIGURATION-USER-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/user.rs`

## Required implementation behavior

Accept only registry keys writable by user preference. Migrate obsolete preferences explicitly and keep identity/keyring values opaque. Layer is immutable until reload passes validation.

## Acceptance

**ZIP-CONFIGURATION-USER-T01.** A preference cannot lower an enforced quality floor or add a privileged operation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
