# Explicit foundation prelude

**ZIP-FND-PRE-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/prelude.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub use crate::{error::FoundationError, identity::identifier::{IdKind, Identifier}, limits::{Limit, Usage}, result::Result, types::digest::Digest};
```

## Implementation and invariants

Keep v1 exports to exactly these names. No glob import or hidden module wiring. Adding names can break downstream wildcard imports and requires API review.

## Acceptance

FND-PRE-T01. Compile named imports; confirm cancellation source and raw UUID are absent.
