# Owned process lifecycle

**ZIP-TERMINAL-PROCESS-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/process.rs`

## Boundary and inputs

Represent one opaque scoped process handle tied to the scheduler and runtime attempt, approved containment locator and owner generation. Construct only from trusted launch observation. Handle observation and stopping require live caller scope even when a process identifier is known.

## Behavior and failure handling

Record bounded exit and process-tree state through the qualified supervisor. Keep ownership provisional when launch or lookup cannot be proved. A process handle is never reusable for another attempt, and dropping it releases only observation state. Cleanup ownership remains durable until settlement.

## Acceptance

**ZIP-TERMINAL-PROCESS-T01.** Attempt cancel using an unbound process identity and a stale handle. Both deny. An authorized handle can request stop but cannot declare the group reaped independently.
