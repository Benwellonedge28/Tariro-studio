# Exclusive replay and snapshot recovery

**ZIP-EVENTS-REPLAY-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/replay.rs`

The cursor after-value is the last durably processed sequence, or zero when no event has been processed. The retained floor is the highest sequence removed from a contiguous prefix. A cursor equal to the floor is valid. A cursor below it or from an older root returns CursorExpired to an authorized caller. A cursor ahead of committed head is InvalidCursor. At the head return an empty page. Otherwise return rows strictly after the after-value using exclusive comparison, avoiding addition at u64 maximum. Validate stream/root/floor/head and rows from one consistent snapshot. Normal compaction does not invalidate still-usable cursors solely because the floor moved.

Return recovery instructions without revealing a protected snapshot. Include a snapshot reference only if currently authorized and verified for that stream and epoch. If none exists, report snapshot unavailable and suspend resume. To install a snapshot, verify its stream, root epoch, included sequence and projection digest, then atomically replace the projection and checkpoint under current session authority. Reject stale snapshots whose sequence now falls below the floor. A restored root requires requalification of affected effects under the Storage restore contract.

**ZIP-EVENTS-REPLAY-T01.** Test cursor below, exactly at and above the floor, at the head, ahead of the head and from an older root. No expired cursor silently starts over.
