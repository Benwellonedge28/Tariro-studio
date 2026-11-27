# Adaptive resource management

**ZIP-RES-002 · v1.0 · Owner:** Resource and runtime maintainers. **Maturity:** D3.

Use the [shared admission contract](RESOURCE_CONTRACT.md) and [limit classification](LIMITS_POLICY.md). The personal deployment example in the master design refers to a 16 GiB laptop and approximately 900 GB storage. Its example allocations are planning inputs. The active profile can prefer sequential execution and lightweight inference; actual concurrency and model fit are admitted against measured capacity and configured policy.

Discover allocatable capacity for host RAM, CPU availability, accelerator memory per device, storage per volume, process/sandbox limits, and supported network controls. A discovery record states source, units, observation age and whether each bound can be enforced. A profile is an input to admission, with effective bounds derived from the capacity snapshot, active reservations, pressure, mandatory policy and assignment constraints. Unknown required metrics deny admission unless an independently enforceable fallback is defined.

Reserve RAM, device memory, processes, disk, time, concurrency and spending before dispatch. Acquire the whole vector atomically across host, workspace and assignment budgets. Use checked arithmetic. Keep the reservation through shutdown until the supervisor verifies cleanup. Bound streaming discovery, indexing, repository processing, workflow expansion and model requests under the same resource contract.

Under pressure stop new admissions, trim eligible caches or reduce context and parallelism within policy. Protect pinned evidence and avoid changing locality without authorization. Report estimated versus observed use, policy and capacity revisions, limiting coordinate and cleanup status. Test two different effective budgets using the same binary and measure the actual workload before publishing a hardware guarantee.
