# Monotonic deadline calculation

**ZIP-RUNTIME-CONTROL-TIMEOUT-001 · v1.1 · Owner** Runtime maintainers. **Maturity** D4 candidate for local deadline arithmetic.

**Planned source** `crates/runtime/src/control/timeout.rs`

## Inputs and evaluation

Use an injected monotonic clock whose live domain belongs to this instance or a trusted local clock adapter. Compare only instants in the same verified domain. Resolve request, policy and permit deadlines at their owning boundaries. At admission, convert each supplied relative execution duration once against the same trusted sample with checked addition. A missing optional request deadline contributes no bound. Policy and the current permit together must provide a finite effective bound before the launch gate can open. Preserve tighter accepted deadlines on retries of an identical operation. Validate all conversions and domain bindings before scheduling work. Overflow or invalid trusted bindings return `InvalidSpec`.

Compute the execution deadline as the minimum of the applicable request, resolved policy and permit deadlines. For grace, compute the minimum of the task deadline, applicable control deadline and stop observation instant plus resolved `runtime.stop_grace_ms`. If an applicable deadline has already passed, the grace period is exhausted immediately. Evaluate the minimum using checked remaining durations before adding grace so a large validated grace cannot overflow past a nearer finite bound. Equality with a deadline means expired. Any timer or wakeup is a hint to sample the trusted clock, with the comparison repeated at the actual launch and publication gates.

The [error contract](../error.md) owns failure precedence. A lost permit or owner triggers fencing. A valid permit with elapsed execution deadline yields `Timeout`. The first durable stop cause survives later timer events. Expiry closes body and result gates. Authorized cleanup continues under its own controls. Never derive new live authority from persisted monotonic instants, wall-clock timestamps or a checkpoint restored after process loss. Record policy revisions and the declared durations as evidence. Use the [registered budget](../../../../../contracts/resources/budget-keys.json) for stop grace and no local default.

## Acceptance

**ZIP-RUNTIME-CONTROL-TIMEOUT-T01.** In a fake clock domain start at tick 10 and supply request, policy and permit deadlines at ticks 20, 22 and 24. No timeout is produced at 19, and the execution gate closes at 20. Observe stop at 18 with grace of 5 ticks and a drain deadline of 19. Grace expires at 19. Repeat with an already exhausted grace, overflowing relative input, mismatched clock domain, absent optional request, and a wall-clock jump. Restart without fresh authority and assert no old instant grants permission. Tick values are fixtures. The execution budget is governed by ZR-004 in the [system requirements](../../../../../REQUIREMENTS.md).
