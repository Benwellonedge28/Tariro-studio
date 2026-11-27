# Identifier namespace

**ZIP-FND-NS-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/identity/namespace.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct Namespace(String); pub fn parse(input: &str, budget: crate::limits::Limit) -> crate::result::Result<Namespace>; impl Namespace { pub fn as_str(&self) -> &str; }
```

## Implementation and invariants

Check byte budget first, then validate syntax, then reserve and copy. An invalid over-limit input returns LimitExceeded before examining its grammar. Accept lowercase ASCII labels beginning with a letter, continuing with lowercase letters or digits, with a dot between labels. Reject empty input or empty label as InvalidIdentifier. Preserve original canonical bytes; fallible reserve reports AllocationFailed. Namespace conveys organization of keys, never permissions.

## Acceptance

FND-NS-T01. Test dotted names, trailing dot, uppercase, excess bytes, identical round trip and zero budget.
