@echo off
echo ========================================
echo AI Wiki Quiz Generator - Backend Startup
echo ========================================
echo.

cd /d "%~dp0backend"

echo Checking environment variables...
if not exist .env (
    echo ERROR: .env file not found!
    echo Please create backend/.env with DATABASE_URL and GEMINI_API_KEY
    pause
    exit /b 1
)

echo.
echo Initializing database...
"%~dp0.venv\Scripts\python.exe" init_db.py
if errorlevel 1 (
    echo.
    echo ERROR: Database initialization failed!
    echo Please ensure PostgreSQL is installed and running.
    echo.
    pause
    exit /b 1
)

echo.
echo Starting backend server...
echo Backend will be available at: http://localhost:8000
echo API documentation at: http://localhost:8000/docs
echo Press Ctrl+C to stop the server
echo.

"%~dp0.venv\Scripts\python.exe" -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload