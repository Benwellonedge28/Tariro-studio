# Qualified GDB adapter

**ZIP-DEBUGGING-ADAPTERS-GDB-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/adapters/gdb.rs`

## Required implementation behavior

Pin executable/version and approved target; prefer controlled structured interface and enforce session containment. No unreviewed scripts.

## Acceptance

**ZIP-DEBUGGING-ADAPTERS-GDB-T01.** Unapproved command or process ID is denied before attach.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
