# Typed identifier module

**ZIP-FND-ID-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** D4 candidate; central kind registry review is required before D5. **Source:** `crates/foundation/src/identity/identifier.rs`.

## Types and ownership

```rust
use uuid::Uuid;
use crate::error::FoundationError;

#[derive(Clone, Copy, Debug, Eq, PartialEq, Hash)]
pub enum IdKind { Principal, Workspace, Repository, Assignment, Task, Event, Artifact, Device }

#[derive(Clone, Copy, Debug, Eq, PartialEq, Hash)]
pub struct Identifier { kind: IdKind, uuid: Uuid }

impl Identifier {
    pub fn from_uuid(kind: IdKind, uuid: Uuid) -> Result<Self, FoundationError>;
    pub fn parse(expected_kind: IdKind, input: &str) -> Result<Self, FoundationError>;
    pub const fn kind(&self) -> IdKind;
    pub const fn as_uuid(&self) -> &Uuid;
}
```

Signatures define the contract; bodies belong to implementation. Keep fields private and use only validated construction. Depend on a qualified UUID type/parser. Device or provider ID discovery and UUID generation belong to separate modules. Callers choose the typed field's expected kind; an external input cannot override it.

## Parse and serialization

1. Require exactly 36 ASCII bytes with hyphens at zero-based indices 8, 13, 18 and 23.
2. For all other positions accept lowercase ASCII hexadecimal bytes only. Reject leading/trailing whitespace, upper case, braces, alternate representations and partial input as `InvalidIdentifier`.
3. Decode 16 bytes in network order into the UUID type. All-zero bytes return `NilIdentifier`. `from_uuid` enforces the same nil check. No UUID version or variant is inferred from the kind in this contract.
4. Retain both kind and UUID. Equality and hashing incorporate both. Format bare UUIDs as lowercase hyphenated strings only in typed fields. Generic records must separately serialize the kind as a lowercase stable enum name. The enclosing schema owns compatibility and denies unknown kinds.

The fixed length is a UUID representation invariant. Parsing is synchronous, immutable and bounded by representation; no scheduling, persistence, cancellation, retention or host discovery belongs here. The parser does not perform identity verification or grant access. Error values contain no rejected bytes. The component supports every target on which the approved UUID dependency compiles.

## Acceptance

FND-ID-T01 round-trips `f085e513-c740-416b-d33d-26758ead6d0c` in a typed repository fixture. FND-ID-T02 rejects uppercase, missing hyphen, surplus input and nil value with separate errors. FND-ID-T03 uses the same UUID with two kinds and asserts inequality and distinct keys. FND-ID-T04 mutates the byte sequence through a property fixture and checks no panic or partial acceptance. Verify the [interface standard](../../../../../API_STANDARD.md) before approval.
