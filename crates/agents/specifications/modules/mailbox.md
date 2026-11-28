# Admitted mailbox queue

**ZIP-AGENTS-MAILBOX-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/mailbox.rs`

## Boundary and inputs

Accept scoped immutable messages with sender identity, per-sender order, semantic digest and grant context. Track a durable bounded queue and receipt cursor per agent. Enforce effective item count and byte budget before staging growth. Keep the per-sender order promised by the approved delivery contract. Use stable tie ordering when selecting messages that are concurrently available.

## Behavior and failure handling

Check authorization before lookup, then replay or conflict, then intake and count. Commit first insertion, count and receipt together. An exact replay consumes no slot. Return typed backpressure on exhaustion without moving the cursor. Remove or acknowledge items only after the owning authorized transition. A dropped receiver leaves the last committed state available after restart. Revocation prevents delivery to an unauthorized agent.

## Acceptance

**ZIP-AGENTS-MAILBOX-T01.** Race two writers for the last item and then replay the winner with a lost reply. Verify one admitted message and stable receipt. Try a mismatched payload under the same sender sequence. Verify conflict and unchanged count.
