# Versioned rule registry

**ZIP-REASONING-SYMBOLIC-RULES-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/symbolic/rules.rs`

## Required implementation behavior

Validate domain, predicates, authority and deterministic priority. Keep conflicting rules explicit and pin revision.

## Acceptance

**ZIP-REASONING-SYMBOLIC-RULES-T01.** Cycle/conflict cannot quietly select arbitrary rule.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
