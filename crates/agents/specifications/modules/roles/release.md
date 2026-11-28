# Release reviewer role

**ZIP-AGENTS-ROLES-RELEASE-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/release.rs`

## Boundary and inputs

Compare the exact release manifest, signed artifacts and verified qualification receipts under the [release standard](../../../../../RELEASE_STANDARD.md). Bind the verdict to commit, artifact digests, policy revision and target channel. Make outstanding gates and unsupported targets explicit.

## Behavior and failure handling

A passing release review provides evidence only for its exact candidate. Promote requires separately authorized owner effect and applies after rechecking live prerequisites and target state. A changed digest, expired approval or missing required check blocks promotion. Keep existing published effects available for reconciliation.

## Acceptance

**ZIP-AGENTS-ROLES-RELEASE-T01.** Replace a verified artifact with another digest while retaining the original review. Verify promotion stays blocked. Reconcile a synthetic matching existing release without dispatching a second effect.
