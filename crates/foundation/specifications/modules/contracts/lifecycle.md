# Lifecycle phase vocabulary

**ZIP-FND-LIF-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/contracts/lifecycle.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub enum Phase { Created, Ready, Running, Draining, Stopped, Failed } impl Phase { pub const fn is_terminal(&self) -> bool; }
```

## Implementation and invariants

Return true only for Stopped or Failed. Do not expose transition authorizations here; each stateful owner defines its binding transition table. Encode phase names by stable lowercase fields in enclosing schema. No implicit restart from a terminal phase.

## Acceptance

FND-LIF-T01. Exhaustively test all six phases; assert drain is nonterminal and carries no cleanup completion.
