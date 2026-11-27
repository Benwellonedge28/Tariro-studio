# Quarantine of terminal delivery failures

**ZIP-EVENTS-DEAD-LETTER-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/dead_letter.rs`

After the approved retry policy classifies a delivery as exhausted or permanently unsupported, write a scoped dead-letter record with original event identity, sequence, root epoch, consumer, sanitized classification, bounded attempt history and immutable evidence reference. Use a revision check tied to expected checkpoint and session. Failure to record it leaves the original unresolved delivery unchanged. Quarantine is not an acknowledgement. Later events for this consumer cannot bypass the blocked sequence.

An authorized redrive uses fresh admission and session authority and reuses the same committed event. Reconcile uncertain effects before redrive. Only a verified processing receipt or an independently authorized snapshot that legitimately replaces the projection may move past the blocked event. Preserve original records through resolution for the configured audit duration.

**ZIP-EVENTS-DEAD-LETTER-T01.** Fail the dead-letter write, then retry successfully and confirm the cursor does not move. Redrive with the original event and advance once after verified processing.
