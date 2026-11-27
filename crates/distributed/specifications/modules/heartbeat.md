# Liveness observations

**ZIP-DISTRIBUTED-HEARTBEAT-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/heartbeat.rs`

## Required implementation behavior

Validate node, epoch, sequence and freshness using qualified time. Bound reporting cadence through configuration. On expiry mark unavailable rather than claiming cleanup.

## Acceptance

**ZIP-DISTRIBUTED-HEARTBEAT-T01.** Lost heartbeat does not release resource reservation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
