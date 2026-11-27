# Validated agent construction

**ZIP-AGENTS-FACTORY-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/factory.rs`

## Required implementation behavior

Resolve reviewed manifest, identity, model compatibility and qualified adapters, leaving effectful controls unavailable if unmet. Do not start before admission.

## Acceptance

**ZIP-AGENTS-FACTORY-T01.** Unsupported model returns a diagnostic without spawning workers.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
