# Audit

This crate's design covers auditRecord with sequence, prev hash, hash, actor, policy digest, scope and outcome.

- [Implementation design](DESIGN.md)
- [Crate contributor instructions](AGENTS.md)
- [Verification](../../specifications/2100-verification/verification.md)
- [Security](../../specifications/2300-security/security.md)
- [Governance](../../specifications/2400-governance/governance.md)
- [Storage](../../specifications/2500-storage/storage.md)
- [Observability](../../specifications/3100-observability/observability.md)
- [Maintenance](../../specifications/3400-maintenance/maintenance.md)

Acceptance fixture: Mutate one record and detect chain failure. Verify ordering under concurrent writers.
