# UTC instant for audit and interchange

**ZIP-FND-TIME-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/types/timestamp.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct Timestamp { seconds: i64, nanosecond: u32 } impl Timestamp { pub fn from_unix_parts(seconds: i64, nanosecond: u32) -> crate::result::Result<Self>; pub const fn unix_parts(self) -> (i64, u32); }
```

## Implementation and invariants

Require nanos below 1_000_000_000 and civil time in UTC years 0001–9999. Seconds are floor since Unix epoch with nonnegative fractional nanos. Invalid range returns LimitExceeded. Interchange uses RFC 3339 UTC with Z and nine fractional digits, no leap-second input. Use qualified calendrical conversion at serialization boundary. Never compare wall time to live monotonic deadlines.

## Acceptance

FND-TIME-T01. Round-trip the instant one nanosecond before the epoch as (-1,999999999). Reject an out-of-range second or fractional ns. Compile and test at wire boundary with fixed-zone fixtures.
