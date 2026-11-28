# Dependency policy evidence

**ZIP-SECURITY-DEFENSES-DEPENDENCY-RISK-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/defenses/dependency_risk.rs`

## Boundary and inputs

Read the pinned resolved dependency graph, exact package identities and checksums, enabled features, provenance, license evidence, native and unsafe exposure, and approved exception records. Assess against the reviewed dependency policy and frozen advisory evidence. Distinguish unavailable evidence from a clean finding.

## Behavior and failure handling

Compare by resolved identity and source rather than package display name. Apply exact approved exception scope and expiry, and bind each finding to the reviewed graph digest. Changes to resolution invalidate affected results. This evaluator neither fetches new dependencies nor activates or installs unreviewed packages.

## Acceptance

**ZIP-SECURITY-DEFENSES-DEPENDENCY-RISK-T01.** Replace a reviewed dependency with one of the same display name and different checksum or source. Verify the previous qualification fails. Report stale advisory evidence as unavailable rather than passing.
