# Orchestration failure classes

**ZIP-ORCHESTRATION-ERROR-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/error.rs`

## Boundary and inputs

Expose stable non-exhaustive error codes InvalidGraph, ConflictUnresolved and NoEligibleAgent from the crate boundary. Include BudgetExhausted, PolicyDenied, StaleOutcome, OutcomeUnknown and EscalationRequired for the corresponding typed failure. Carry only redacted source class and authorized evidence references in public diagnostics. Downstream messages and task payloads are excluded.

## Behavior and failure handling

Check shape and authorization before graph membership, then expected revision and effect identity, then resource or evidence eligibility. Definite precommit failure preserves the previous graph. OutcomeUnknown keeps the original intent unsettled. ConflictUnresolved and EscalationRequired prevent completion and do not substitute for the owning authorization. StaleOutcome allows current recovery to inspect evidence, without giving the old worker current settlement authority. Reuse only bounded retries defined by the owning boundary.

## Acceptance

**ZIP-ORCHESTRATION-ERROR-T01.** Inject an ambiguous orchestration submission with a stale and a conflicting completion. Preserve the original intent, report typed outcomes and verify no completion or new effect was inferred. Inject private synthetic strings and verify redaction.
