# Production release standard

**ZIP-REL-001 · v1.0 · Owner:** Release maintainers. **Maturity:** D4 candidate.

A release candidate is identified by source commit, toolchain, locked dependency graph, target, build recipe, artifact digests and selected release profile. The release manifest lists the supported capabilities, incompatible changes, migrations, rollback artifact IDs and evidence for the required G01–G16 gates in [VERIFICATION.md](VERIFICATION.md).

1. Build each declared target from reviewed inputs. Include integrity-verifiable artifacts, SBOM, signed provenance and release notes.
2. Verify executable claims against the artifact being promoted. Validate native installation, offline operation, backup and restoration on declared targets.
3. Stage upgrade and rollback against a snapshot fixture. If a migration has no compatible rollback path, block promotion until the owner approves a tested restore plan.
4. Obtain independent review and separate production authority for the manifest digest and destination. Publishing is a governed effect and requires reconciliation if its outcome is unknown.
5. Probe healthy operation after activation. Preserve prior known-good state through the qualification window. Stop promotion on any failed mandatory check.

A design-stage tag may identify documentation without asserting application availability. D5 design approval, implementation test evidence and release authorization are separate records. A signed artifact with missing mandatory evidence fails acceptance.
