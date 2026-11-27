# Foundation implementation order

**Maturity:** D4 candidate. All paths refer to the planned crate layout.

1. Establish `lib.rs`, `error.rs` and `result.rs`. Publish and verify stable error codes before other types depend on them.
2. Add `limits.rs`, `types/quantity.rs` and `types/bounded.rs`. Verify checked arithmetic, units and denial before allocation.
3. Add identifier, namespace, generation and digest modules. Qualify the UUID dependency before introducing it. Parse fixtures without live services.
4. Add timestamp, duration and version. Verify fixed representation, conversion and compatibility fixtures.
5. Add component/capability, lifecycle and compatibility descriptors, validation helpers and provenance. Verify exact visibility paths.
6. Add cancellation under its admitted waiter budget. Run race and re-entrant waker fixtures before integrating the runtime.
7. Wire the explicit public prelude and check that downstream users cannot construct private fields.

The [crate design](../DESIGN.md) links the individual contracts. Compilation, property testing and race tests are implementation gates. The drafted interfaces require independent review before D5.
