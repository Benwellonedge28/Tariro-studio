# Manifest and lifecycle client

**ZIP-SDK-PLUGINS-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/plugins.rs`

## Required implementation behavior

Use negotiated plugin registry and approved install/activation operations, record actual status. No auto-install from discovered metadata.

## Acceptance

**ZIP-SDK-PLUGINS-T01.** Unqualified plugin capability does not dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
