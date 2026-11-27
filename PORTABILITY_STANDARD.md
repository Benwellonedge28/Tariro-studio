# Platform capability standard

**ZIP-PRT-001 · v1.0 · Owner:** Platform maintainers. **Maturity:** D4 candidate.

Declare capabilities by target and runtime probe. OS identity, filesystem isolation, process containment, TLS, device memory and accelerated inference may differ by platform. Each adapter specifies capabilities it can enforce, operations it refuses, code and evidence for unsupported cases, and fallback allowed by policy.

Normalize units at the adapter. For paths, test case sensitivity, prohibited components, symlink/reparse handling and atomic rename behavior on supported filesystems. For deadlines use monotonic clocks. For physical memory and storage use discovered allocatable capacity and limits from the active sandbox or host. Missing mandatory enforcement denies operation.

Test on each advertised platform. Mark unavailable features explicitly. Treat portable fixture success as evidence for the tested targets only.
