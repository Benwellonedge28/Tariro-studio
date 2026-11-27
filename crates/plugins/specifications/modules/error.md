# Plugin failure vocabulary

**ZIP-PLUGINS-ERROR-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/error.rs`

## Required implementation behavior

Separate invalid manifest, incompatible API, denied import, sandbox unavailable, resource exhaustion, revoke and rollback failure.

## Acceptance

**ZIP-PLUGINS-ERROR-T01.** Plugin denied network receives typed error, not fallback privilege.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
