# Debugger role

**ZIP-AGENTS-ROLES-DEBUGGER-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/debugger.rs`

## Required implementation behavior

Reproduce failure under qualified adapter, record observations and propose patch with uncertainty. Do not mutate protected files implicitly.

## Acceptance

**ZIP-AGENTS-ROLES-DEBUGGER-T01.** Unknown reproduction gives hypothesis only.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
