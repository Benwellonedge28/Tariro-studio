FROM ubuntu:24.04 AS toolchain
RUN apt update && apt install -y \
    build-essential curl git python3 python3-pip \
    qemu-system-misc qemu-system-x86 verilator yosys \
    gcc-riscv64-unknown-elf nodejs npm wabt binaryen \
    openocd gdb-multiarch && \
    npm install -g wrangler

FROM rust:1.80 AS builder
WORKDIR /app
COPY .
RUN cargo build --release

FROM ubuntu:24.04
RUN apt update && apt install -y python3 python3-pip git gh && \
    pip3 install --break-system-packages gradio openai autogen-agentchat \
    gitpython qdrant-client httpx apscheduler redis && \
    mkdir -p /toolchains

COPY --from=toolchain /usr/bin/qemu-system-* /usr/bin/
COPY --from=toolchain /usr/bin/verilator /usr/bin/
COPY --from=toolchain /usr/bin/yosys /usr/bin/
COPY --from=toolchain /usr/bin/riscv64-* /usr/bin/
COPY --from=builder /app/target/release/studio /usr/bin/tariro-studio
COPY studio_v3.py /app/studio_v3.py
COPY scripts/ /app/scripts/

WORKDIR /app
ENV PATH="/toolchains/bin:$PATH"
CMD ["python3", "studio_v3.py"]