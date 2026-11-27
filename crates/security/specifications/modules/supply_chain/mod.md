# Supply-chain verification boundary

**ZIP-SECURITY-SUPPLY-CHAIN-MOD-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/supply_chain/mod.rs`

## Required implementation behavior

Bind manifest, SBOM, artifact provenance and signatures to exact reviewed artifact; missing portion fails appropriate release check.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-MOD-T01.** A signed manifest with absent required SBOM fails the gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
