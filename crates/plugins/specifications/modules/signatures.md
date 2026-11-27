# Trusted package verification

**ZIP-PLUGINS-SIGNATURES-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/signatures.rs`

## Required implementation behavior

Check manifest/artifact digest, domain, known trusted key and scope before install. Fail closed when signatures required.

## Acceptance

**ZIP-PLUGINS-SIGNATURES-T01.** A signature for other bytes does not authorize installation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
