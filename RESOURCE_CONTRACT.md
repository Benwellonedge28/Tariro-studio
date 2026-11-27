# Shared resource admission contract

**ZIP-RES-001 · v1.1 candidate · Owner** Resource and runtime maintainers

Every operation requiring managed capacity obtains an authorized lease before it allocates, spawns, opens a stream, attaches a device or invokes an adapter. [Admission](crates/resources/specifications/modules/admission.md) owns the public Rust interface. It returns an opaque `ResourceLease`; the manager keeps the corresponding durable reservation private. Runtime, compilation, inference, tools and adapters consume this interface through existing dependencies. Bind each lease to one authorized attempt, one coordinator epoch and its complete admitted vector.

## Capacity and accounting

Define every pool by scope, physical identity where relevant, metric and unit. Account concurrent occupancy such as RAM, device memory and reserved bandwidth separately from metered allowance such as tokens and minor currency units. Separate currencies, devices and volume identities. A monotonic deadline constrains each operation independently. Never add deadlines or subtract them from shared capacity.

Admission checks the same demand against the host or service pool and every applicable workspace and assignment quota. Resolve the complete set of pools from trusted bindings. Unknown or stale required measurements fail admission. An observed zero is a known capacity. Convert observations to a common accounting basis before applying headroom and policy, and never debit the same occupancy twice. [Allocator rules](crates/resources/specifications/modules/allocation/allocator.md) specify the checked arithmetic.

Resource estimates distinguish minimum and preferred demand. A consumer may request a smaller profile only within its authorized quality floor. A change of locality, provider, or data exposure requires the corresponding authority. Record the selected demand, measurements, configuration, grant revision and reason. Policies and adapters supply finite capacities. Advisory hardware profiles supply starting preferences.

## Lease lifecycle

[Reservation](crates/resources/specifications/modules/allocation/reservation.md) defines durable transitions and replay. Expiry or revocation fences new work and output, including retries of an already accepted command. Occupancy remains held until verified teardown or reconciliation proves it absent. When a metered provider result is uncertain, hold unspent reservation until the applicable receipts reconcile. Release never refunds verified consumption.

Pressure closes admission for affected pools and may request cancellation or approved degradation. Degrade only after releasing the superseded demand safely or reserving its permitted overlap. The model owner may evict only unpinned eligible models. If containment cannot install hard controls, do not dispatch an operation that requires them. A resource lease does not confer permission for an external effect.

## Acceptance

Use the [admission fixtures](contracts/acceptance/resources/admission-fixtures.json) to check atomic admission, deadline independence, accounting normalization, revocation, expiry, fenced cleanup and metered replay. Keep a separate adapter integration test for real containment and host pressure. Independent design review and operational qualification are separate gates.
