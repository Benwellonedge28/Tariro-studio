# Verification and production gates

A verdict is Pass only if every required gate has an independently valid pass observation for the current input and artifact. Any failure wins; missing or stale evidence blocks completion. Record execution ID, immutable input and output digests, verifier identity/version, policy digest, start/end times, status, and a redacted artifact reference. Preserve failed attempts.

| Gate | Evidence |
| --- | --- |
| G01–G04 | Safe Rust, security findings disposition, effective repository instructions and denied unauthorized effects |
| G05–G07 | Independent evidence, recovery after interruption and resource enforcement under pressure |
| G08–G10 | Filesystem boundary, secret canaries and reconciled Git effects |
| G11–G13 | Offline suite, personal hardware inference suite and public compatibility suite |
| G14–G16 | Clean install/upgrade, backup/restore and signed artifact verification |

Use stable test fixtures and record tool versions, seeds and platform. A skipped suite has its own status and cannot satisfy a mandatory gate. Revalidate after any change to candidate, policy, dependency lockfile or required test inputs. The [Vimbai acceptance scenario](specifications/3600-acceptance/acceptance.md) is mandatory before the reference documentation release.
