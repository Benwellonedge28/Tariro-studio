# Isolated process plugin adapter

**ZIP-PLUGINS-PROCESS-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/process.rs`

## Required implementation behavior

Use approved executable identity and typed arguments under qualified sandbox. Process is isolated from parent secrets and arbitrary files.

## Acceptance

**ZIP-PLUGINS-PROCESS-T01.** Plugin exit does not imply descendant cleanup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
