# ADR-0004 · Persistent assignments

**Status** Accepted in the master design. Implementation evidence is required separately.

## Decision

Persist verified progress transactionally with revisioned state. Record external effect intent before dispatch and reconcile unknown outcomes by stable keys.

## Consequences

Durable checkpoint design adds metadata overhead and enables reliable resume. Evidence and output are stored atomically or referenced only after object staging succeeds.

## Acceptance

Kill after unit 17, restart at unit 18, and reconcile ambiguous push and PR results.

[Master design](../../ZIPPORAH-STUDIO-DESIGN.md)
