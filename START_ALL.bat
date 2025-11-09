@echo off
echo ========================================
echo  AI Wiki Quiz Generator - Full Startup
echo ========================================
echo.
echo Starting Backend Server...
start "Backend Server" cmd /k "cd /d %~dp0backend && %~dp0.venv\Scripts\python.exe -m uvicorn main:app --reload --port 8000"

timeout /t 3 /nobreak >nul

echo Starting Frontend Server...
start "Frontend Server" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo ========================================
echo Both servers are starting in separate windows!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173 (or 5174 if 5173 is busy)
echo API Docs: http://localhost:8000/docs
echo.
echo Close this window or press any key to exit...
pause >nul
