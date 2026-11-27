# System requirements

The applicable subsystem specification defines the schema and acceptance protocol for each requirement. Release evidence records the requirement ID, expected observation, actual observation and immutable artifact references.

| ID | Requirement | Acceptance |
| --- | --- | --- |
| ZR-001 | Persist every verified assignment work unit and state transition. | Kill and restart after document 17, resume at 18. |
| ZR-002 | Block out-of-scope file writes, deletes and publications. | Traversal, nested instruction, 31-file and implementation-file cases fail. |
| ZR-003 | Preserve denials, expiry and revocation across restart. | Expire or revoke while queued and between verify and publish, then inspect audit. |
| ZR-004 | Enforce byte, process, time, concurrency and spend limits. | Induced resource pressure respects profile limits and produces an actionable outcome. |
| ZR-005 | Require exact independent evidence for completion. | Tamper with an artifact or omit a required check and observe a blocked verdict. |
| ZR-006 | Keep local operations available without internet. | Replay, inspect, verify and run a deterministic workflow with network cut. |
| ZR-007 | Reconcile external effects across interrupted responses. | Lose push and PR acknowledgments, then confirm one intended branch and PR. |
| ZR-008 | Use Safe Rust and verified build inputs. | CI shows workspace policy, dependency review, SBOM and integrity gates. |
| ZR-009 | Version and negotiate all public interfaces. | Previous supported minor interoperates and unknown major receives structured rejection. |
| ZR-010 | Provide verified export and restore. | Restore onto a clean instance with exact artifact digests and no copied live credentials. |
| ZR-011 | Redact private credentials before durable output or model traffic. | Synthetic canaries are absent from prompts, logs, audit exports and artifacts. |
| ZR-012 | Enforce editor-neutral API and provider negotiation. | CLI works without editor or remote provider. Unsupported features are explicitly reported. |
| ZR-013 | Keep idle runtime below 500 MB excluding loaded models and large indexes. | Measure process tree after stabilization and report raw measurements and target platform. |
| ZR-014 | Authenticate remote control and bind to loopback by default. | Fresh install has no remote listener; remote mode rejects wrong identity and audience. |
| ZR-015 | Profile local inference without automatic egress. | Personal profile loads one model and refuses a second or oversize context. |
| ZR-016 | Require separately authorized production release and merge. | A successful build and a passing PR confer neither permission. |
