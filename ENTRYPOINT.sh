#!/bin/sh
set -e

echo "TARIRO Studio v4 booting..."

# Optionally start Ollama if available (non-blocking, non-fatal)
if command -v ollama > /dev/null 2>&1; then
    echo "Starting Ollama in background..."
    ollama serve &
    sleep 3
    ollama pull qwen2.5-coder:7b &
else
    echo "[INFO] Ollama not found - skipping. Set OPENAI_API_BASE to use an external LLM endpoint."
fi

echo "Starting Tariro Studio v4 (AutonomyRuntime)..."
exec python3 /app/app.py
