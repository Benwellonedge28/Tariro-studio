# Restart and external-effect reconciliation

**ZIP-ASG-RCV-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/recovery.rs`

Recovery identifies the assignment, expected revision, valid recovery principal and pinned plan. Composition supplies bounded read-only provider inspection, trusted cleanup evidence, storage and authorization. Recovery itself issues no publication call.

1. Read and validate one committed aggregate snapshot. Return terminal evidence to an authorized reader. For nonterminal active work, fence its worker epoch in a revision-checked commit. Preserve pending stop disposition, old lease and all observed effects.
2. Determine prior runtime teardown and resource settlement under scoped cleanup authority. Verify the committed unit prefix, referenced artifacts and evidence. Gaps, corrupt bytes or conflicting digests block. Continue required reconciliation even if execution authority expired.
3. Inspect each claimed or ambiguous provider effect against the [repository boundaries](../../../../specifications/1400-repositories/repositories.md). Return Completed for exact matching verified evidence. Return Conflict for incompatible remote state or more than one matching PR. Return Absent only when the read is authoritative for the original identity and the old dispatch can no longer complete. A delayed search result, missing response or local receipt lost after restore is insufficient. Keep unresolved effects blocked.
4. Record the recovery result with CAS and outbox. With a pending stop, select its terminal or paused destination only after cleanup and all effects settle. With live execution authority, recover to Scheduled for remaining units or Verifying for a verified candidate needing publication or acceptance. No recovery verdict issues a live lease.
5. An authorized dispatch can retry an effect proven Absent using the same identity, exact reviewed bytes and original preconditions, after revalidating live authority. Never automatically recreate the intent with new markers. For a PR provider that cannot rule out a delayed prior creation or prove absence, require further reconciliation.

A provider effect has phases Prepared, Claimed, Unknown, Confirmed, Absent or Conflict. Prepared is an intent with no prior dispatch authority. Claimed commits a one-use admission decision before dispatch. A lost claimant or reply requires read-only reconciliation. Verified matching evidence transitions to Confirmed, authoritative no longer in-flight absence to Absent, incompatible evidence to Conflict, and all other uncertainty to Unknown. Only a live, exact identity retry from Absent may claim again. Confirmed and Conflict never reopen dispatch under the same key.

A provider effect freezes immutable repository ID, operation kind, reviewed candidate digest, expected and intended remote refs, and effect key. A push receipt binds the intended commit to the authorized branch. A PR receipt binds repository, base, head and effect marker. Use separate effect keys for push and PR creation. A recorded push is a prerequisite for PR creation. Claim dispatch with live [authorization](authorization.md) and checkpoint the intent before invoking the effect adapter. Local journal cancellation does not retract a committed external effect.

**ASG-RCV-T01.** Resume at unit 18. **ASG-RCV-T02.** Lose push and PR replies, recover existing matching receipts and verify no duplicate invocation. **ASG-RCV-T03.** Expired or revoked grants stop execution while cleanup can reconcile. **ASG-RCV-T04.** Unverifiable or conflicting evidence blocks the affected operation.
