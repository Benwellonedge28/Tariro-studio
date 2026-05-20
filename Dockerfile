# TARIRO Studio v4 Dockerfile
# syntax=docker/dockerfile:1.7

ARG TARGETPLATFORM
ARG BUILDPLATFORM

# STAGE 1: TOOLCHAIN
FROM ubuntu:24.04 AS toolchain
ARG DEBIAN_FRONTEND=noninteractive
RUN umask 0022 && apt update && apt upgrade -y && \
    apt install -y --no-install-recommends \
    build-essential curl git python3 python3-pip ca-certificates gnupg \
    nodejs npm wabt binaryen \
    openocd gdb-multiarch tini \
    firejail bubblewrap strace lsof \
    qemu-system-misc qemu-system-x86 \
    && apt clean

# STAGE 2: PYTHON BUILDER
FROM python:3.12-slim AS py_builder
WORKDIR /app

COPY requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -U pip wheel && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt && \
    /opt/venv/bin/pip install --no-cache-dir pip-audit safety && \
    /opt/venv/bin/pip-audit -r requirements.txt || true && \
    /opt/venv/bin/safety check -r requirements.txt || true

# Copy v4 runtime source (studio_v3 files removed, tariro/ is the new runtime)
COPY app.py /app/
COPY tariro/ /app/tariro/
COPY features/ /app/features/
COPY scripts/ /app/scripts/
COPY tariro_features.py /app/
COPY tool_forge.py /app/
COPY litellm_config.yaml /app/
COPY ENTRYPOINT.sh /app/
COPY allowed_hashes.json /app/

RUN chmod +x /app/ENTRYPOINT.sh && \
    /opt/venv/bin/python -m compileall -f /app

# STAGE 3: FINAL
FROM python:3.12-slim
LABEL org.opencontainers.image.title="TARIRO Studio v4"
LABEL org.opencontainers.image.description="Autonomous Runtime v4"
LABEL org.opencontainers.image.licenses="Apache-2.0"

RUN useradd -m -u 1000 tariro
USER tariro
WORKDIR /app

COPY --from=py_builder --chown=tariro:tariro /opt/venv /opt/venv
COPY --from=py_builder --chown=tariro:tariro /app /app

ENV PATH="/opt/venv/bin:$PATH"
ENV TARIRO_WORKSPACE="/app/workspace"
ENV PYTHONPATH="/app"

EXPOSE 7860

ENTRYPOINT ["/app/ENTRYPOINT.sh"]
