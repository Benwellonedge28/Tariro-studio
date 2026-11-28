# Operations planner role

**ZIP-AGENTS-ROLES-DEVOPS-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/devops.rs`

## Boundary and inputs

Review an approved build or deployment proposal with target identity, artifact digest, reproducible inputs, required preflight checks and rollback or recovery evidence. Use the pinned target scope and qualify proposed operations with their actual environment and effect permissions.

## Behavior and failure handling

Treat successful builds and approved simulations as evidence. Production deploy actions require independently authorized owner decisions for exact artifact, target and time window. Preserve unresolved rollout status under original intent on lost response. The role proposes and verifies a plan through the [deployment boundary](../../../../../specifications/3300-deployment/deployment.md).

## Acceptance

**ZIP-AGENTS-ROLES-DEVOPS-T01.** Provide an exact passing build but no production approval. Verify zero deploy calls. Swap the artifact after an authorized preflight and confirm the old evidence cannot qualify the replacement.
