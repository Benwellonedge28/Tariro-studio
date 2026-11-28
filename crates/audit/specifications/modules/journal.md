# Ordered atomic audit append

**ZIP-AUDIT-JOURNAL-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/journal.rs`

## Boundary and inputs

Append under the same qualified metadata transaction as the privileged intent or outcome when required. Read the current workspace chain head, validate the draft, reserve the next checked sequence and bind its predecessor. Persist canonical record, new head and stable audit identity link in the same transaction. Keep a stable mapping across retry for the required replay window.

## Behavior and failure handling

Reject missing head evidence, unequal replay payloads and sequence overflow before mutation. Exact replay returns the matching existing reference without allocating another sequence. The reference returned before commit is provisional. A losing concurrent writer rereads the committed head under a fresh transaction. An ambiguous commit is reconciled by original transaction and audit identity. Publish no authoritative receipt before commit.

## Acceptance

**ZIP-AUDIT-JOURNAL-T01.** Race two appenders and inject reply loss after the first commit. Verify one contiguous chain, no duplicate sequence or identity and exact receipt replay. Force append failure and confirm the paired privileged intent aborts.
