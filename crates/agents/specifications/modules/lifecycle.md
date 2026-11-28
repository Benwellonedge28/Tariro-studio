# Agent activation and shutdown

**ZIP-AGENTS-LIFECYCLE-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/lifecycle.rs`

## Boundary and inputs

Use the durable Registered, Ready, Busy, Suspended, Draining and Stopped states from the [numbered agent contract](../../../../specifications/1000-agents/agents.md). A constructed but unregistered instance has no durable state. Failures are typed denials or recorded dispositions under the owning transition, without a second set of lifecycle names. Check expected revision and current authority at each reported transition.

## Behavior and failure handling

Registered becomes Ready after validated composition. Ready becomes Busy only after a bound runtime submission is confirmed. Busy returns Ready after confirmed settlement. Ready may suspend immediately. Busy may suspend only at a verified settled boundary under the controlling policy. An authorized resume from Suspended requires fresh checks. Stop or revocation closes intake and moves a nonterminal instance to Draining. Draining becomes Stopped after in-flight submission, effects and cleanup settle. Deny all other edges and replay exact accepted commands without another transition.

## Acceptance

**ZIP-AGENTS-LIFECYCLE-T01.** Race dispatch with stop, revoke a Busy agent, and restore during Draining. Verify no new execution starts, committed evidence survives, and stop is reported only after verified settlement.
