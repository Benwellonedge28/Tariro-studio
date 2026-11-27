# Backup integrity and closure

**ZIP-STORAGE-BACKUP-VERIFICATION-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/backup/verification.rs`

1. Open only an authorized package within supplied archive, entry, byte and time bounds. Verify manifest version, logical store and approved scope. Verify a required signature against the configured trusted key before using any manifest claim. A checksum provides integrity evidence and never confers authority.
2. Derive expected rooted destinations from declared object identity. Reject duplicate entries, aliased destinations, extra entries, symlinks and path traversal. Do not extract names supplied by an archive as paths. Decode with checked arithmetic and reject excess decompressed output before making it visible.
3. Verify metadata export digest and complete decode. Compute reachable objects across the restored record, outbox and audit references. Require exact equality with the manifest set. Verify both archived bytes and logical digest and length after authenticated decryption where required. A missing key, unsupported codec, mismatched digest or cross-scope identity fails verification.
4. Verify sequence high-water counters, receipt generations, revision compatibility, reference counts and schema. Require an approved migration chain for a readable but incompatible writer format. Revalidate the migrated candidate at its final version. Record manifest digest, verification outcome and evidence under the restore operation identity.

**ZIP-STORAGE-BACKUP-VERIFICATION-T01.** Try one missing reachable object, one extra entry, one obsolete format without migration and one bad digest. Each blocks activation. Test a valid signed synthetic manifest under the configured trust policy.
