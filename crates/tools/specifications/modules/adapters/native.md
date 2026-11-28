# In-process tool adapter

**ZIP-TOOLS-ADAPTERS-NATIVE-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/adapters/native.rs`

## Boundary and inputs

Invoke an enrolled typed implementation under the exact adapter revision and allowed resource and effect scope. Use only injected safe host capability ports for scoped actions. A native implementation is eligible only when it can enforce required isolation, budget, cancellation and observable result.

## Behavior and failure handling

Check authority before effect and observe cancellation at bounded safe points. Report provisional or final evidence with the same attempt and descriptor binding. Noncooperative or unobservable mandatory control makes the mode unavailable. Do not add ambient filesystem, network or credential access through a hosted interface.

## Acceptance

**ZIP-TOOLS-ADAPTERS-NATIVE-T01.** Offer a synthetic native action with one missing required isolation proof. Verify it is not eligible and no implementation call occurs. Validate that an approved read cannot obtain a mutation port.
