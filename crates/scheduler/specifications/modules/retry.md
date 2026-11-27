# Bounded retry decision

**ZIP-SCHEDULER-RETRY-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/retry.rs`

Retry only after recording the previous attempt's trusted result, confirming occupancy release and reconciling every possibly committed effect. A transient outcome is retryable only when the effect ledger proves no effect, acknowledged compensation or an approved replay of the same immutable effect identity. Unknown, authorization denied, cancelled and permanent failures cannot schedule a retry. Live authority and deadline are checked again at claim and at runtime launch.

Intersect the resolved `scheduler.max_attempts` with assignment policy. Charge one dispatch attempt in the transaction that transitions Reserving to Dispatched, before external handoff. A restart or replay never resets that count. A predispatch capacity defer does not decrement dispatch allowance. It still gets a unique attempt number and remains bounded by the original job lifetime and resource wake rules.

The resolved retry policy supplies a base wait and any backoff cap. `scheduler.retry_jitter_ms` gives the maximum additional delay. A zero jitter setting adds zero. For a positive bound, request a uniform integer from the injected randomness source over the inclusive bounded interval. Add with checked arithmetic and persist the selected wait before returning RetryWait. An overflow or a wake at or after the job deadline ends retry eligibility. Never draw again when replaying an accepted decision. Record failure class, effect evidence, effective policy and dispatch count.

**ZIP-SCHEDULER-RETRY-T01.** A lost effect acknowledgement produces no retry while uncertain. Reconcile it, apply the original deadline and cap, then verify a persisted retry decision replays with the same selected jitter.
