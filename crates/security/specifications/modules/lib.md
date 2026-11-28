# Security facade

**ZIP-SECURITY-LIB-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/lib.rs`

## Boundary and inputs

Declare the [Security modules](../../DESIGN.md) with unsafe first-party code forbidden. Expose redacted authentication and permission decisions, scoped references, trusted control observations, and qualified cryptographic interfaces. Keep mutable epoch setters, proof constructors and secret access callbacks private or adapter-scoped.

## Behavior and failure handling

Use Foundation, Identity and Storage as the only first-party dependencies. Qualified authentication, key handling and effect ownership are assembled through composition. Linking or evaluating typed policy does not open key stores or networks by default. Scoped operations require explicit configured services and verified prerequisites.

## Acceptance

**ZIP-SECURITY-LIB-T01.** Compile a public policy consumer with synthetic trust inputs and no keyring or network. Verify bounded decision output and no inspection of secret bytes or internal trust constructors.
