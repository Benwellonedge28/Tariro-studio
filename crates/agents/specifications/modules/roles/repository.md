# Repository role

**ZIP-AGENTS-ROLES-REPOSITORY-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/repository.rs`

## Boundary and inputs

Inspect a pinned repository snapshot and authorized refs using the [repository contract](../../../../../specifications/1400-repositories/repositories.md). Produce a scoped proposal binding current head, base, exact diff, instructions and ownership. Keep artifact and branch identity stable through the review.

## Behavior and failure handling

Apply remote effects only through the repository owner's conditional or otherwise approved effect boundary. Recheck exact refs before mutation, preserve the candidate on head drift, and reconcile an unknown reply using the original intent. No role selection conveys force-push, merge, release or access to another repository.

## Acceptance

**ZIP-AGENTS-ROLES-REPOSITORY-T01.** Change the remote ref after the plan is sealed. Verify a conflict and no overwrite. Lose an authorized synthetic response and verify reconciliation cannot issue the same mutation again blindly.
