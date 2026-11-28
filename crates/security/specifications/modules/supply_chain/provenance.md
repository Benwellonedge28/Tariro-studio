# Reproducible build claim

**ZIP-SECURITY-SUPPLY-CHAIN-PROVENANCE-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/supply_chain/provenance.rs`

## Boundary and inputs

Verify build evidence linking source revision, builder identity and configuration, toolchain and dependency lock digests, declared recipe and exact output digest. Verify the trusted attestation and compare its fields to independently expected build inputs. [SLSA artifact verification](https://slsa.dev/spec/v1.2/verifying-artifacts)

## Behavior and failure handling

Treat a trustworthy build assertion and an independently reproduced build as distinct observations. A reproducibility verdict requires the approved independent build evidence and output comparison. Reject changed output or unsupported attestation edition. Preserve actual results, caveats and the pinned evidence source in the scoped report.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-PROVENANCE-T01.** Replace artifact bytes or claimed builder identity in an otherwise matching evidence set. Both must fail. Provide a qualified attestation with no rebuild report and verify no reproducibility claim is issued.
