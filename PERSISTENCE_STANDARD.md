# Persistence and durability standard

**ZIP-PST-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D4 candidate.

Every durable entity defines key and byte encoding, exact value schema, revision and index maintenance, ownership, sensitivity, retention and backup participation. Primary and foreign identities use stable namespaces. Secondary indexes are updated atomically with authoritative records or documented as rebuildable projections with generation tracking.

For mutable state use compare-and-swap under one transactional writer and snapshot reads. Stage immutable bytes on the destination volume, validate and sync, atomically promote, then commit object references, domain records and outbox. Storage adapters declare the durability guarantee of completion. A crash before metadata commit can leave unreferenced bytes; a committed reference to absent bytes is corruption and blocks affected work.

Make migrations independently repeatable and ledgered. Take a consistent metadata+object snapshot, stage conversion, check references and indexes, then cut over atomically. Roll back to a previously verified compatible generation. Test kill points around staging, sync, metadata commit, index promotion and restore.
