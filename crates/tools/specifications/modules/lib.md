# Typed tool service facade

**ZIP-TOOLS-LIB-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/lib.rs`

## Boundary and inputs

Declare the [Tools modules](../../DESIGN.md) and forbid unsafe first-party code. Export the typed descriptor, registry observations, validated invocation input and result boundary. Keep raw dispatch constructors, key and scope verifiers and untrusted protocol DTOs internal.

## Behavior and failure handling

Use Foundation, Governance, Resources and Sandbox as the only first-party Cargo dependencies. Compose Terminal, networking and external transports through enrolled interfaces. Import and descriptor construction perform no discovery, external call or process launch. Access to qualified adapters requires explicit active setup and effect authority.

## Acceptance

**ZIP-TOOLS-LIB-T01.** Compile a synthetic consumer using public descriptor and validation types. Verify construction and linking do not call network or process adapters and raw effect constructors are inaccessible.
