# Threat and control registry

**ZIP-SECURITY-THREAT-MODEL-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/threat_model.rs`

## Boundary and inputs

Record per-effect asset and data class, authenticated and untrusted actors, trust boundary, threat, mandatory invariant, control owner and qualification evidence. Include untrusted repository or model instructions, authority confusion, unintended disclosure, unverified artifact and interrupted-effect recovery threats from the [numbered security specification](../../../../specifications/2300-security/security.md). Bind version and affected capabilities.

## Behavior and failure handling

Use a stable ordered mapping from threats to mandatory controls. Missing, stale or unsupported required qualification blocks the affected capability. Advisory mitigations and residual risks remain explicit without changing the authorized effect boundary. Update findings when policy, adapter, threat assumptions or deployed configuration changes. A report supplies evidence only and cannot modify policy.

## Acceptance

**ZIP-SECURITY-THREAT-MODEL-T01.** Remove a required isolation or redaction control from one candidate and verify that its affected capability becomes unavailable while an independent verified capability stays eligible.
