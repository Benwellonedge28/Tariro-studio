# Permission decision composition

**ZIP-SECURITY-PERMISSIONS-MOD-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/permissions/mod.rs`

## Boundary and inputs

Compose [role](rbac.md), [attribute](abac.md), [capability](capability.md), [inheritance](inheritance.md) and [revocation](revocation.md) evidence for one exact authorization decision. Each evaluator returns scoped typed facts, not authority. The coordinator consumes one coherent snapshot with application-owned normalization evidence.

## Behavior and failure handling

Apply mandatory and explicit denies first, then require all applicable positive conditions and effect-specific approvals. Inconsistent or unsupported mandatory facts deny. Sort reason evidence under stable ordering and redact it for the caller. Only the [authoritative decision boundary](../authorization.md) can report an allowed proposal, and only the owning guarded claim can start an effect.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-MOD-T01.** Invoke each evaluator separately under an otherwise valid test policy and confirm no runnable authorization is produced. Combine an applicable deny with broad role eligibility and verify a stable denial.
