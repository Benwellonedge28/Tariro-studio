# Rust interface standard

**ZIP-API-001 · v1.0 · Owner:** Interface maintainers. **Maturity:** D4 candidate.

Publish complete signatures, type definitions, modules and visibility. For every parameter specify validation, units, lifetime, ownership and whether it can contain sensitive data. Name preconditions, postconditions, side effects, linearization point, error mapping and concurrency guarantees. Include an example call and a misuse test.

Prefer concrete synchronous interfaces for pure value types. A replaceable async adapter that callers store behind `dyn` returns an explicit `Pin<Box<dyn Future<Output = Result<T, E>> + Send + 'a>>` tied to its receiver or request lifetime. Document allocation charging and drop behavior. A static-dispatch trait may use `impl Future` if all consumers use generic bounds; an architecture diagram does not imply object safety.

Mutation inputs carry authorization context and expected revision or an idempotency key where required. A replay with the same key and payload returns the recorded outcome. A changed payload conflicts. Protocol DTOs encode typed errors without credentials or internal handles. Contract tests compile signatures at every supported feature boundary and exercise cancellation before and after the committed effect.
