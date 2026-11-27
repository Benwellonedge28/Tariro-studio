# Unit-safe resource arithmetic

**ZIP-FND-QTY-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/types/quantity.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct Quantity<U> { value: u64, unit: core::marker::PhantomData<U> } impl<U> Quantity<U> { pub const fn new(value: u64) -> Self; pub const fn get(self) -> u64; pub fn checked_add(self, other: Self) -> crate::result::Result<Self>; }
```

## Implementation and invariants

Use one marker per metric/representation, for example bytes and tokens are distinct. Use checked arithmetic; overflow returns QuantityOverflow. No implicit coercion, signed conversion or use as a lease. The enclosing schema supplies the unit tag on wire.

## Acceptance

FND-QTY-T01. Compile-fail adding different unit markers; test max+1 and zero. Inspect generic storage has no dynamic unit dispatch.
