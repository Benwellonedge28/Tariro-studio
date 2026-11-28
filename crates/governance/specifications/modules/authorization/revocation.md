# Durable scope fencing

**ZIP-GOVERNANCE-AUTHORIZATION-REVOCATION-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/authorization/revocation.rs`

## Boundary and inputs

Accept a scoped authenticated revoke command with exact identity, expected active epoch and a bounded reason. Verify caller authority before disclosing grants. Increment the scope epoch with checked arithmetic and atomically record revocation and outbox intent. Keep the committed revision authoritative after restart and treat repeated identical commands as receipt replay.

## Behavior and failure handling

Serially compare protected effect claims with the current epoch in their owning transaction. Claim attempts that observe a newer epoch deny before dispatch. If a prior claim may have crossed the effect boundary, preserve its intent for read-only reconciliation and independently authorized cleanup. Runtime and Resources retain ownership of leases. Do not credit a hold or erase committed receipts on revoke. Fence descendants through live lineage checks.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-REVOCATION-T01.** Race revoke and claim in both orders, lose the revoke acknowledgement and restart. Verify exact replay returns the prior revocation receipt, old grants remain fenced, and existing effect receipts stay visible to authorized readers.
