# Audit failure classes

**ZIP-AUDIT-ERROR-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/error.rs`

## Boundary and inputs

Expose stable AuditUnavailable, InvalidRecord, ChainMismatch, RetentionConflict, ForbiddenExport, CursorExpired and OutcomeUnknown decisions. Normalize storage, integrity and adapter failure at the owning boundary. Expose only safe codes and scoped evidence to authorized callers. Do not include raw payloads, paths, credentials or other tenant counts.

## Behavior and failure handling

AuditUnavailable is a known failure before the storage boundary commits. When mandatory audit fails, roll back the associated privileged intent and return no executable result. OutcomeUnknown preserves exact transaction identity for reconciliation and must not be retried as a fresh append. Distinguish an authorized expired cursor from a forbidden query before disclosing any stream state.

## Acceptance

**ZIP-AUDIT-ERROR-T01.** Fail redaction, mandatory append and commit acknowledgement in separate runs. Confirm no privileged effect starts from a failed append and an ambiguous commit is resolved by the original transaction without duplicate records.
