# Governance facade

**ZIP-GOVERNANCE-LIB-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/lib.rs`

## Boundary and inputs

Declare the [Governance modules](../../DESIGN.md) with unsafe first-party code forbidden. Expose typed policy snapshots, decision results and scoped issuing, oversight and effect-guard commands. Keep raw epoch mutators, durable intent constructors and decision attestation internals private.

## Behavior and failure handling

Compose the approved Foundation, Identity, Security, Storage and Events dependencies. An audit adapter may join the same Storage transaction through an injected port. Governance has no direct Audit dependency. An absent qualified baseline leaves privileged operations closed. Construction or import performs no external operation and supplies no globally trusted principal or policy.

## Acceptance

**ZIP-GOVERNANCE-LIB-T01.** Compile a downstream fixture that evaluates through the public interface. Initialize with no qualified policy and verify denial. Verify consumers cannot bypass authority by importing internal claim or revocation constructors.
