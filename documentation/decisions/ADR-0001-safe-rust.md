# ADR-0001 · Safe Rust

**Status** Accepted in the master design. Implementation evidence is required separately.

## Decision

Adopt Safe Rust for all first-party code. Workspace crates use forbid(unsafe_code). Native or unsafe transitive dependencies require explicit review and lockfile evidence.

## Consequences

Strict policy reduces memory-unsafe first-party surface while platform isolation remains necessary. A JavaScript editor bridge requires explicit exception; initial bridges can use CLI or LSP.

## Acceptance

Verify all target/features compile and CI rejects a synthetic unsafe block.

[Master design](../../ZIPPORAH-STUDIO-DESIGN.md)
