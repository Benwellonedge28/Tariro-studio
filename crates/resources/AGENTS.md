# Resources crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- One generation model on 16 GiB. Keep host reserve and active work headroom. Unknown GPU capacity is unavailable for hard guarantees.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Concurrent admissions cannot overcommit. Pressure test confirms fallback unloads only unpinned models.
