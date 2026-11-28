# Sandbox capability facade

**ZIP-SANDBOX-LIB-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/lib.rs`

## Boundary and inputs

Declare the [Sandbox modules](../../DESIGN.md) with unsafe first-party code forbidden. Expose typed profile requirements, scoped capability observations and supervised preparation and cleanup interfaces. Keep uncontrolled handles and backend constructors private.

## Behavior and failure handling

Use Foundation, Governance, Resources and Security as the approved first-party dependencies. Bind Runtime supervision through the application composition boundary instead of adding a reverse dependency. Importing or constructing input types performs no process or network work. Expose no unconfined compatibility route.

## Acceptance

**ZIP-SANDBOX-LIB-T01.** Compile a synthetic consumer preparing a validated profile through the public service. Verify there is no public constructor for a live workload, and missing isolation denies under every exposed constructor.
