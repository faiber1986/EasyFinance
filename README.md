# 📈 Easy Finance

> **Motor de cálculo financiero determinista con asesoría inteligente basada en IA (RAG + Agentes)**

Easy Finance es una aplicación full-stack diseñada para estudiantes, asesores y profesionales de las finanzas. Combina un **backend de cálculos exactos** (sin alucinaciones de IA) con un **asistente conversacional** que consulta documentación técnica y ejecuta operaciones matemáticas de forma precisa.

---

## 🚀 Funcionalidades

| Módulo | Descripción |
|--------|-------------|
| 🔄 **Conversión de Tasas** | Convierte entre tasas Nominales, Periódicas y Efectivas Anuales (EA) con fórmulas exactas |
| 📈 **Anualidades y Gradientes** | Calcula el valor presente y futuro de anualidades ordinarias, anticipadas, gradientes aritméticos y geométricos |
| 📊 **Tablas de Amortización** | Genera tablas de amortización completas bajo los sistemas Francés y Alemán |
| 🤖 **Asistente IA (RAG)** | Asesor financiero inteligente que consulta documentación técnica (PDFs) y ejecuta cálculos deterministas mediante herramientas |

---

## 🏗️ Arquitectura

```
Easy Finance/
├── backend/                    # API REST con FastAPI
│   ├── api/                    # Endpoints por módulo
│   │   ├── tasas.py
│   │   ├── amortizacion.py
│   │   ├── anualidades.py
│   │   └── chatbot.py          # Endpoint del agente IA
│   ├── core/                   # Lógica financiera determinista (sin IA)
│   │   ├── interest.py         # Conversión de tasas
│   │   ├── amortization.py     # Tablas de amortización
│   │   ├── annuities.py        # Anualidades
│   │   ├── gradients.py        # Gradientes
│   │   └── cashflows.py        # Flujos de caja
│   ├── schemas.py              # Modelos Pydantic
│   └── main.py                 # Punto de entrada de FastAPI
│
├── frontend/                   # Interfaz de usuario con Streamlit
│   ├── app.py                  # Punto de entrada principal
│   ├── auth.py                 # Autenticación de sesión
│   ├── utils.py                # Funciones de ayuda (CSS, footer)
│   ├── assets/                 # Recursos estáticos (logo, CSS)
│   └── modulos/                # Páginas de la aplicación
│       ├── 1_tasas.py
│       ├── 2_anualidades.py
│       ├── 3_amortizacion.py
│       └── 4_chatbot_rag.py
│
├── ai_engine/                  # Motor de Inteligencia Artificial
│   ├── agents/
│   │   ├── financial_agent.py  # Agente LangChain con herramientas
│   │   └── math_agent.py       # Herramientas de cálculo determinista
│   └── rag/
│       ├── ingest.py           # Indexación de PDFs → ChromaDB
│       ├── retriever.py        # Búsqueda semántica
│       └── vectorstore/        # Base de datos vectorial (local, en .gitignore)
│
├── data/
│   └── docs/                   # PDFs de normatividad y libros (en .gitignore)
│
├── Dockerfile
├── docker-compose.yml
├── render.yaml                 # Configuración de despliegue en Render
├── pyproject.toml
└── .env                        # Variables de entorno (en .gitignore)
```

---

## ⚙️ Tecnologías

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/)
- **Frontend**: [Streamlit](https://streamlit.io/)
- **IA / LLM**: [Gemini](https://ai.google.dev/) vía `langchain-google-genai`
- **Agente**: [LangChain](https://www.langchain.com/) — `AgentExecutor` con `StructuredTool`
- **RAG**: [ChromaDB](https://www.trychroma.com/) + `GoogleGenerativeAIEmbeddings`
- **Gestión de entorno**: [uv](https://github.com/astral-sh/uv)
- **Despliegue**: Docker / [Render](https://render.com/)

---

## 📦 Instalación Local

### Requisitos previos
- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) instalado
- Una **Google API Key** (obtenla gratis en [Google AI Studio](https://aistudio.google.com/app/apikey))

### Pasos

**1. Clona el repositorio e instala dependencias:**
```bash
git clone <url-del-repositorio>
cd easy-finance
uv sync --link-mode=copy
```

**2. Configura las variables de entorno:**
```bash
# Crea el archivo .env en la raíz del proyecto
cp .env.example .env
```
Edita el archivo `.env` y agrega tu llave:
```env
GOOGLE_API_KEY=tu_api_key_aqui
```

**3. (Opcional) Indexa tus documentos PDF:**

Coloca los archivos PDF en la carpeta `data/docs/` y ejecuta:
```bash
uv run python ai_engine/rag/ingest.py
```
Esto procesará los PDFs y creará la base de datos vectorial en `ai_engine/rag/vectorstore/`.

---

## ▶️ Ejecución

### Opción A — Script automático (Windows)
```powershell
.\run_app.ps1
```

### Opción B — Manual (dos terminales)

**Terminal 1 — Backend (FastAPI):**
```bash
uv run python -m uvicorn backend.main:app --reload
```
API disponible en: `http://127.0.0.1:8000`
Documentación interactiva: `http://127.0.0.1:8000/docs`

**Terminal 2 — Frontend (Streamlit):**
```bash
cd frontend
uv run python -m streamlit run app.py
```
App disponible en: `http://localhost:8501`

---

## 🐳 Despliegue con Docker

```bash
docker-compose up --build
```

---

## 🌐 Despliegue en Render

El archivo `render.yaml` define dos servicios (backend y frontend). 

1. Conecta tu repositorio en [Render](https://render.com/).
2. Ve a **Environment** del servicio backend y agrega la variable:
   - `GOOGLE_API_KEY` → tu llave de Google AI.
3. Render detectará el `render.yaml` y desplegará ambos servicios automáticamente.

---

## 📐 Fórmulas Implementadas

### Conversión de Tasas
| Conversión | Fórmula |
|---|---|
| Nominal → EA | `EA = (1 + i_nom/n)^n - 1` |
| Periódica → EA | `EA = (1 + i_per)^n - 1` |
| EA → Nominal | `i_nom = n * ((1 + EA)^(1/n) - 1)` |
| EA → Periódica | `i_per = (1 + EA)^(1/n) - 1` |

### Amortización Francesa
- Cuota fija: `C = P * i / (1 - (1+i)^-n)`

### Amortización Alemana
- Cuota de capital fija: `K = P / n`

---

## 🔒 Seguridad

- El archivo `.env` está excluido del repositorio vía `.gitignore`.
- La carpeta `data/` (PDFs) y `ai_engine/rag/vectorstore/` (base de datos) son locales y no se suben al repositorio.

---

## 👤 Autor

**Faiber Andres Montes Gómez**  
Proyecto de finanzas computacionales aplicadas con IA.

---

*Easy Finance — Cálculos exactos, asesoría inteligente.*
