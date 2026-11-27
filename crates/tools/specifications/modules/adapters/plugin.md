# Isolated plugin adapter

**ZIP-TOOLS-ADAPTERS-PLUGIN-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/adapters/plugin.rs`

## Required implementation behavior

Validate plugin identity/version, lifecycle and permitted host imports. Enforce fuel/memory and reconcile host effects independently.

## Acceptance

**ZIP-TOOLS-ADAPTERS-PLUGIN-T01.** Revoked plug-in cannot invoke host capability after lease change.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
