#!/bin/bash

# Iniciar el Backend en segundo plano
uv run uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Iniciar el Frontend
uv run streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0
