# Resource management

On the 16 GiB personal profile reserve 4 GiB for host/editor, up to 6 GiB for model weights, 2 GiB for context/buffers, 1 GiB for runtime/indexes and 3 GiB for compilation/headroom. Treat these as startup estimates. Enforce discovered usable capacity, measure actual allocation, and never load a second generation model on this profile. The 900 GB storage planning split is 100 OS, 150 models, 200 repositories, 100 build caches, 50 indexes, 100 snapshots and 200 free/expansion.

Reserve each task's RAM, device memory, processes, disk, time, concurrency and spending before dispatch. Admission acquires the whole vector atomically across host, workspace and assignment budgets. Unit counters use checked arithmetic. Keep the lease during shutdown until the supervisor verifies cleanup. Refuse operations requiring a dimension that cannot be measured or enforced.

Under pressure stop admissions; trim caches, shrink a new model request within its permitted quality floor, unload unpinned models and pause work with a checkpoint. Never evict referenced evidence or resume on a remote machine without authorization. Report estimated versus observed resource use and the specific constraint preventing admission.
