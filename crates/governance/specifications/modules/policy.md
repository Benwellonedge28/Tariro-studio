# Versioned policy representation

**ZIP-GOVERNANCE-POLICY-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/policy.rs`

## Boundary and inputs

Represent a versioned immutable candidate with trusted issuer, revision, compatibility edition, canonical scope, normalized allow and deny rules, ceilings, obligations and repository or workspace bindings. Compute a digest only over its validated canonical representation. Keep credential material external.

## Behavior and failure handling

Validate issuer authority, supported edition, rule shape and mandatory compatibility against the active constitution. Reject same-revision different bytes and stale replacement. Publish policy plus evidence under the owning CAS so readers see one complete generation. Invalid input leaves the existing generation in force and new effects still consult live revocation.

## Acceptance

**ZIP-GOVERNANCE-POLICY-T01.** Try to replace a valid policy with malformed, stale and same-revision conflicting candidates. All fail without publication. Permute equivalent rule input and verify a stable canonical digest.
