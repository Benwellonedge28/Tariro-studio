# Finite agent admission

**ZIP-AGENTS-LIMITS-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/limits.rs`

## Required implementation behavior

Use resolved mailbox/delegation keys, attempt deadlines, quotas and measured resource lease. Do not add local fixed ceilings.

## Acceptance

**ZIP-AGENTS-LIMITS-T01.** Same build enforces two configured mailbox bounds.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
