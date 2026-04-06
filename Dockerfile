# Usamos una imagen de Python ligera
FROM python:3.11-slim

# Instalamos uv para manejar dependencias rápidamente
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY pyproject.toml uv.lock ./

# Instalar dependencias (sin instalar el proyecto como paquete)
RUN uv sync --frozen --no-cache

# Copiar el resto del código
COPY . .

# Exponer los puertos (8000 para FastAPI, 8501 para Streamlit)
EXPOSE 8000
EXPOSE 8501

# Script de inicio (lo crearemos a continuación)
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
