# Resource facade

**ZIP-RESOURCES-LIB-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/lib.rs`

## Boundary and inputs

Declare the [Resources crate modules](../../DESIGN.md), forbid unsafe first-party code and expose the typed admission port, demand representation, opaque leases and qualified capacity views. Keep journal mutation, native probe records and private proof constructors under their owning modules. The application composition root supplies adapter and verifier interfaces.

## Behavior and failure handling

Keep Foundation and Configuration as the only first-party Cargo dependencies. The [admission](admission.md) port owns authoritative reserve, start, charge and release. Public getters carry no activation permission and no cross-tenant raw host or provider detail. Import and type construction have no host, journal or network side effects. Check interface additions under the workspace compatibility policy.

## Acceptance

**ZIP-RESOURCES-LIB-T01.** Compile a synthetic downstream caller constructing a typed request using fake observations. Confirm no probes or mutations occur until an explicit owning call, and a downstream consumer cannot construct its own lease, bypass the allocator or instantiate private journal types.
