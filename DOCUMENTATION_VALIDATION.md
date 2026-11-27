# Specification validation

**ZIP-DOC-001 · v1.1 · Owner:** Documentation and architecture maintainers. **Maturity:** D4 candidate.

Run structural and semantic checks separately. Structural checks verify file inventory, one-to-one mapping from each planned Rust path to an identifiable contract, completeness of headings or justified inapplicability, schema validation, cross-links, ID uniqueness and graph acyclicity. Compile Rust signatures and examples in a fixture after required types exist. A Rust-shaped snippet that does not compile must be identified as pseudocode.

Semantic reviewers compare every rule with the pinned constitution, approved configuration and dependency contracts. Check exact error ordering, crash and cancellation paths, data compatibility, authority and performance definitions. Review component-owned numeric limits against [LIMITS_POLICY.md](LIMITS_POLICY.md). Unresolved interpretations and unsupported claims block D5.

A review report gives candidate commit/blob, validator versions, failures, scope and reviewer identity. Treat machine validation as an input to independent review. Byte-for-byte publication verification says the repository contains the intended artifact, while design acceptance requires the reviewed behavior to be complete.

For migration evidence, verify the pinned [file inventory](contracts/legacy/inventory.json) against the Git tree and validate the [migration map](contracts/legacy/migration-map.json) against the inventory and [record schema](contracts/schemas/legacy-audit.schema.json). Verify target specification links and unique IDs. Report inventory coverage, static review coverage and execution evidence separately. Check support for every observed-behavior claim and successor acceptance case before treating a disposition as reviewed.
