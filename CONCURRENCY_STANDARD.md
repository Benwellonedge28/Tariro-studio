# Concurrency and ownership standard

**ZIP-CON-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D4 candidate.

Each asynchronous task has one supervisor, one attempt identity and one cleanup owner. Every operation defines its shared and exclusive state, synchronization primitive, lock order, linearization point and acceptable racing outcomes. Do not await I/O while holding a synchronous mutex or a transaction guard. Transfer work through resource-admitted, bounded queues with an explicit full-queue result or backpressure.

Use monotonic time for live leases, durable revisions for restart and epochs to fence stale workers. Reserve resource vectors atomically before dispatch. Multipool locking uses stable pool ordering. A cancellation or timeout cannot release capacity for children whose cleanup is unconfirmed. Track lease ownership through asynchronous teardown.

Test parallel attempts, lost wakes, shutdown while a queue is full, panic containment and stale commit races. Where model checking is appropriate, use a dedicated bounded scheduler fixture. Include actual stress run parameters in evidence.
