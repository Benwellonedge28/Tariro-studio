# Approved draft publication

**ZIP-DOCUMENTATION-PUBLISHING-001 · v1.1 candidate · Owner** Documentation maintainers

**Planned source** `crates/documentation/src/publishing.rs`

Submit a complete documentation seal to the Assignments workflow. Re-read current scope, source and expected head, then check exact staged tree, current approval and verifier evidence. No push may start from partial work. Repository adapters own commits and remote effects. Use distinct durable push and draft-PR intents and the original stable identities. Never dispatch PR creation before the matching branch update is confirmed. A stale base or unsafe provider capability blocks the effect under the [publication contract](../../../../specifications/1400-repositories/repositories.md).

After response loss, use read-only reconciliation. A matching provider receipt must bind stable repository, expected base/head and commit, exact effect marker and requested draft state. A mismatch or unsettled effect blocks repeat mutation. Record provider observations and required check results on the actual published head. Do not imply PR approval, merge or completed release from a draft. A draft is a distinct authorized deliverable, and later effects require their own scope.

**ZIP-DOCUMENTATION-PUBLISHING-T01.** A changed base blocks push. Lost draft-PR response recovers the existing matching draft and emits no second create.
