# Pause at a durable boundary

**ZIP-RUNTIME-CONTROL-PAUSE-001 · v1.1 · Owner** Runtime maintainers. **Maturity** D4 candidate for local pause.

**Planned source** `crates/runtime/src/control/pause.rs`

## Control and state

Pause is a reversible intake gate scoped to the authorized task or assignment. It does not transition the installation out of Running. At composition, the assignment or scheduler owner first durably closes its corresponding claim gate, then requests the runtime pause. The runtime serializes closure with registration and the supervisor's final launch gate. The controlling owner retains the scoped gate after restart. A restored runtime checks that gate before admitting work.

The pause request identifies the scope, command identity, controlling revision and effective monotonic deadline. Check authorization before disclosing progress. Exact authorized replay returns the current observation for that operation. A changed request under the same identity returns `Conflict`. The runtime reports Pending while admitted work remains active, Paused when a verified boundary is durable and all associated work is settled, and Blocked when the pause deadline expires with outstanding work or a required proof is unavailable. An authorized observation may report Paused after later reconciliation establishes the boundary. Paused may represent the original boundary if no new checkpoint committed.

## Execution and resumption

A body already past the launch gate may reach its next valid checkpoint within its live authority and effective deadline. No pause extends a lease or introduces new permission. After that checkpoint, request cooperative stop and verify teardown, resource release and external effect settlement. At the pause deadline fence the worker and continue authorized cleanup. Report the highest contiguous verified checkpoint from the [checkpoint store](../checkpoint/store.md), even when cleanup prevents returning Paused. Uncertain effects or unreaped work keep the gate closed.

Resume requires a new authorized command, current controlling revision, no unresolved obligations in scope and an installation that accepts intake. It releases the scoped gate under the controlling owner's compare-and-swap and permits fresh eligible claims. Compute the first unfinished unit from the verified boundary, or return the settled outcome if the plan is complete. A successor starts at that unfinished unit with a fresh attempt identity and resource admission. Installation shutdown prevails over reopening a scoped gate. A lost response requires rereading the controlling operation before repeating it.

## Acceptance

**ZIP-RUNTIME-CONTROL-PAUSE-T01.** Pause after the checkpoint commit and before the next claim. Restart and verify the gate stays closed, then resume under fresh authority and execute only the next unit. Pause before the checkpoint commit and kill the worker. Verify staged bytes cannot advance progress. With an unresolved effect or missing teardown proof, return Blocked and reject resume. Link the checkpoint interruption to RT-LIFE-04 in the [lifecycle fixtures](../../../../../contracts/acceptance/runtime/lifecycle-fixtures.json).
