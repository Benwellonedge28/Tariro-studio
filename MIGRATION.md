# Tariro Studio migration

The repository has been renamed to Zipporah. The original source is preserved at `legacy` commit `f085e513c740416bd33d26758ead6d0ce89b3bbc`. PR #1 prepared the new main tree with the master design. Verify an archival tag before treating that milestone as completed.

1. Inventory the pinned legacy tree. For each auditable capability record source path, revision, observed behavior and whether the observation was static or executed.
2. Use classifications Preserve, Rewrite, Consolidate, Redesign, Experimental, Simulated, Retire or Blocked. Store one entry per capability in the migration register with target specification and acceptance gate.
3. Rewrite Python/FastAPI runtime responsibilities in Safe Rust. Replace required Redis/Qdrant services with embedded storage/index adapters. Treat Ollama, external search and containers as optional. Keep GitHub integration.
4. Test each replacement against the approved acceptance criteria before retiring a legacy capability. Never execute legacy repository code outside an authorized sandbox.
5. Preserve the archive and commit history. Resolve claims of working legacy features by evidence before migrating their status. Use snapshot import/export contracts and compare data summaries and artifact hashes before activation.

Register schema uses `feature_id,source_path,source_commit,classification,target_spec,status,evidence_refs,rollback`. Record unknowns as Blocked or Experimental with an owner and explicit follow-up gate.
