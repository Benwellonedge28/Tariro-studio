# Assignment acceptance and completion

**ZIP-ASSIGNMENTS-ACCEPTANCE-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/acceptance.rs`

Evaluate prepublication checks while Verifying. Verify complete required units, approved effective policy, exact sealed candidate and all required prepublication evidence. Only an authorized effect adapter may claim publication after that gate. Treat delivery of a refresh notification as distinct from evidence. If the plan calls for no publication, completion requires its documented local outcome evidence.

Before Accept, bind the requested assignment revision to the active plan, sealed candidate, typed verdicts and all required effect receipts. A PR receipt verifies repository, base, head and marker and records whether draft was requested. Required downstream checks must reference the exact published commit. Each mandatory check must return a verified passing observation. Missing, stopped, unavailable or failed mandatory checks block completion. No effects or worker cleanup may remain unresolved. Compare the accepted digests and current authorization in the commit guard. Emit one terminal receipt and outbox event.

**ZIP-ASSIGNMENTS-ACCEPTANCE-T01.** After reviewing one tree, change a file and verify its stale evidence cannot enable publication or Complete. Verify a matching PR receipt with checks for a different commit still cannot complete the assignment.
