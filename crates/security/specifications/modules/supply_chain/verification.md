# Supply-chain acceptance rule

**ZIP-SECURITY-SUPPLY-CHAIN-VERIFICATION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/supply_chain/verification.rs`

## Required implementation behavior

Aggregate scoped findings, evidence identity and mandatory qualification gates. Failed and missing checks are distinct, and neither passes.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-VERIFICATION-T01.** Missing test report blocks release even when cryptographic verification passes.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
