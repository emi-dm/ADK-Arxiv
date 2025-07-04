from re import I
from agents import Agent, Runner
from agents.tool import function_tool
from typing import List, Optional
import datetime
from pathlib import Path
from pydantic import BaseModel
import asyncio
from agents.extensions.models.litellm_model import LitellmModel
from agents.tracing import set_tracing_disabled
from agents.mcp.server import MCPServerStreamableHttp, MCPServerStreamableHttpParams
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled(True)

MODEL = "gemini-2.0-flash-lite"
model=LitellmModel(model="gemini/" + MODEL)



from agents import repl

async def main():
    class Paper(BaseModel):
        title: str
        authors: list[str]
        summary: str
        pdf_url: str
        published_date: str

    @function_tool
    def save_papers_to_markdown(papers: list[Paper], filename: str = "") -> str:
        """
        Guarda una lista de papers en un archivo markdown sencillo.
        Args:
            papers: Lista de objetos Paper.
            filename: Nombre opcional para el archivo markdown.
        Returns:
            str: Ruta al archivo markdown guardado
        """
        if not filename.endswith('.md'):
            filename += '.md'
        papers_dir = Path("papers")
        papers_dir.mkdir(exist_ok=True)
        filepath = papers_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Papers\n\nGenerado: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n")
            for i, paper in enumerate(papers, 1):
                f.write(f"## {i}. {paper.title}\n")
                f.write(f"**Autores:** {', '.join(paper.authors)}\n")
                f.write(f"**Publicado:** {paper.published_date}\n")
                f.write(f"**URL:** {paper.pdf_url}\n")
                f.write(f"**Resumen:** {paper.summary}\n\n---\n\n")
        return str(filepath)

    # Configuración del MCP Server HTTP para ArXiv
    arxiv_mcp_server = MCPServerStreamableHttp(
        MCPServerStreamableHttpParams(
            url="https://arxiv-mcp-sq0a.onrender.com/mcp",
            timeout=65,
        )
    )

    await arxiv_mcp_server.connect()


    saver_agent = Agent(
        name="saver_agent",
        model=model,
        instructions="Eres un agente que guarda papers en un archivo markdown.",
        tools=[save_papers_to_markdown],
    )

    # Definición del agente principal usando OpenAI Agents SDK
    research_assistant_agent = Agent(
        name="research_assistant_agent_openai",
        model=model,
        instructions=(
            "Eres un asistente de investigación avanzado especializado en descubrimiento, análisis y organización de papers académicos con memoria de sesión. "
            "Tus responsabilidades principales incluyen:\n\n"
            "## Funciones principales:\n"
            "1. Descubrir papers relevantes según consultas, temas o áreas de investigación\n"
            "2. Analizar y resumir papers, identificando contribuciones clave, metodologías y hallazgos\n"
            "3. Organizar y categorizar papers por tema, relevancia o líneas de investigación\n"
            "4. Apoyar revisiones de literatura e identificar vacíos de investigación\n"
            "5. Gestionar citas y referencias\n"
            "6. Mantener memoria de sesión sobre búsquedas y temas tratados\n\n"
            "## Capacidades clave:\n"
            "- Buscar papers en ArXiv por palabras clave, autores, categorías o criterios específicos\n"
            "- Extraer y resumir información clave de papers\n"
            "- Identificar relaciones entre papers y temas\n"
            "- Generar listas de lectura estructuradas\n"
            "- Crear documentos markdown con los papers recopilados\n"
            "- Mantener contexto de investigación y construir sobre búsquedas previas\n"
            "- Sugerir próximos pasos según el historial de sesión\n\n"
            "## Memoria de sesión:\n"
            "- Recordar papers ya discutidos\n"
            "- Rastrear temas explorados\n"
            "- Construir sobre búsquedas previas\n"
            "- Mantener contexto de intereses\n\n"
            "## Buenas prácticas:\n"
            "- Explica siempre tu estrategia de búsqueda\n"
            "- Incluye metadatos relevantes (autores, fechas, categorías)\n"
            "- Incluye siempre la URL de cada paper\n"
            "- No modifiques el contenido devuelto por la herramienta de papers\n"
            "- Al guardar en markdown, pasa la respuesta cruda a save_papers_to_markdown\n"
            "- Sugiere términos o áreas relacionadas\n"
            "- Organiza la información de forma clara\n"
            "- Ofrece guardar colecciones en markdown\n"
            "- Usa el contexto de sesión para recomendaciones personalizadas\n"
            "- Reconoce si construyes sobre búsquedas previas\n"
        ),
        tools=[
            saver_agent.as_tool(
                tool_name="save_papers_to_markdown",
                tool_description="Guarda papers en un archivo markdown.",
            ),
        ],
        mcp_servers=[arxiv_mcp_server],
    )
    await repl.run_demo_loop(research_assistant_agent)

if __name__ == "__main__":
    asyncio.run(main())
