# Stage 1: Build Rust components and install non-Python tools
FROM ubuntu:24.04 AS toolchain
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y && \\
    apt install -y --no-install-recommends \\
    build-essential curl git python3 python3-pip \\
    qemu-system-misc qemu-system-x86 verilator yosys \\
    gcc-riscv64-unknown-elf nodejs npm wabt binaryen \\
    openocd gdb-multiarch && \\
    npm install -g wrangler && \\
    apt clean && rm -rf /var/lib/apt/lists/*

FROM rust:1.80 AS rust_builder
WORKDIR /app
COPY . .
RUN cargo build --release --locked

# Stage 2: Prepare Python environment and final application image
# Using a slim Python base image for reduced size and attack surface
FROM python:3.11-slim-bookworm AS python_env
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

# Install common system dependencies needed for Python packages and runtime
RUN apt update && apt upgrade -y && \\
    apt install -y --no-install-recommends \\
    git curl \
    # Add any other core dependencies for your Python packages here if needed, e.g., libpq-dev for psycopg2
    # gh CLI is used in the original Dockerfile, keeping it here as it might be used by the studio itself
    gh \
    && apt clean && rm -rf /var/lib/apt/lists/*

# Create a dedicated non-root user for security
RUN groupadd --system tariro && useradd --system --gid tariro tariro
# Ensure write access for the workspace volume, owned by the tariro user
RUN mkdir -p /app/workspace && chown -R tariro:tariro /app/workspace

WORKDIR /app

# Copy requirements.txt and install Python dependencies as the non-root user
COPY requirements.txt .
USER tariro
RUN pip install --no-cache-dir -r requirements.txt

# Switch back to root temporarily for copying built artifacts and toolchains
USER root
COPY --from=toolchain /usr/bin/qemu-system-* /usr/bin/
COPY --from=toolchain /usr/bin/verilator /usr/bin/
COPY --from=toolchain /usr/bin/yosys /usr/bin/
COPY --from=toolchain /usr/bin/riscv64-* /usr/bin/
COPY --from=rust_builder /app/target/release/studio /usr/bin/tariro-studio

# Copy application code, ensuring non-root ownership
COPY --chown=tariro:tariro studio_v3.py /app/
COPY --chown=tariro:tariro scripts/ /app/scripts/
COPY --chown=tariro:tariro features/ /app/features/
COPY --chown=tariro:tariro tariro_features.py /app/
COPY --chown=tariro:tariro tool_forge.py /app/

# Set up the toolchains directory. This will be mounted from the host.
# We ensure the tariro user can access it.
RUN mkdir -p /toolchains && chown -R tariro:tariro /toolchains

# Expose the port the application listens on
EXPOSE 7860

# HEALTHCHECK instruction to allow Docker/orchestrator to verify container health
# Assumes studio_v3.py will serve a health endpoint on /health
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \\
  CMD curl --fail http://localhost:7860/health || exit 1

# Switch to the non-root user for running the application
USER tariro

ENV PATH="/toolchains/bin:$PATH"
CMD ["python3", "studio_v3.py"]