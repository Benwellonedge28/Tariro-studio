# Optional marketplace catalog

**ZIP-PLUGINS-MARKETPLACE-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/marketplace.rs`

## Required implementation behavior

Fetch through explicit approved network scope, classify untrusted metadata and require separate installation authority.

## Acceptance

**ZIP-PLUGINS-MARKETPLACE-T01.** Browsing catalog never installs or executes package.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
