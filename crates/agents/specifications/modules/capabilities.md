# Agent capability intersection

**ZIP-AGENTS-CAPABILITIES-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/capabilities.rs`

## Required implementation behavior

Intersect declared capabilities with current grant, task scope and qualified runtime adapters. Preserve unsupported and denied as explicit outcomes.

## Acceptance

**ZIP-AGENTS-CAPABILITIES-T01.** Agent with read capability cannot select a publish adapter.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
