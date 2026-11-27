# Component boundaries

**Contract version** 1.0. Master design §71.

Gateway DTOs are independent from CLI/UI objects. Policy and identity return decisions without executing effects. Resource admission creates leases without owning task outcomes. Repositories own snapshot and ref operations. Verification owns verdicts, while assignments own lifecycle states and references to evidence.

## Implementation and acceptance

Use narrow read and effect adapters with typed requests. A boundary may surface a capability as unavailable, deny according to policy, or return an observed failure. Avoid direct cross-crate database table access.
