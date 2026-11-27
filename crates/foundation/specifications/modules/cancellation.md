# Sticky cancellation token

**ZIP-FND-CAN-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** D4 candidate; concurrency qualification required. **Source:** `crates/foundation/src/cancellation.rs`.

```rust
use std::future::Future;
use std::pin::Pin;
use crate::error::FoundationError;

pub struct CancellationSource { /* private shared state */ }
#[derive(Clone)]
pub struct CancellationToken { /* private shared state */ }

impl CancellationSource {
    pub fn new(waiter_limit: usize) -> Self;
    pub fn token(&self) -> CancellationToken;
    pub fn cancel(&self) -> Result<bool, FoundationError>;
}

impl CancellationToken {
    pub fn is_cancelled(&self) -> Result<bool, FoundationError>;
    pub fn cancelled(&self)
        -> Pin<Box<dyn Future<Output = Result<(), FoundationError>> + Send + '_>>;
}
```

The waiter limit is supplied by the admitted caller. Zero lets observers poll `is_cancelled` but prevents registering pending futures. Owning or cloning a token cannot request cancellation. Dropping a source does not change the flag. Dropping a pending wait removes its own registration. Cancellation is an observation, not supervisor shutdown or proof that an external effect stopped.

## State and algorithm

Use an `Arc` to a mutex-protected state with sticky flag, configured waiter limit, a checked sequence of registration IDs, and a bounded map from registration ID to waker. No await while holding the mutex. The waiter future stores its own optional registration ID. Clone the caller's waker before locking. Do not invoke or drop displaced wakers while holding the lock.

| Event | Guard | Result |
| --- | --- | --- |
| First wait poll | Flag clear and capacity available | Reserve one map entry before insertion, assign unique checked ID, store waker, return Pending |
| Poll again | Flag still clear and ID present | Replace only this waiter's waker, return Pending |
| Poll after cancel | Flag set | Clear local ID, return Ready(Ok) |
| First cancel | Flag clear | Set flag and take the waiter map in one critical section; unlock, wake each drained waker, return true |
| Repeated cancel | Flag set | Return false without waking again |
| Pending future drop | ID registered and lock available | Remove only that entry, unlock before dropping its waker |

Validate capacity before registration; return `ObserverLimit` if full and `AllocationFailed` if fallible map reservation fails. Use `QuantityOverflow` on registration ID exhaustion and `SynchronizationFailed` if the mutex is poisoned. Pending future Drop cannot return an error; a poisoned handle already fails closed for every following explicit operation. Calling `cancelled` allocates one boxed future under the caller's already-admitted memory envelope. Rust's process-level allocator failure behavior for infallible allocations applies to that box and the initial Arc; registration growth is fallible. Use no wall clock. Commit uncertainty, grace periods and process teardown belong to [the cancellation standard](../../../../CANCELLATION_STANDARD.md) and runtime.

## Race and terminal-result rules

A wait caches its terminal result and returns that result on later polls without locking, cloning a waker or allocating. While Pending, exactly one registered ID refers to that future. An attempt to replace or drop its registration may encounter an empty map after cancellation; that is expected. A future with a cached error is complete and is not resurrected by a subsequent cancel.

The first successful flag change is the cancellation linearization point. Under the mutex, check the flag before quota or sequence logic. Check the waiter limit before a fallible map reservation. A failure must leave the existing registrations and sequence unchanged. For an already-cancelled token, return ready success even with zero waiter capacity. The cancellation-side map drain must be detached before invoking any waker. Waker callbacks are expected to return normally; a panic originating from an executor callback is outside the wake-delivery guarantee. No callback panic while outside the lock may poison the cancellation state.

The module has no persistence, serialization or network effects. The state machine is process-local; reconstruction creates an independent scope after the runtime reconciles the persisted operation. Waker behavior is subject to Rust's executor contract. Require tests on declared targets, and report waiter operations and cancellation latency from callers without exposing the identity of registered wakers.

## Acceptance

FND-CAN-T01 race first poll with cancellation and prove no lost wake. FND-CAN-T02 drop one pending waiter and verify the capacity returns without removing other waiters. FND-CAN-T03 race two cancel invocations and verify exactly one returns true. FND-CAN-T04 run zero and finite capacity fixtures, including re-poll with replaced waker and cancellation after all waiters have dropped. FND-CAN-T05 use an executor fixture whose waker can re-enter token observation, proving wake and drop occur outside the lock.
