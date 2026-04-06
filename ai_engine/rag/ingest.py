import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

# Carga las variables del archivo .env que está en la raíz
load_dotenv()

def process_financial_docs():
    # 1. Rutas de configuración
    base_path = os.path.dirname(os.path.abspath(__file__))
    docs_path = os.path.join(base_path, "../../data/docs")
    persist_path = os.path.join(base_path, "vectorstore/db")
    
    # 2. Cargar API KEY de Google (Asegúrate de tenerla en tus variables de entorno)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY no encontrada. Configúrala en tu terminal.")

    # 3. Cargar documentos
    if not os.path.exists(docs_path) or not os.listdir(docs_path):
        print(f"Error: No hay archivos PDF en {docs_path}")
        return

    loader = DirectoryLoader(docs_path, glob="./*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    
    # 4. Splitting Estratégico
    # Para finanzas, usamos un chunk_size moderado para no romper fórmulas
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    texts = text_splitter.split_documents(documents)
    
    # 5. Generar Embeddings de Google
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    
    # 6. Crear y persistir VectorStore
    vector_db = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=persist_path
    )
    
    print(f"--- Proceso Finalizado ---")
    print(f"Documentos procesados: {len(documents)}")
    print(f"Fragmentos indexados: {len(texts)}")
    print(f"Base de datos guardada en: {persist_path}")

if __name__ == "__main__":
    process_financial_docs()

