# Typed errors and recovery

**ZIP-ERR-001 · v1.0 · Owner:** Foundation and interface maintainers. **Maturity:** D4 candidate.

Give each component an enum for the failures its callers can act on. Public boundaries expose stable codes, correlation ID, retryability and safe details. Map upstream errors at adapter boundaries. Preserve typed source or redacted diagnostics locally under access control. Never use a display string as the retry signal.

| Class | Caller action |
| --- | --- |
| Invalid input / unsupported format | Correct request or negotiate capability |
| Denied / revoked / expired | Stop new effects and obtain authority if appropriate |
| Stale revision / conflict | Re-read and replan under current state |
| Exhausted / pressure | Apply approved backpressure or lower demand |
| Transient transport | Retry only under remaining budget and a safe idempotent boundary |
| Unknown effect outcome | Reconcile against the authoritative service before trying again |
| Corruption | Isolate the affected state and recover from verified evidence |
| Cancellation | Report where execution stopped and any committed outcome |

Define input-validation and error precedence per operation. Check remote authorization before returning details that would reveal concealed resources. Verify stable codes and redaction with golden fixtures and test ambiguous I/O separately from definitive failure.
