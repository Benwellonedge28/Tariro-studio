# Test contract standard

**ZIP-TEST-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D4 candidate.

Each file contract lists applicable unit, integration, public interface, property, fuzz, security, concurrency, cancellation, resource exhaustion, crash/recovery, compatibility, performance, regression, fault injection, platform and end-to-end tests. Explain why an omitted category does not apply to the file or where its behavior is tested.

Record fixture ID and bytes or generator seed, setup, operation sequence, expected outcome and typed error, expected effects and cleanup, and measurable pass/fail conditions. Run deterministic fixtures offline unless test scope includes an approved integration. Use synthetic secrets and repositories.

A skipped, timed-out or missing report fails to satisfy a required test. Record exact executable, args, version, candidate digest, environment, policy, raw result and normalized verdict. Pin each requirement to a positive test and its relevant boundary denial. Prevent tolerance or retry settings from hiding failures.
