# Contained descendant control

**ZIP-TERMINAL-PROCESS-TREE-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/process_tree.rs`

## Required implementation behavior

Track descendants with sandbox-qualified scope, terminate only owned group and verify no live processes retain lease resources.

## Acceptance

**ZIP-TERMINAL-PROCESS-TREE-T01.** A spawned child holding output pipe cannot survive reported cleanup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
