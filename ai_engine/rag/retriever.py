import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

# Carga las variables del archivo .env que está en la raíz
load_dotenv()

class FinancialRetriever:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        persist_path = os.path.join(base_path, "vectorstore/db")
        
        # Debe ser el mismo modelo usado en ingest.py
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        self.vector_db = Chroma(
            persist_directory=persist_path, 
            embedding_function=self.embeddings
        )

    def get_relevant_context(self, query: str):
        """Busca los 3 fragmentos más honestos y realistas del PDF."""
        docs = self.vector_db.similarity_search(query, k=3)
        return "\n---\n".join([d.page_content for d in docs])

if __name__ == "__main__":
    # Prueba rápida de búsqueda
    searcher = FinancialRetriever()
    print(searcher.get_relevant_context("¿Qué es una tasa nominal?"))

