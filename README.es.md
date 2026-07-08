# 📈 Easy Finance

> **Motor de cálculo financiero determinista con asesoría inteligente basada en IA (RAG + Agentes)**

🌐 **[Read in English](README.md)**

Easy Finance es una aplicación full-stack para estudiantes, asesores y profesionales de las finanzas. Combina un **backend de cálculos exactos** (sin alucinaciones de IA) con un **asistente conversacional** que consulta documentación técnica y ejecuta operaciones matemáticas precisas como herramientas invocables.

La interfaz incluye un **selector de tema claro/oscuro** y un **toggle de idioma Español/Inglés**, disponibles desde la pantalla de acceso y desde la barra lateral.

---

## 📸 Capturas de Pantalla

| Conversión de Tasas (Claro · Español) | Tabla de Amortización (Oscuro · Español) |
|---|---|
| ![Conversión de tasas](frontend/assets/screenshots/01_tasas_light_es.png) | ![Tabla de amortización](frontend/assets/screenshots/02_amortizacion_dark_es.png) |

| Anualidades y Gradientes (Claro · Inglés) | Asistente IA (Claro · Español) |
|---|---|
| ![Anualidades](frontend/assets/screenshots/03_anualidades_light_en.png) | ![Asistente IA](frontend/assets/screenshots/04_chatbot_light_es.png) |

---

## 🚀 Funcionalidades

| Módulo | Descripción |
|--------|-------------|
| 🔄 **Conversión de Tasas** | Convierte entre tasas Nominales, Periódicas y Efectivas Anuales (EA) con fórmulas exactas |
| 📈 **Anualidades y Gradientes** | Calcula el valor presente y futuro de anualidades vencidas y anticipadas, y gradientes aritméticos y geométricos |
| 📊 **Tablas de Amortización** | Genera tablas de amortización completas bajo los sistemas Francés (cuota fija) y Alemán (abono fijo a capital) |
| 🤖 **Asistente IA (RAG)** | Asesor financiero que consulta documentación técnica (PDFs) y delega los cálculos exactos a herramientas deterministas |
| 🌓 **Modo Oscuro / Claro** | Cambio de tema instantáneo, persistido por sesión y aplicado de forma consistente en toda la app |
| 🌐 **Español / Inglés** | Traducción completa de la interfaz, incluyendo navegación, formularios y mensajes de resultado |

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
│   │   └── cashflows.py        # Orquestación de flujos de caja
│   ├── schemas.py              # Modelos Pydantic
│   └── main.py                 # Punto de entrada de FastAPI
│
├── frontend/                   # Interfaz de usuario con Streamlit
│   ├── app.py                  # Punto de entrada, control de acceso, toggles de tema/idioma
│   ├── auth.py                 # Autenticación de sesión
│   ├── utils.py                # Funciones de ayuda (CSS, sincronización de tema, footer)
│   ├── i18n.py                 # Diccionarios de traducción y helpers
│   ├── assets/                 # Recursos estáticos (logo, CSS, capturas)
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
│   └── docs/                   # PDFs de normatividad y referencia (en .gitignore)
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

> Credenciales de demo por defecto: `admin@riesgos.com` / `admin123` (autenticación simulada en `frontend/auth.py`; reemplázala por autenticación real antes de usar en producción).

---

## 🐳 Despliegue con Docker

```bash
docker-compose up --build
```

---

## 🌐 Despliegue en Render

El archivo `render.yaml` define dos servicios (backend y frontend).

1. Conecta tu repositorio en [Render](https://render.com/).
2. Ve a la pestaña **Environment** del servicio backend y agrega:
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

### Anualidades y Gradientes (Valor Presente)
| Instrumento | Fórmula |
|---|---|
| Anualidad Vencida | `VP = A * (1 - (1+i)^-n) / i` |
| Anualidad Anticipada | `VP = A * (1 - (1+i)^-n) / i * (1+i)` |
| Gradiente Aritmético | `VP = VP_anualidad + (G/i) * ((1-(1+i)^-n)/i - n/(1+i)^n)` |
| Gradiente Geométrico | `VP = A * (1 - ((1+j)/(1+i))^n) / (i - j)` |

El valor futuro de cualquier instrumento se obtiene como `VF = VP * (1+i)^n`.

### Amortización Francesa
- Cuota fija: `A = P * i(1+i)^n / ((1+i)^n - 1)`

### Amortización Alemana
- Cuota de capital fija: `K = P / n`

---

## 🌓 Tema y 🌐 Idioma

- Las preferencias de tema e idioma viven en `st.session_state` y se reaplican en cada página mediante `frontend/utils.py::load_css()`.
- El modo oscuro funciona marcando la raíz del documento con `data-theme` y alternando variables CSS definidas en `frontend/assets/style.css`.
- Las traducciones están centralizadas en `frontend/i18n.py`; las etiquetas de la interfaz usan `t(key)`, mientras que los valores de las opciones seleccionables conservan su identificador interno (en español) para que el contrato con el backend no cambie — solo se traduce la etiqueta visible mediante `opt(categoria, valor)`.

---

## 🔒 Seguridad

- El archivo `.env` está excluido del repositorio vía `.gitignore`.
- La carpeta `data/` (PDFs) y `ai_engine/rag/vectorstore/` (base de datos) son locales y no se suben al repositorio.
- El inicio de sesión incluido es una simulación de desarrollo — reemplaza `frontend/auth.py` con autenticación real antes de desplegar públicamente.

---

## 👤 Autor

**Faiber Andres Montes Gómez**
Proyecto de finanzas computacionales aplicadas con IA.

---

*Easy Finance — Cálculos exactos, asesoría inteligente.*
