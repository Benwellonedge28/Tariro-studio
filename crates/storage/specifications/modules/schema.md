# Embedded storage schema and keys

**ZIP-STO-SCH-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/schema.rs`

The logical schema is shared by qualified backends. Binary keys concatenate fixed-width components using UUID bytes in network order and unsigned integers in big-endian order. A binary digest key uses algorithm tag 1 for SHA-256 followed by the 32 digest bytes. Wire strings using the Foundation tagged digest are separate. Validate namespace and UUID identifiers before encoding; reject extra key bytes, unknown tags, nil UUIDs and unsupported write formats before any mutation.

| Table | Key | Required value and invariant |
| --- | --- | --- |
| schema | singleton byte zero | format major/minor u16, committed generation u64, migration ledger head u64, logical store identity |
| domain_records | namespace UUID + type byte + record UUID | payload schema major/minor u16, monotonically increasing revision u64, live/tombstone flag, live payload digest, length and bytes, ordered unique object links |
| objects | protection-domain UUID + digest key | logical length u64, ready/deleting tag, reference count u64, retention marker and authenticated envelope version where applicable |
| event_outbox | stream UUID + sequence u64 | event UUID, schema version, payload object reference, optional correlation UUID, canonical occurrence timestamp |
| event_identity | stream UUID + event UUID | committed sequence; retained while the producer can replay the event ID |
| stream_head | stream UUID | last committed sequence u64; survives outbox retention |
| transaction_receipts | transaction UUID | canonical batch digest, committed generation u64 and outcome version |
| audit | workspace UUID + sequence u64 | redacted record, prior digest, record digest and signature reference when required |
| migration_ledger | migration sequence u64 | from/to versions, input and output digests, stage and backup reference |
| backup_pins | snapshot UUID | generation u64, operation identity, owner and durable lifecycle phase |
| recovery_journal | operation UUID | kind, target root or attempt identity, phase and verified evidence references; phase changes use CAS |

Empty stores start with generation 0. The first sequence or record revision is 1. Counters are checked before advancement. A tombstone retains record schema and revision while excluding live payload links; its physical retirement requires an equivalent stale-writer fence. Never reset a stream head during outbox pruning. Update event identity, stream head and event envelope in one transaction. Outbox delivery cursors are separate durable state in the Events domain.

Use `encode_key(key: &LogicalKey) -> Result<Vec<u8>, StorageError>` and `decode_key(table: TableId, bytes: &[u8]) -> Result<LogicalKey, StorageError>`. Charge the owned buffers. Opaque payloads use their owners' schemas. A format change requires an approved migration map with tagged type identifiers, canonical value codecs and any encryption metadata. Unsupported adapters and schemas remain closed to writes. Domain type tags and the selected backend's value codecs require review before D5.

**STO-SCH-T01–T03.** Verify exact key vectors and ordering, stable logical backup keys and explicit denial for unsupported formats.
