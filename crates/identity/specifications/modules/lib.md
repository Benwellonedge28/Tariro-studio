# Identity service boundary

**ZIP-IDENTITY-LIB-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/lib.rs`

## Boundary and inputs

Declare the modules in the [Identity design](../../DESIGN.md) and forbid unsafe first-party code. Expose immutable typed principal views and authenticated membership, credential-reference and session APIs. Keep proof-verifier internals, raw journal mutation and principal context constructors private.

## Behavior and failure handling

Use Foundation and Storage as the only first-party dependencies. Compose trusted authentication, clock and local/external enrollment adapters at the application boundary. Import and DTO construction access no secret store, IAM service or journal. Identity proof establishment is distinct from effect authorization.

## Acceptance

**ZIP-IDENTITY-LIB-T01.** Compile a synthetic downstream DTO consumer with no started services. Verify it cannot construct a verified principal context by directly instantiating stored data or untrusted claims.
