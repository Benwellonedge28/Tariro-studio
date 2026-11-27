# Mandatory plugin containment

**ZIP-PLUGINS-SANDBOX-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/sandbox.rs`

## Required implementation behavior

Apply qualified filesystem, network, process, memory/fuel and host-import restrictions before start. Unavailable control denies.

## Acceptance

**ZIP-PLUGINS-SANDBOX-T01.** Missing required sandbox prevents plugin execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
