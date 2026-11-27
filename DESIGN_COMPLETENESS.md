# Design completion and independent review

**ZIP-DES-001 · v1.0 · Owner:** Architecture and verification maintainers. **Maturity:** D4 candidate.

Apply this checklist separately to each component revision and its file-level contracts.

| Gate | Required evidence |
| --- | --- |
| Coverage | [Source inventory](contracts/components/source-inventory.json), exact file mappings and applicable [specification sections](SPECIFICATION_STANDARD.md) |
| Determinism | Algorithms, transition guards, error precedence, ownership and irreversible boundaries |
| Integration | Qualified or explicitly unresolved ports, dependency and compatibility review |
| Resource policy | Registered limits, finite fallback, enforcement site, accounting and cleanup |
| Testability | Positive, denial, interruption and recovery cases mapped to each normative requirement where applicable |
| Review | Named independent reviewer, reviewed commit, findings closed or explicit blockers |

D4 requires complete contracts for the advertised scope. D5 requires reproducible structural validation and a separate reviewer to verify semantics and close findings. An available file path, a passing link check or an authored candidate proves only what the evidence actually covers. Inventory status `missing` denotes a missing file contract; `candidate` denotes an existing draft awaiting review. An unresolved cross-component decision blocks D5.

Record the reviewed Git commit, exact contract paths and digests, decision IDs, validator versions and outcome. Reopen approval when a relevant contract changes. Release evidence is governed by [RELEASE_STANDARD.md](RELEASE_STANDARD.md).
