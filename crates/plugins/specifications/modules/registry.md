# Versioned plugin registry

**ZIP-PLUGINS-REGISTRY-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/registry.rs`

## Required implementation behavior

Index reviewed revisions under exact scope; compare-and-swap activation pointer and bounded registry quotas.

## Acceptance

**ZIP-PLUGINS-REGISTRY-T01.** Conflicting plugin version cannot shadow current active version.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
