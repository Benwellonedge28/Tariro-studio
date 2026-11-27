# Object staging and publication

**ZIP-STORAGE-OBJECTS-CONTENT-ADDRESSED-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/objects/content_addressed.rs`

Stage bytes into a freshly created private temporary sibling on the target volume. Reserve storage and validate free space before writing. Stream within admitted input, output and time budgets. Abort before consuming excess input into the staged file. Hash exact logical bytes and verify actual length. If encrypted at rest, stream an authenticated envelope using the configured format. The content identity stays the logical digest and length. Deduplicate only within the same storage protection domain. Never use content identity alone to grant access.

Generate the target path from the validated digest and owned storage root. Under a per-object gate, either validate and reuse an existing digest/length target or promote the staged file atomically without replacing an existing target. Sync file data and qualified directory metadata. Check the final target identity after promotion. If an existing target is damaged or inaccessible, quarantine or block and preserve evidence. Do not overwrite it or report duplicate success. The object gate yields a scoped, in-memory staged pin. Its drop cannot create domain metadata.

A staged pin can be consumed by a metadata commit. Before commit, an interruption may leave temporary or orphan bytes with no domain visibility. After commit, the object must be both durable and authorized through the metadata link. Never accept a bare pathname or worker-supplied proof for those checks. Platform adapters unable to qualify atomic promotion and durable directory changes return Unsupported before enabling this mode.

**ZIP-STORAGE-OBJECTS-CONTENT-ADDRESSED-T01.** Repeat a bounded put with equal bytes and observe one immutable target. Corrupt the existing target in an isolated fixture and verify the next put fails without overwriting it.
