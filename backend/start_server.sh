#!/usr/bin/env bash
# Simple startup script to help debug runtime issues in container
set -e
echo "=== Runtime debug info ==="
echo "Python: $(python --version 2>&1)"
echo "Pip: $(python -m pip --version 2>&1)"
echo "Listing installed packages (top 30 lines):"
python -m pip freeze | head -n 30 || true
echo "Checking uvicorn availability..."
if python -c "import uvicorn" 2>/dev/null; then
  echo "uvicorn import OK"
else
  echo "uvicorn import FAILED"
fi

echo "Running server using: python -m uvicorn main:app --host 0.0.0.0 --port $PORT"
exec python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
