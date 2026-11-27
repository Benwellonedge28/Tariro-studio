# Versioning and compatibility

**ZIP-CMP-001 · v1.0 · Owner:** Interface and storage maintainers. **Maturity:** D4 candidate.

Identify the version independently for each wire, event, record and plugin family. A major changes required shape or meaning. A minor may add optional fields only when a declared compatibility rule proves older readers can handle them. Version semantics, negotiation and default interpretation are normative. Refuse unknown majors before performing effects.

Persist writer schema, reader compatibility set and downgrade boundary. Readers preserve opaque fields only where the schema explicitly permits round-tripping. A state or policy downgrade cannot weaken active authorization. Stage migrations and keep a verified prior generation for rollback. Advertise capabilities by version and feature independent of binary version.

Test prior supported readers, unknown majors, omitted optional fields, lossless migration and rollback with golden fixtures.
