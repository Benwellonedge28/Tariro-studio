# Bounded health observation

**ZIP-PROVIDERS-HEALTH-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/health.rs`

## Required implementation behavior

Use authorized probes, deadlines and minimal evidence. Report last observed status separately from declared capability; no auto-fallback.

## Acceptance

**ZIP-PROVIDERS-HEALTH-T01.** Offline profile blocks external probe.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
