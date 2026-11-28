# Agent actor binding

**ZIP-AGENTS-IDENTITY-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/identity.rs`

## Boundary and inputs

Represent an AgentId as a typed scoped identity bound to workspace, assignment, principal and verified principal epoch. The owning identity authority verifies origin and delegation lineage through composition. A name, claimed role, model ID or provider credential alone conveys no agent principal or authority.

## Behavior and failure handling

Before returning a binding, require current verified membership and authorized audience. Match the full binding on dispatch, delegation and result evidence. Revocation or retirement prevents new privileged work under the old epoch. Preserve historical evidence by full identity without making old identities reusable. Expose read-only identifiers within permitted scopes and keep credentials opaque.

## Acceptance

**ZIP-AGENTS-IDENTITY-T01.** Submit two same-name agents with separate assignments and a forged privileged role. Verify no cross-assignment match or role elevation. Retire one and attempt replay using its previous epoch.
