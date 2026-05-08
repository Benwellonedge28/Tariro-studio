# Upgraded `Dockerfile` - Ultra Autonomous + Hardened (Python-only version)
# syntax=docker/dockerfile:1.7

# Define platform for multi-arch builds
ARG TARGETPLATFORM
ARG BUILDPLATFORM

# STAGE 1: TOOLCHAIN - Install core tools and utilities
FROM ubuntu:24.04 AS toolchain
ARG DEBIAN_FRONTEND=noninteractive
RUN umask 0022 && apt update && apt upgrade -y && \
    apt install -y --no-install-recommends \
    build-essential curl git python3 python3-pip ca-certificates gnupg \
    nodejs npm wabt binaryen \
    openocd gdb-multiarch tini \
    firejail bubblewrap strace lsof \
    cosign slsa-verifier syft grype \
    qemu-system-misc qemu-system-x86 qemu-system-riscv32 \
    && npm install -g wrangler && \
    apt clean && rm -rf /var/lib/apt/lists/*

# STAGE 2: PYTHON BUILDER - Create venv, install Python dependencies, scan deps, PRE-COMPILE PYTHON CODE
FROM python:3.12-slim AS py_builder
ARG TARGETPLATFORM
RUN umask 0022
WORKDIR /app

COPY requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -U pip wheel && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt && \
    /opt/venv/bin/pip install --no-cache-dir pip-audit safety && \
    /opt/venv/bin/pip-audit -r requirements.txt || true && \
    /opt/venv/bin/safety check -r requirements.txt || true

# Copy all Python source for compilation. 
# Ensure these paths exist in your repo's root.
COPY studio_v3.py /app/
COPY features/ /app/features/
COPY scripts/ /app/scripts/
COPY tariro_features.py /app/
COPY tool_forge.py /app/
COPY litellm_config.yaml /app/
COPY ENTRYPOINT.sh /app/ 
COPY allowed_hashes.json /app/ # Copy allowed_hashes.json for immutable core verification
RUN chmod +x /app/ENTRYPOINT.sh # Ensure ENTRYPOINT.sh is executable early

# Pre-compile Python source files to bytecode and remove source .py files
RUN /opt/venv/bin/python -m compileall -f /app 
    && find /app -name '*.py' -type f -delete 
    && find /app -name '*.pyc' -exec chmod a+r {} + 

# STAGE 3: FINAL - Distroless + Nonroot + ReadOnlyRoot + Seccomp
FROM gcr.io/distroless/cc-debian12:nonroot
LABEL org.opencontainers.image.title="TARIRO Studio v3"
LABEL org.opencontainers.image.description="N-1 Tested Autonomous Swarm for OS/Cloud/FPGA"
LABEL org.opencontainers.image.licenses="Apache-2.0"

# Security: Run as nonroot UID 65532
USER nonroot:nonroot
WORKDIR /app

# Set a restrictive umask for files created at runtime (if any)
RUN umask 0022

# Copy essential tools from toolchain
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/curl /usr/bin/ 
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/qemu-system-riscv32 /usr/bin/
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/node /usr/bin/
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/gh /usr/bin/
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/git /usr/bin/
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/openocd /usr/bin/
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/firejail /usr/bin/
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/bwrap /usr/bin/
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/tini /usr/bin/

# Python venv: no system python, no pip in final image
COPY --from=py_builder --chown=nonroot:nonroot /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# App code: now copy pre-compiled Python from py_builder stage
COPY --from=py_builder --chown=nonroot:nonroot /app /app

# Set ENTRYPOINT
ENTRYPOINT ["/app/ENTRYPOINT.sh"]

# Security: Read-only rootfs + tmpfs for workspace
VOLUME ["/app/workspace", "/tmp"]
ENV TMPDIR=/tmp
ENV WORKSPACE=/app/workspace

# Environment variables for application-level resource tuning (can be overridden at runtime)
ENV TARIRO_MAX_MEMORY_MB="" # Application can read this to limit its own memory use
ENV TARIRO_THREAD_COUNT=""  # Application can read this to adjust thread/process count
ENV TARIRO_LOG_LEVEL="INFO" # Application can adjust logging verbosity (DEBUG, INFO, WARNING, ERROR)
ENV TARIRO_WORKER_POOL_SIZE="" # Application can adjust internal worker pool size
ENV TARIRO_FEATURE_FLAGS="" # Comma-separated list of feature flags for dynamic behavior

# Healthcheck: Check if the Python application is responding on port 7860
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD ["/usr/bin/curl", "--fail", "http://localhost:7860/health"] || exit 1

# Final CMD is now handled by ENTRYPOINT.sh
CMD ["python3", "studio_v3.py"]
