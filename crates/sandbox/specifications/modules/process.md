# Process-tree containment

**ZIP-SANDBOX-PROCESS-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/process.rs`

## Required implementation behavior

Start processes inside preconfigured containment scope. Track opaque process identifiers and gateway lease; supervise descendants until exit.

## Acceptance

**ZIP-SANDBOX-PROCESS-T01.** Forked child stays inside containment and is counted during cleanup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
