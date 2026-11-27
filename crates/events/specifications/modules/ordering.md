# Per-stream sequence validation

**ZIP-EVENTS-ORDERING-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/ordering.rs`

An envelope sequence is positive, immutable and strictly increasing within a committed stream. Sequence zero exists only as an initial cursor. Storage allocates checked sequence numbers without wraparound. Dispatch reads in numeric order. Occurrence time is display and audit data. Across streams there is no total order. After a snapshot starts at cursor n, the next accepted processing receipt must match the next retained sequence, and comparison stops at the committed tail. A sequence with a different event identity or unexpected gap inside the retained prefix is corruption. On replay, suppress duplicates only when a durable receipt establishes exact identity.

**ZIP-EVENTS-ORDERING-T01.** Reverse event timestamps and verify unchanged delivery order. Replay an envelope at the u64 maximum and verify no wrapped sequence is accepted.
