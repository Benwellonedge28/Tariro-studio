# Scoped host capability bridge

**ZIP-PLUGINS-HOST-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/host.rs`

## Required implementation behavior

Validate each import/operation and payload, enforce exact grant and lease, record outcome and suppress secret leakage.

## Acceptance

**ZIP-PLUGINS-HOST-T01.** Host import with changed actor or epoch fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
