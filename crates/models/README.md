# Models

This crate's design covers manifest, content digest, checksum, source/license record, import/download checkpoint.

- [Implementation design](DESIGN.md)
- [Crate contributor instructions](AGENTS.md)
- [Model management](../../specifications/0600-model-management/model-management.md)

Acceptance fixture: Corrupt resume file, change ETag, verify only intact payload becomes Ready.
