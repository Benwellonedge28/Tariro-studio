# Event service facade

**ZIP-EVENTS-LIB-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/lib.rs`

Expose the public modules error, event, envelope, publisher, subscriber and topic. Keep dispatcher, queue, journal, ordering, replay, deduplication, backpressure, dead_letter and retention crate-private. The public service uses the publisher and subscriber ports. Composition supplies scoped Storage access, authorization, resource permits, receipt verification and runtime supervision. Foundation and Storage remain the only first-party dependencies. Linking or constructing a type performs no database, network or process operation. Opening a subscription validates admission and effective budget before starting supervised work.

**ZIP-EVENTS-LIB-T01.** Type-check a caller using the public envelope and subscription port without allocating a queue or opening a journal. Run adapter tests only through explicit composed services.
