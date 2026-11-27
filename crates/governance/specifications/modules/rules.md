# Rule normalization and conflict detection

**ZIP-GOVERNANCE-RULES-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/rules.rs`

## Required implementation behavior

Normalize canonical paths, identities, effects and destinations. Reject ambiguities and contradictions at publication; explicit mandatory denial wins at evaluation.

## Acceptance

**ZIP-GOVERNANCE-RULES-T01.** Two aliases of same scope resolve consistently without widening.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
