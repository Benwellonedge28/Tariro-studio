# Versioned scoped plugin grants

**ZIP-PLUGINS-PERMISSIONS-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/permissions.rs`

## Required implementation behavior

Intersect configured imports with owner grant and policy, revalidate each platform effect. Capability declaration does not grant execution scope.

## Acceptance

**ZIP-PLUGINS-PERMISSIONS-T01.** Read-only plug-in cannot request writes through host bridge.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
