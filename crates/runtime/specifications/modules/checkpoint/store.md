# Atomic checkpoint publication

**ZIP-RUNTIME-CHECKPOINT-STORE-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/checkpoint/store.rs`

## Boundary and inputs

Accept a trusted execution context and immutable checkpoint candidate from [checkpoint](checkpoint.md). Read the exact attempt and expected journal revision. Resolve authorization first. An authorized exact replay of an accepted sequence and candidate returns its receipt before new worker-gate checks. A different candidate for the same sequence returns Conflict. For a new commit recheck owner generation, live lease, deadline, stop and publishing scope, then require the next contiguous sequence with the recorded predecessor.

## Behavior and failure handling

Stage and verify bytes before the write transaction. In one expected-revision transaction append the record, advance the attempt's checkpoint cursor, record its receipt and commit one checkpoint outbox entry. On concurrent stop or ownership change the guarded commit fails. After ambiguous commit use the same attempt and sequence to inspect the receipt before retry. Release bounded staging through Storage ownership rules. Staging cleanup never deletes a referenced object. Return OutcomeUnknown until the owning journal can settle ambiguity.

## Acceptance

**ZIP-RUNTIME-CHECKPOINT-STORE-T01.** Use RT-LIFE-04 and RT-LIFE-05 in the [lifecycle fixtures](../../../../../contracts/acceptance/runtime/lifecycle-fixtures.json). Crash on both sides of commit and lose a reply after success. The observed cursor and event count reflect the transaction. Race a second commit with stop and with a different checkpoint for the same sequence.
