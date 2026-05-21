# TARIRO Studio v4 — Production Multi-Stage Dockerfile
# syntax=docker/dockerfile:1.7
# Supports: linux/amd64, linux/arm64

ARG PYTHON_VERSION=3.12
ARG TARGETPLATFORM
ARG BUILDPLATFORM

# ─────────────────────────────────────────────────────────────────
# STAGE 1: toolchain — OS tools needed at build time
# ─────────────────────────────────────────────────────────────────
FROM ubuntu:24.04 AS toolchain
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
        build-essential curl git ca-certificates gnupg \
        nodejs npm wabt binaryen \
        openocd gdb-multiarch tini \
        firejail bubblewrap \
        qemu-system-misc qemu-system-x86 \
    && apt-get clean

# ─────────────────────────────────────────────────────────────────
# STAGE 2: py-deps — Python venv + all pip dependencies
# ─────────────────────────────────────────────────────────────────
FROM python:${PYTHON_VERSION}-slim AS py-deps
WORKDIR /build
RUN pip install --no-cache-dir -U pip wheel setuptools
COPY requirements.txt .
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -U pip wheel \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt \
    && /opt/venv/bin/pip install --no-cache-dir pip-audit safety \
    && /opt/venv/bin/pip-audit -r requirements.txt || true \
    && /opt/venv/bin/safety check -r requirements.txt || true

# ─────────────────────────────────────────────────────────────────
# STAGE 3: app-source — copy all source, compile bytecode
# ─────────────────────────────────────────────────────────────────
FROM py-deps AS app-source
WORKDIR /app
COPY app.py             ./
COPY tariro_features.py ./
COPY tool_forge.py      ./
COPY litellm_config.yaml ./
COPY allowed_hashes.json ./
COPY seccomp.json        ./
COPY ENTRYPOINT.sh       ./
COPY tariro/             ./tariro/
COPY features/           ./features/
COPY scripts/            ./scripts/
RUN chmod +x /app/ENTRYPOINT.sh \
    && /opt/venv/bin/python -m compileall -q /app/tariro /app/features /app/app.py

# ─────────────────────────────────────────────────────────────────
# STAGE 4: workspace-init — pre-create all workspace directories
# ─────────────────────────────────────────────────────────────────
FROM app-source AS workspace-init
RUN mkdir -p \
    /app/workspace/advanced_multimodal_outputs \
    /app/workspace/adversarial_ai_logs \
    /app/workspace/agent_configs \
    /app/workspace/agi_sandbox/execution_logs \
    /app/workspace/agi_sandbox/risk_reports \
    /app/workspace/alignment_logs \
    /app/workspace/anomaly_detection_logs \
    /app/workspace/automation_scripts \
    /app/workspace/autonomy_policies \
    /app/workspace/backlog_proposals \
    /app/workspace/causal_inference_logs \
    /app/workspace/cognitive_allocation_logs \
    /app/workspace/contextual_memory_data \
    /app/workspace/data_integrity_logs \
    /app/workspace/decision_path_logs \
    /app/workspace/deployment_logs \
    /app/workspace/emergent_behavior_logs \
    /app/workspace/entity_data \
    /app/workspace/ethical_conflict_logs \
    /app/workspace/goal_recalibration_logs \
    /app/workspace/meta_learning_logs \
    /app/workspace/multimodal_outputs \
    /app/workspace/network_healer_logs \
    /app/workspace/optimization_logs \
    /app/workspace/policy_audit_logs \
    /app/workspace/policy_enforcement_logs \
    /app/workspace/quantum_crypto_manager \
    /app/workspace/resource_optimization_logs \
    /app/workspace/sdk_outputs \
    /app/workspace/security_audits \
    /app/workspace/self_evolution \
    /app/workspace/sensory_fusion_logs \
    /app/workspace/simulated_codebase \
    /app/workspace/spatial_data \
    /app/workspace/swarm_events \
    /app/workspace/task_automation_logs \
    /app/workspace/threat_model_logs \
    /app/workspace/tools/bin \
    /app/workspace/tools/specs \
    /app/workspace/ui_adaptation_logs \
    /app/workspace/vulnerability_remediation_logs \
    /app/workspace/workflows \
    /app/workspace/zero_trust_logs

# ─────────────────────────────────────────────────────────────────
# STAGE 5: final — lean runtime image
# ─────────────────────────────────────────────────────────────────
FROM python:${PYTHON_VERSION}-slim AS final

LABEL org.opencontainers.image.title="Tariro Studio v4"
LABEL org.opencontainers.image.description="Autonomous Runtime v4"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.source="https://github.com/Benwellonedge28/Tariro-studio"

RUN apt-get update && apt-get install -y --no-install-recommends tini curl \
    && apt-get clean

RUN useradd -m -u 1000 -s /bin/sh tariro

COPY --from=py-deps        --chown=tariro:tariro /opt/venv /opt/venv
COPY --from=workspace-init --chown=tariro:tariro /app      /app

USER tariro
WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/app"
ENV TARIRO_WORKSPACE="/app/workspace"
ENV OPENAI_API_BASE="http://litellm:4000/v1"
ENV OPENAI_API_KEY="sk-free"
ENV PYTHONUNBUFFERED=1

EXPOSE 7860

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:7860/health || exit 1

ENTRYPOINT ["/usr/bin/tini", "--", "/app/ENTRYPOINT.sh"]
