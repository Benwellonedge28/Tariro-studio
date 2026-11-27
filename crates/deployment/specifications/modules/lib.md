# Deployment service facade

**ZIP-DEPLOYMENT-LIB-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/lib.rs`

## Required implementation behavior

Expose artifact, verification, strategy and release ports. Linking or compiling grants no deployment permission.

## Acceptance

**ZIP-DEPLOYMENT-LIB-T01.** Facade can inspect artifact identity without contacting provider.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
