# Resolved software inventory

**ZIP-SECURITY-SUPPLY-CHAIN-SBOM-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/supply_chain/sbom.rs`

## Required implementation behavior

Validate normalized manifest resolves exact dependency version, checksum, license/feature metadata and artifact provenance. Record omissions as findings.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-SBOM-T01.** A lockfile changed after SBOM generation invalidates the gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
