# Resolved software inventory

**ZIP-SECURITY-SUPPLY-CHAIN-SBOM-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/supply_chain/sbom.rs`

## Boundary and inputs

Read a bounded, supported inventory artifact and bind it to the exact resolved lock, artifact digest and build scope. Normalize identities, versions, checksums, source and declared features deterministically. Include required licensing and native/unsafe exposure evidence from qualified sources, with omissions visible.

## Behavior and failure handling

Compare against the reviewed resolved graph. Reject stale digest, unrecognized mandatory format and conflated package identities. Separate an unverified declaration from observed build composition. Updating the lock or build flags invalidates affected inventory acceptance. Report missing components and dependencies without fetching or executing them.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-SBOM-T01.** Modify the lock digest after generation and verify the original inventory no longer qualifies. Supply two components with the same name but different sources and verify they remain distinct.
