# Durable human decision request

**ZIP-ORCHESTRATION-ESCALATION-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/escalation.rs`

## Boundary and inputs

Persist a scoped decision request through Assignments with the pinned candidate and expected revision, evidence references, bounded question, required approval authority and expiry. Bind the request to a stable identity and exact digest. A pending request blocks dependent work and any new effect requiring that decision. Unrelated eligible work retains its normal protections.

## Behavior and failure handling

Accept a response only if authenticated, live, in scope and bound to the same request and candidate. Apply using the assignment's revision-checked decision path. Return the stored result for the exact authorized replay. Conflicting or expired answers cannot unblock work. A changed candidate needs a new request even if the display text is unchanged. Avoid exposing private evidence through notification payloads.

## Acceptance

**ZIP-ORCHESTRATION-ESCALATION-T01.** Record a decision request, replace the candidate and deliver a late approval for the original. Verify rejection. Replay a properly accepted response and confirm only one unblock transition.
