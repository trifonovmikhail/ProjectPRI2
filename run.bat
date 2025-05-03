@echo off
echo [INFO] Checking virtual environment...

REM Check if .venv exists
IF NOT EXIST .venv (
    echo [INFO] Virtual environment not found. Creating...
    python -m venv .venv
)

REM Activate the virtual environment
echo [INFO] Activating .venv...
call .venv\Scripts\activate

REM Install dependencies
echo [INFO] Installing dependencies...
pip install --upgrade pip > nul
pip install -r requirements.txt

REM Run the FastAPI app
echo [INFO] Starting the app at http://127.0.0.1:8000 ...
uvicorn app.api:app --host 127.0.0.1 --port 8000

pause
