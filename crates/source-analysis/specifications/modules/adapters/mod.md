# Qualified language adapter registry

**ZIP-SOURCE-ANALYSIS-ADAPTERS-MOD-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/mod.rs`

## Required implementation behavior

Resolve language and requested analysis capabilities to approved parser/server. Optional adapters cannot override scope or budget.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-MOD-T01.** Missing analyzer falls back to explicitly text-only behavior.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
