# Checked limit primitives

**ZIP-FND-LIM-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** D4 candidate. **Source:** `crates/foundation/src/limits.rs`.

```rust
use crate::error::FoundationError;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct Limit { ceiling: u64 }

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct Usage { limit: Limit, used: u64 }

impl Limit {
    pub const fn inclusive(ceiling: u64) -> Self;
    pub const fn ceiling(self) -> u64;
    pub fn check(self, requested: u64) -> Result<(), FoundationError>;
}

impl Usage {
    pub fn new(limit: Limit, used: u64) -> Result<Self, FoundationError>;
    pub const fn remaining(self) -> u64;
    pub fn charge(&mut self, amount: u64) -> Result<(), FoundationError>;
}
```

Accept zero as a finite bound; zero demand against zero succeeds. For `charge`, first use checked addition; overflow returns `QuantityOverflow`. Then compare candidate against the inclusive ceiling; excess returns `LimitExceeded`. Mutate only after both checks pass. Separately typed enclosing records declare the unit; this primitive must never add accounting values from different coordinates. `remaining` is valid by the private invariant `used <= ceiling`.

The caller passes a validated value derived from configuration, policy or admission. No embedded operational defaults. This module never probes hardware, allocates units, covers distributed leases or changes a configured cap. It has no I/O, locks, cancellation, async effects or persistent schema. A concurrent owner synchronizes externally via [resource admission](../../../../RESOURCE_CONTRACT.md). Serializers for containing records revalidate on decode rather than injecting private fields.

FND-LIM-T01 tests zero and inclusive equality. FND-LIM-T02 distinguishes overflow at `u64::MAX + 1` from excess and preserves usage on error. FND-LIM-T03 applies property tests across all valid monotonic charges and confirms the result equals checked cumulative usage. Two configuration-supplied ceilings must change behavior without code changes.
