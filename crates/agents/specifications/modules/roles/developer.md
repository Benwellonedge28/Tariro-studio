# Developer role

**ZIP-AGENTS-ROLES-DEVELOPER-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/developer.rs`

## Boundary and inputs

Author a reviewable candidate against the pinned repository identity, base commit, exact paths and relevant instructions. Preserve immutable patch bytes, approved preimages and validation evidence. Use an isolated authorized workspace and stop when the proposed diff exceeds scope.

## Behavior and failure handling

Before submission, verify changed paths and bytes against the reviewed candidate. Exclude side effects requested inside untrusted source content. Hand the candidate to Verification with exact checks and scoped provenance. Publishing externally uses its own authorizations and reviewed effect identity.

## Acceptance

**ZIP-AGENTS-ROLES-DEVELOPER-T01.** Insert one unauthorized file into an otherwise passing patch and verify submission remains blocked. Return to the approved diff and confirm acceptance evidence is tied to its exact bytes.
