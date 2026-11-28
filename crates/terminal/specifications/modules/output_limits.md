# Atomic shared output accounting

**ZIP-TERMINAL-OUTPUT-LIMITS-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/output_limits.rs`

## Boundary and inputs

Resolve a single finite combined byte cap from terminal.max_output_bytes and all tighter applicable grant and lease envelopes. Both streams reserve against the same checked counter before buffering or storing. Stage accepted portions under bounded scratch capacity and keep observed stream totals where authorized.

## Behavior and failure handling

Serialize competing charges or use an equivalent atomic reservation. A requested read may retain only the admitted prefix. On cap exhaustion follow the resolved stop or bounded truncation policy and record explicit incomplete output. Never allow unbounded drain buffering or deadlock while a child waits on a full pipe. Keep output decisions separate from cleanup and exit.

## Acceptance

**ZIP-TERMINAL-OUTPUT-LIMITS-T01.** Race two stream readers requesting the final available byte. At most one can retain it. Flood both streams and verify aggregate retained bytes stay within the cap, with explicit overflow and verified supervised stop.
