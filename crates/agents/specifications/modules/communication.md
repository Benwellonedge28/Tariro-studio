# Scoped agent message routing

**ZIP-AGENTS-COMMUNICATION-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/communication.rs`

## Boundary and inputs

Accept a versioned envelope binding sender, intended recipient, workspace, assignment, task, stable message identity, audience and classified payload reference. Authenticate sender and recipient scope before routing. Preserve payload as untrusted proposal or evidence data. Authority comes exclusively from the owning policy interface.

## Behavior and failure handling

Enforce the resolved deadline and bounded message bytes before storage or transfer. Route only through [mailbox](mailbox.md) or a separately authorized transport. An exact replay preserves the receipt and count. An invalid audience, changed content or expired request produces a scoped typed error without payload disclosure. Delivery confirmation is independent of downstream execution.

## Acceptance

**ZIP-AGENTS-COMMUNICATION-T01.** Deliver text asserting owner approval to an otherwise permitted mailbox and verify the recipient cannot claim an effect with it. Drop an accepted delivery reply and verify exact replay creates no duplicate.
