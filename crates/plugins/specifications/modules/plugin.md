# Immutable plugin identity

**ZIP-PLUGINS-PLUGIN-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/plugin.rs`

## Required implementation behavior

Bind ID, vendor, version, artifact digest and qualified adapter. Runtime instance authority remains separately scoped.

## Acceptance

**ZIP-PLUGINS-PLUGIN-T01.** Same name with different artifact cannot replace approved instance.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
