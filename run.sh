#!/bin/bash

echo "[INFO] Checking virtual environment..."

# Check if .venv exists
if [ ! -d ".venv" ]; then
    echo "[INFO] Virtual environment not found. Creating..."
    python3 -m venv .venv
fi

# Activate the virtual environment
echo "[INFO] Activating .venv..."
source .venv/bin/activate

# Install dependencies
echo "[INFO] Installing dependencies..."
pip install --upgrade pip >/dev/null
pip install -r requirements.txt

# Run the FastAPI app
echo "[INFO] Starting the app at http://127.0.0.1:8000 ..."
uvicorn app.api:app --host 127.0.0.1 --port 8000
