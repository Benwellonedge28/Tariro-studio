# Agent runtime boundary

**ZIP-AGENTS-LIB-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/lib.rs`

## Required implementation behavior

Export typed manifests, role descriptors and lifecycle/control ports; inject all runtime and policy adapters. No work launches during setup.

## Acceptance

**ZIP-AGENTS-LIB-T01.** A manifest can be inspected without executing any agent.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
