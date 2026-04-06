import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent import AgentExecutor
from langchain.agents.structured_chat.base import create_structured_chat_agent
from langchain.tools import StructuredTool 
from langchain import hub

from ai_engine.rag.retriever import FinancialRetriever
from ai_engine.agents.math_agent import MathAgent

load_dotenv()

class FinancialAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            temperature=0, 
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        self.retriever = FinancialRetriever()
        self.math = MathAgent()

        # 2. Definición de Herramientas con StructuredTool
        self.tools = [
            StructuredTool.from_function(
                name="Consultar_Base_Conocimiento",
                func=self.retriever.get_relevant_context,
                description="Busca definiciones técnicas y normatividad en los PDFs indexados. Entrada: una pregunta o término técnico."
            ),
            StructuredTool.from_function(
                name="Calculadora_Tasas",
                func=self.math.tool_convertir_tasa,
                description="""Convierte tasas de interés. 
                Argumentos obligatorios: 
                - tasa_origen (float): La tasa en decimal (ej: 0.20 para 20%). 
                - n (int): Número de períodos. 
                - tipo_origen (str): Ejemplo 'Nominal', 'Periódica' o 'Efectiva Anual (EA)'.
                - tipo_destino (str): Ejemplo 'Efectiva Anual (EA)'."""
            )
        ]

        self.prompt = hub.pull("hwchase17/structured-chat-agent")
        
        agent = create_structured_chat_agent(self.llm, self.tools, self.prompt)
        
        self.agent_executor = AgentExecutor(
            agent=agent, 
            tools=self.tools, 
            verbose=True, 
            handle_parsing_errors=True,
            max_iterations=5
        )

    def chat(self, user_input: str):
        instrucciones_personalidad = (
            "Eres Faiber Andres Montes Gómez, asesor financiero experto. "
            "Sé brutalmente honesto. Si el usuario pide un cálculo, extrae los parámetros "
            "y usa la Calculadora_Tasas. Si la tasa es porcentaje (ej: 20%), divídela por 100 para la herramienta."
        )
        
        try:
            response = self.agent_executor.invoke({
                "input": f"{instrucciones_personalidad}\nUsuario: {user_input}",
                "chat_history": []
            })
            return response["output"]
        except Exception as e:
            return f"Error técnico en el razonamiento: {str(e)}"

