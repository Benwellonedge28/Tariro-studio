# Bounded elapsed duration

**ZIP-FND-DUR-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/types/duration.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
#[derive(Clone, Copy, Debug, Eq, PartialEq, Hash)]
pub struct DurationMillis(u64); impl DurationMillis { pub const fn new(value: u64) -> Self; pub const fn get(self) -> u64; pub fn checked_add(self, other: Self) -> crate::result::Result<Self>; pub fn as_std(self) -> std::time::Duration; }
```

## Implementation and invariants

Represent nonnegative integer milliseconds with no hidden unit conversion. checked_add returns QuantityOverflow. as_std uses from_millis. Encode as a u64 in binary and canonical decimal string in JSON to preserve the full range. A DurationMillis alone is neither a deadline nor a grant; runtime anchors it to a monotonic instant.

## Acceptance

FND-DUR-T01. Test zero, maximum value and addition across the representation bound. Verify no saturation and no loss at JSON precision boundary.
