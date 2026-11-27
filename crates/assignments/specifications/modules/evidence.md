# Evidence references and immutability

**ZIP-ASSIGNMENTS-EVIDENCE-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/evidence.rs`

Immutable evidence has stable ID, artifact digest, plan digest, candidate tree or unit digest, stable requirement ID, verifier identity and version, test/fixture identifier, environment and policy references, observed verdict, and raw evidence reference with authorized access. Outcomes distinguish passed, failed, blocked, unavailable and skipped. Record evidenced conditions and observed output references, separating generated conclusions from observations. Only a qualified verifier supplies a passing observation.

On insertion and acceptance validate verified artifact identity, current required policy and verifier compatibility, reviewed candidate, required test ID and evidence provenance. Verify that every cited reference resolves. Reject equal evidence ID with a different immutable record. Pin durable references through checkpoint and sealed-candidate retention. A changed plan, source, candidate or verifier contract reopens the affected checks. Preserve past observations as historical evidence. Never fabricate an outcome on retry or import.

**ZIP-ASSIGNMENTS-EVIDENCE-T01.** An evidence record with a correct requirement but a different candidate digest cannot satisfy acceptance. Missing or synthetic prose-only observations cannot complete the assignment.
