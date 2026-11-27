# Reproducible build claim

**ZIP-SECURITY-SUPPLY-CHAIN-PROVENANCE-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/supply_chain/provenance.rs`

## Required implementation behavior

Pin source, builder/toolchain, dependency lock, recipe and output digest. Verify asserted source against actual evidence.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-PROVENANCE-T01.** Artifact with altered digest cannot inherit the original build claim.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
