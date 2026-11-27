# Plugin lifecycle facade

**ZIP-PLUGINS-LIB-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/lib.rs`

## Required implementation behavior

Expose approved manifests, registry and scoped host ports. No unrestricted native dynamic loading or marketplace startup.

## Acceptance

**ZIP-PLUGINS-LIB-T01.** Linked library activates no plugin.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
