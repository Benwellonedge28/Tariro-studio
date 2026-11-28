# Scoped write staging

**ZIP-FILESYSTEM-WRITER-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/writer.rs`

## Boundary and inputs

Accept exact scoped target, validated expected preimage, immutable input reference and current operation, byte and time allowances. Reserve private staging through [temporary](temporary.md). The writer copies verified bytes within budget, checks actual size and digest and produces a staged receipt only.

## Behavior and failure handling

Check cancellation before each bounded write and preserve the original target before publication. Delegate conditional commit and reconciliation to [atomic write](atomic_write.md). An invalid content digest, over-limit write or staging failure cannot expose partial target bytes. Cleanup follows owned object evidence.

## Acceptance

**ZIP-FILESYSTEM-WRITER-T01.** Force staged write failure and a wrong content digest under an intact destination. Verify the previous bytes remain untouched and no publish is attempted. An accepted stage still requires its own commit check.
