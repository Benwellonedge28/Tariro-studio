# Invariant declaration

**ZIP-VERIFICATION-FORMAL-INVARIANTS-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/formal/invariants.rs`

## Required implementation behavior

Require stable ID, reachable-state predicate and scope. Counterexamples reference checked model digest, fixture and actual observed trace.

## Acceptance

**ZIP-VERIFICATION-FORMAL-INVARIANTS-T01.** Proof over a different invariant revision cannot qualify current candidate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
