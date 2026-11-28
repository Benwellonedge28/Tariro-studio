# Windows process and path containment

**ZIP-SANDBOX-BACKENDS-WINDOWS-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/backends/windows.rs`

## Boundary and inputs

Qualify process-group containment, filesystem identity and deterministic restart inspection for the exact Windows adapter and environment. Verify path-root scope using enrolled filesystem handles and the approved resolution semantics for redirected or linked objects. Return unavailable for unsupported mandatory observations.

## Behavior and failure handling

Open the execution gate only after verified restrictors and exact process ownership are installed. A path string or individual process identifier is insufficient proof. Verify all descendants terminate and mandatory usage settles before issuing trusted teardown evidence. A conflicting or missing observation holds the obligation.

## Acceptance

**ZIP-SANDBOX-BACKENDS-WINDOWS-T01.** Use a synthetic permitted root and an unapproved linked target. Deny the latter without touching it. Run an approved child-tree fixture and require whole-group exit evidence before advertising qualified cleanup.
