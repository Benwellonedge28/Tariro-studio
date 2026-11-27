# Reasoning provenance and claim linkage

**ZIP-REASONING-EVIDENCE-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/evidence.rs`

## Required implementation behavior

Pin claim, evidence reference, source revision and confidence/type. Validate references independently and preserve unknowns.

## Acceptance

**ZIP-REASONING-EVIDENCE-T01.** A claim with missing evidence cannot pass acceptance.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
