@echo off
echo ===================================================
echo   Starting Smart Waste Management Assistant
echo ===================================================
echo.

echo Launching FastAPI backend server (Port 8000)...
start "FastAPI Backend" cmd /k "python -m uvicorn backend.main:app --reload --port 8000"

echo Waiting for backend server startup...
timeout /t 3 /nobreak > nul

echo Launching Streamlit frontend server (Port 8501)...
start "Streamlit Frontend" cmd /k "python -m streamlit run frontend/app.py"

echo.
echo Services started successfully!
echo - Streamlit UI: http://localhost:8501
echo - FastAPI Docs: http://127.0.0.1:8000/docs
echo.
pause
