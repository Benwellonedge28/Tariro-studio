#!/bin/sh
set -e

echo "TARIRO Studio booting..."

# Start Ollama in the background
ollama serve &

# Wait for Ollama to be ready
echo "Waiting for Ollama to start..."
until ollama list >/dev/null 2>&1; do
    echo "Ollama not ready, waiting 1 second..."
    sleep 1
done
echo "Ollama is ready."

# Pull specified models (non-blocking)
echo "Pulling Ollama models in background..."
ollama pull qwen2.5-coder:7b &
ollama pull qwen2.5-coder:32b &
wait # Wait for background pulls to complete if you want them before the main app starts

echo "Starting TARIRO Studio with firejail sandbox..."

# Execute the main application with firejail
exec firejail --noprofile --caps.drop=all --seccomp --nonewprivs \
     --private-tmp --read-only=/app --read-write=/app/workspace --read-write=/tmp \
     python3 /app/studio_v3.py
