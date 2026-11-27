# Dependency rules

**Contract version** 1.0. Master design §71.

Use the graph below for first-party Cargo dependencies. Composition roots choose implementations behind consumer-owned interfaces. Test adapters can be wired externally to avoid cycles. For split crates preserve boundary and verify dependency direction before widening.

## Implementation and acceptance

Verification consumes observations through an injected runner trait; it has no dependency on the testing crate. Use a topological workspace metadata check in CI and reject any reverse edge from foundation to a product service.

| Crate | Allowed first-party dependencies |
| --- | --- |
| foundation | None |
| configuration | foundation |
| identity | foundation, storage |
| storage | foundation |
| events | foundation, storage |
| runtime | foundation, storage, events, resources |
| resources | foundation, configuration |
| scheduler | foundation, storage, resources |
| intelligence | foundation, models, resources, providers |
| inference | foundation, models, resources |
| models | foundation, storage, resources |
| context | foundation, repository, search, security |
| reasoning | foundation, intelligence, context |
| memory | foundation, storage, security |
| knowledge | foundation, storage, source-analysis |
| search | foundation, storage |
| agents | foundation, governance, intelligence, runtime |
| orchestration | foundation, agents, assignments, scheduler, verification |
| assignments | foundation, storage, events, governance, verification |
| workflows | foundation, assignments, governance, scheduler |
| repository | foundation, storage, governance, filesystem, terminal |
| source-analysis | foundation, repository |
| engineering | foundation, assignments, repository, verification |
| documentation | foundation, assignments, repository, context, verification |
| compilation | foundation, terminal, resources, repository |
| testing | foundation, terminal, compilation, verification |
| debugging | foundation, terminal, source-analysis, verification |
| research | foundation, networking, storage, security |
| tools | foundation, governance, resources, sandbox |
| terminal | foundation, sandbox, resources |
| filesystem | foundation, security |
| sandbox | foundation, governance, resources, security |
| security | foundation, identity, storage |
| governance | foundation, identity, security, storage, events |
| verification | foundation, repository, storage |
| audit | foundation, storage, security |
| networking | foundation, governance, security, resources |
| synchronization | foundation, networking, storage, audit |
| distributed | foundation, networking, resources, scheduler, synchronization |
| providers | foundation, configuration, networking, security |
| interoperability | foundation, networking, providers |
| plugins | foundation, governance, sandbox, storage |
| sdk | foundation, interoperability |
| observability | foundation, events, security |
| economics | foundation, storage, resources |
| deployment | foundation, verification, governance, storage, networking |
| maintenance | foundation, storage, audit, verification |
| evolution | foundation, governance, verification, repository |
