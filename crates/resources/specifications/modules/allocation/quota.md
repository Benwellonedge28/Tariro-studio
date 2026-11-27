# Scoped quota intersection

**ZIP-RESOURCES-ALLOCATION-QUOTA-001 · v1.1 candidate · Owner** Resources maintainers

**Planned source** `crates/resources/src/allocation/quota.rs`

Resolve required quota scopes from authenticated assignment and workspace bindings, never from a caller-supplied pool list. For a dimension with several compatible ceilings in a scope, use their minimum. Keep independent host/service, workspace and assignment ledgers. Admit only when every scope has enough free capacity for the requested units. Calculate allowance after admitted holds and applicable verified consumption. Keep different currencies, device IDs, and other incompatible coordinates in distinct ledgers.

A policy can provide a finite cap or explicitly inherit an enforceable ancestor bound for a dimension. Missing required quota resolution denies an attempt. An exact task constraint remains in the assignment contract and cannot be clipped by a profile. Live policy tightening closes admission and may fence existing work according to authority. A valid cleanup principal can still settle or release the original reservation after the change. A metered allowance may reset only at an authorized budget period boundary with reconciled balances. Never erase an unresolved prior period hold or use period change to exceed an overall assignment grant.

**ZIP-RESOURCES-ALLOCATION-QUOTA-T01.** An override cannot raise a system cap. A wider workspace balance cannot make a depleted assignment balance admissible. Releasing a completed metered attempt returns unused units, while verified consumption still reduces future allowance.
