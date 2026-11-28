# Filesystem intent reconciliation

**ZIP-FILESYSTEM-RECOVERY-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/recovery.rs`

## Boundary and inputs

Load a bounded scoped original write intent with preimage binding, new immutable digest, private stage identity and relevant owner receipts. Read current target through the qualified root and compare with expected effect evidence. Scope read-only recovery and cleanup separately from future writes.

## Behavior and failure handling

Classify exact settled match, definitive nonapplication with unchanged preconditions, conflict, and unknown. A matching digest alone does not prove the original command where other writers could produce it. Verify owning evidence before claiming success. Permit retry only on qualified nonapplication, live authority and unchanged preimage. Never delete uncertain staging evidence.

## Acceptance

**ZIP-FILESYSTEM-RECOVERY-T01.** Lose a rename acknowledgement. Use a matching trusted observation, a changed third-party target and unavailable scope in separate runs. Only the trusted match settles success, and the latter two remain blocked without repeating the mutation.
