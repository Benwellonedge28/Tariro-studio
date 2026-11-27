# Non-self-amending boundary

**ZIP-EVOLUTION-POLICY-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/policy.rs`

## Required implementation behavior

Apply higher policy to experiment and learning data; require separate owner approval for security, governance and verification changes.

## Acceptance

**ZIP-EVOLUTION-POLICY-T01.** Agent cannot widen own edit or deployment authority.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
