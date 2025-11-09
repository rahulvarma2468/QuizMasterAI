@echo off
echo ========================================
echo AI Wiki Quiz Generator - Frontend Startup
echo ========================================
echo.

cd /d "%~dp0frontend"

echo Starting frontend development server...
echo Frontend will be available at: http://localhost:5173
echo Press Ctrl+C to stop the server
echo.

npm run dev