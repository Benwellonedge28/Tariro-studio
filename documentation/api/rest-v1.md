# REST API v1

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Default server bind is loopback. Require authenticated session for all workspace-scoped actions; health exposes only version readiness and capabilities exposes context-appropriate feature flags. Remote access requires explicit HTTPS and audience-bound credentials.

## Procedure

Use JSON UTF-8 and route prefix /api/v1. Mutation requests carry Idempotency-Key and expected_revision when changing a durable record. A 202 operation returns operation_id and a status URI. A duplicate key with a different body returns 409. Errors have code, message, request_id, retryable and optional safe details.

## Verification and recovery

Return 400 invalid input, 401 invalid session, 403 deny, 404 absent or concealed resource, 409 stale revision, 413 body limit, 429 bounded admission and 503 unavailable side effect. Use SSE sequence IDs for progress; an expired cursor returns 410 and a snapshot URI. Resolve `api.max_request_bytes` and `api.max_principal_concurrency` from validated configuration and tighten using operation-specific policy and availability.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)

## Route ownership and methods

Paths are relative to `/api/v1`. Collection reads use `limit` and opaque `cursor`. Resolve `api.default_page_items` and `api.max_page_items` at request admission; reject out-of-range requests before fetching or allocating results. Mutations reference the repository or assignment by immutable ID. Routes for unreleased subsystems return a structured `unsupported_capability` response.

| Path | Method and contract |
| --- | --- |
| /health, /capabilities | GET readiness or version, feature and limit negotiation |
| /sessions | POST authenticate/pair; DELETE revoke the current session |
| /users, /workspaces | GET authorized identities and workspaces; POST workspace creation with owner scope |
| /repositories | GET scoped list; POST register repo identity and location |
| /repositories/{id} | GET metadata and latest pinned revision |
| /repositories/{id}/inspect, /instructions, /pull-requests | GET pinned snapshot summary, applicable instructions or scoped PR state |
| /assignments | GET owner-visible list; POST `{repository_id, base_revision, requirements, scope, budget}` |
| /assignments/{id} | GET state, state revision, latest checkpoint and outstanding effects |
| /assignments/{id}/plan | POST normalized plan and output digest |
| /assignments/{id}/run, /pause, /resume, /cancel | POST revision-checked lifecycle command |
| /assignments/{id}/progress | GET SSE with `Last-Event-ID` and subject authorization |
| /assignments/{id}/evidence | GET filtered evidence and scoped artifact references |
| /agents, /models, /workflows | GET registered capability set; POST scoped definition or model registration |
| /inference | POST authorized generation or embedding request; SSE for streamed generation when negotiated |
| /memory, /knowledge, /search | GET scoped results; POST explicit query when filters exceed query-string budget |
| /artifacts, /approvals, /permissions | GET scoped artifacts and policy decisions; POST approved decision/grant operation on the respective collection |
| /resources, /audit, /plugins, /mesh | GET authorized operational state; POST explicit versioned plugin or mesh mutation when enabled |
| /events | GET SSE with topic scope and resume cursor |

A status response returns `{id, state, state_revision, checkpoint, outstanding_effects, updated_at}`. A progress event supplies `{stream_id, sequence, kind, occurred_at, payload}` with no credentials or prompt text. On a revision conflict return the current revision and require the client to re-read and replan. Approval submission binds request ID and immutable effect digest. Authorization happens again inside the effect boundary.
