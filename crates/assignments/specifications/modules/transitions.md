# Revision-checked transition binding

**ZIP-ASSIGNMENTS-TRANSITIONS-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/transitions.rs`

```rust
use foundation::{identity::identifier::Identifier, types::digest::Digest};
use crate::{error::AssignmentError, state::AssignmentState};

pub struct TransitionCommand {
    pub id: [u8; 16],
    pub expected_revision: u64,
    pub action: Action,
}

pub enum Action {
    Validate, Authorize { grant: Digest }, Plan { plan: Digest }, Queue,
    Start, Verify, Accept, Pause, Resume, Cancel, Revoke, Fail { evidence: Digest },
    RequireReconciliation { evidence: Digest }, FinishRecovery { evidence: Digest },
}

pub struct TransitionReceipt {
    pub id: [u8; 16],
    pub previous: AssignmentState,
    pub current: AssignmentState,
    pub revision: u64,
}

pub trait AssignmentTransitions: Send + Sync {
    fn transition(
        &self, assignment: Identifier, command: TransitionCommand,
    ) -> Result<TransitionReceipt, AssignmentError>;
}
```

The port is bound to an authenticated execution context. Command IDs are nonnil UUIDs in network byte order. Authenticate before reading an existing receipt. Bind the canonical request to assignment, actor, command ID, expected revision, action and action-specific input. Matching authorized replay returns the original receipt before checking the superseded revision. ID reuse with a changed action, payload or revision is Conflict. Replaying an accepted command issues no execution or publication authority.

Use the [numbered lifecycle table](../../../../specifications/1200-assignments/assignments.md) as the transition allowlist. Queue and Start are distinct. Start verifies live scheduler/runtime ownership, current grant and admitted resource evidence supplied by composition. The typed action contains no caller-provided proof of authorization. Accept, Revoke, RequireReconciliation and FinishRecovery verify their owning authority and exact evidence. A normal worker cannot issue a governance revocation or a recovery verdict.

Perform readiness checks outside the database transaction. At commit compare expected revision and the versions of any guard the operation depends on, and atomically write state, updated fields, receipt and event. Authorities with a separate journal must linearize the final permit with their own fencing contract. Storage's writer lock is not held across provider or runtime calls. A failure before submission leaves aggregate and outbox unchanged. After ambiguous submission reconcile by original command and transaction ID. Illegal edges and terminal transitions deny without mutation.

**ZIP-ASSIGNMENTS-TRANSITIONS-T01.** Race two commands from one revision. Exactly one commits. Replay its original ID and verify one state change and one outbox event.
