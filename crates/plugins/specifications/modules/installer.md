# Approved staged install

**ZIP-PLUGINS-INSTALLER-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/installer.rs`

## Required implementation behavior

Authorize source/destination, stage verified assets under finite quota, qualify manifest and prepare activation; do not auto-enable new effects.

## Acceptance

**ZIP-PLUGINS-INSTALLER-T01.** Cancel install preserves prior verified state.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
