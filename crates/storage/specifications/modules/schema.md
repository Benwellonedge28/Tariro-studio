# Embedded storage schema and keys

**ZIP-STO-SCH-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D4 candidate. **Planned source:** `crates/storage/src/schema.rs`.

The logical keyspace is backend-neutral. Binary keys concatenate fixed-width identifiers and big-endian unsigned integers; a one-byte kind precedes a UUID when a domain table admits multiple kinds. Use the same stable kind registry as the ID DTO. Repository identifiers owned by external providers resolve to locally assigned immutable UUIDs before storage.

| Table | Key | Record fields |
| --- | --- | --- |
| schema | singleton byte zero | format major/minor u16, generation u64, migration ledger head |
| domain_records | namespace UUID + type byte + record UUID | payload schema major/minor u16, revision u64, tagged digest, payload length and bytes |
| objects | algorithm byte + 32-byte SHA-256 | length u64, staged/ready state, durable reference counter, retention marker |
| event_outbox | stream UUID + sequence u64 | event ID, schema version, payload reference, correlation ID, occurrence timestamp |
| audit | workspace UUID + sequence u64 | redacted record, prior digest, record digest, signature reference if applicable |
| transaction_receipts | transaction UUID | batch digest, committed generation u64, outcome version |
| migration_ledger | migration sequence u64 | from/to versions, input and output digests, stage and backup reference |

Expose `encode_key(key: &LogicalKey) -> Result<Vec<u8>, StorageError>` and `decode_key(table: TableId, bytes: &[u8]) -> Result<LogicalKey, StorageError>`. Charge output bytes through admitted batch limits. Reject wrong key length/tag, duplicate identifiers, unknown mandatory schema and unsigned overflow. Never accept a partial decode. Namespace IDs are validated at construction and bytes are encoded in network order. Sequence keys preserve per-stream numeric ordering.

The domain payload is opaque to generic storage. Each domain publishes its own versioned encoder with deterministic bytes and validates field types. Typed schema owners must approve each numeric kind tag before this registry reaches D5. Pending owner decisions include table-specific compression and encryption envelope identifiers. Keep live credentials out of all tables.

STO-SCH-T01 verifies exact key vectors, order, parse round-trip and rejection of extra bytes. T02 shows backups preserve keyspace and blob references; T03 rejects unknown schema before write access. See [persistence standard](../../../../PERSISTENCE_STANDARD.md).
