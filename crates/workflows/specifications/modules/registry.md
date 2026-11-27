# Versioned workflow registry

**ZIP-WORKFLOWS-REGISTRY-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/registry.rs`

## Required implementation behavior

Index qualified workflow identity and immutable revisions. Activation changes pointer with compare-and-swap and durable evidence.

## Acceptance

**ZIP-WORKFLOWS-REGISTRY-T01.** Identical aliases cannot shadow approved exact version.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
