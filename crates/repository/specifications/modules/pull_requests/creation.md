# Guarded draft pull request creation

**ZIP-REPOSITORY-PULL-REQUESTS-CREATION-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/pull_requests/creation.rs`

Bind the stable repository ID, exact base and head branch refs and expected commit IDs, reviewed manifest and instruction seals, approved title and body digest, requested draft flag and stable effect key. Use an adapter-controlled deterministic marker derived from the already authorized effect identity. The marker is public correlation data and carries no credentials. Use the same approved marker on matching retries. Reject ambiguous or duplicate marker representations in user content. Require a verified branch receipt and recheck the current grant and both heads before provider dispatch.

Use conditional creation when the qualified provider can bind expected commits atomically. If it cannot, policy must explicitly authorize the read-before and verify-after model. If atomic accuracy is required by the grant, deny unsupported providers before the call. With the non-atomic model, a discovered base or head change after dispatch is a recorded effect mismatch. Preserve the created PR identity and stop subsequent publication actions. A changing head does not grant scope to edit, close or recreate the PR.

Persist the durable effect claim before sending. Confirm provider PR ID, immutable repository, branch refs, expected commits, draft status, marker and scoped content against the request. A title match is insufficient. If the provider cannot establish those required observations, report uncertainty or mismatch and reconcile. A possible dispatch timeout never triggers an immediate second create.

**ZIP-REPOSITORY-PULL-REQUESTS-CREATION-T01.** Simulate a lost reply and recover the one existing matching PR. Simulate a ref move after an allowed non-atomic create and verify the created PR remains visible as mismatched evidence.
