# Matar procesos previos para evitar conflictos de puerto
stop-process -name python -force -ErrorAction SilentlyContinue

Write-Host "--- Iniciando Backend FastAPI ---" -ForegroundColor Cyan
Start-Process -NoNewWindow -FilePath "uv" -ArgumentList "run", "python", "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"

Write-Host "--- Iniciando Frontend Streamlit ---" -ForegroundColor Green
Start-Process -NoNewWindow -FilePath "uv" -ArgumentList "run", "python", "-m", "streamlit", "run", "frontend/app.py", "--server.port", "8501"

Write-Host "Sistemas activos. Backend en :8000, Frontend en :8501" -ForegroundColor Yellow
