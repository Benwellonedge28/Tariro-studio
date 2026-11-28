# Agent principal representation

**ZIP-IDENTITY-AGENT-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/agent.rs`

## Boundary and inputs

Represent an agent as a distinct typed principal linked to one workspace, assignment, reviewed role manifest and authorized owner lineage. Store its identity generation and enrollment provenance. A shared inference model, agent display name or requested role supplies no identity evidence.

## Behavior and failure handling

Resolve the binding only while both the exact assignment and owner lineage remain current. Agent credential verification and scope attenuation belong to their owning policies. Retiring an agent fences previous generations and preserves historical provenance. A new assignment requires a separate bound identity even if the manifest is reused.

## Acceptance

**ZIP-IDENTITY-AGENT-T01.** Enroll two agents using the same synthetic model in different workspaces. Attempt to resolve the first against the second assignment. Verify rejection before private scope is disclosed and preserve distinct history.
