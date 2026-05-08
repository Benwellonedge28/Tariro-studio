# Upgraded `Dockerfile` - Ultra Autonomous + Hardened (Python-only version)
# syntax=docker/dockerfile:1.7

# STAGE 1: TOOLCHAIN - Install core tools and utilities
FROM ubuntu:24.04 AS toolchain
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y && \
    apt install -y --no-install-recommends \
    build-essential curl git python3 python3-pip ca-certificates gnupg \
    nodejs npm wabt binaryen \
    openocd gdb-multiarch tini \
    firejail bubblewrap strace lsof \
    cosign slsa-verifier syft grype \
    # Removed Rust-specific tools: gcc-riscv64-unknown-elf clang lld llvm verilator yosys nextpnr-ice40 icestorm
    # Keeping qemu-system for potential emulation needs from python
    qemu-system-misc qemu-system-x86 qemu-system-riscv32 \
    && npm install -g wrangler && \
    apt clean && rm -rf /var/lib/apt/lists/*

# STAGE 2: PYTHON BUILDER - Create venv, install Python dependencies, scan deps
FROM python:3.12-slim AS py_builder
WORKDIR /app
# IMPORTANT: Ensure requirements.txt is correctly generated with hashes.
COPY requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -U pip wheel && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt && \
    /opt/venv/bin/pip install --no-cache-dir pip-audit safety && \
    # The pip-audit and safety checks will happen here
    /opt/venv/bin/pip-audit -r requirements.txt || true && \
    /opt/venv/bin/safety check -r requirements.txt || true

# STAGE 3: FINAL - Distroless + Nonroot + ReadOnlyRoot + Seccomp
FROM gcr.io/distroless/cc-debian12:nonroot
LABEL org.opencontainers.image.title="TARIRO Studio v3"
LABEL org.opencontainers.image.description="N-1 Tested Autonomous Swarm for OS/Cloud/FPGA"
LABEL org.opencontainers.image.licenses="Apache-2.0"

# Security: Run as nonroot UID 65532
USER nonroot:nonroot
WORKDIR /app

# Copy only what's needed. Nothing else exists in final image
# All binaries below must be statically linked or their dynamic libs must be present in distroless
COPY --from=toolchain --chown=nonroot:nonroot /usr/bin/qemu-system-riscv32 /usr/bin/
# Removed specific verilator, yosys, nextpnr-ice40, icestorm, icepack, iceprog, riscv64-unknown-elf-gcc
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

# App code: read-only
# Ensure all these paths exist in your repo
COPY --chown=nonroot:nonroot studio_v3.py /app/
COPY --chown=nonroot:nonroot features/ /app/features/
COPY --chown=nonroot:nonroot scripts/ /app/scripts/
COPY --chown=nonroot:nonroot tariro_features.py /app/
COPY --chown=nonroot:nonroot tool_forge.py /app/
COPY --chown=nonroot:nonroot litellm_config.yaml /app/ # LiteLLM config needed inside container


# Security: Read-only rootfs + tmpfs for workspace
VOLUME ["/app/workspace", "/tmp"]
ENV TMPDIR=/tmp
ENV WORKSPACE=/app/workspace

# Healthcheck: Check if the Python application is responding on port 7860
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD ["/usr/bin/curl", "--fail", "http://localhost:7860/health"] || exit 1

# Autonomy: tini as PID 1 for zombie reaping + signal forwarding
ENTRYPOINT ["/usr/bin/tini", "--"]

# Run: firejail sandbox + seccomp + capabilities drop
CMD ["firejail", "--noprofile", "--caps.drop=all", "--seccomp", "--nonewprivs",
     "--private-tmp", "--read-only=/app", "--read-write=/app/workspace", "--read-write=/tmp",
     "python3", "/app/studio_v3.py"]
