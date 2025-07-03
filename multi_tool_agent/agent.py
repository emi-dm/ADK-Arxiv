from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
import os
import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Paper(BaseModel):
    title: str
    authors: str
    abstract: str
    pdf_url: str
    published: str
    categories: str

def dict_to_paper(d):
    return Paper(
        title=d.get("title", "") or "",
        authors=d.get("authors", "") or "",
        abstract=d.get("abstract", d.get("summary", "")) or "",
        pdf_url=d.get("pdf_url", d.get("url", "")) or "",
        published=d.get("published", d.get("published_date", "")) or "",
        categories=d.get("categories", "") or ""
    )

def save_papers_to_markdown(papers: List[Paper], filename: Optional[str] = None) -> str:
    """
    Tool to save a list of papers extracted from ArXiv MCP to a markdown file.
    
    Args:
        papers: List of Paper objects containing title, authors, abstract, etc.
        filename: Optional filename for the markdown file
    
    Returns:
        str: Path to the saved markdown file
    """
    # Conversión automática de dict a Paper si es necesario, con mapeo flexible
    papers = [dict_to_paper(p) if isinstance(p, dict) else p for p in papers]
    if filename is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"research_papers_{timestamp}.md"
    if not filename.endswith('.md'):
        filename += '.md'
    papers_dir = Path("papers")
    papers_dir.mkdir(exist_ok=True)
    filepath = papers_dir / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("# Research Papers Collection\n\n")
        f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        for i, paper in enumerate(papers, 1):
            f.write(f"## {i}. {paper.title}\n\n")
            f.write(f"**Authors:** {paper.authors}\n\n")
            f.write(f"**Published:** {paper.published}\n\n")
            f.write(f"**Categories:** {paper.categories}\n\n")
            if paper.pdf_url:
                f.write(f"**URL:** [{paper.pdf_url}]({paper.pdf_url})\n\n")
            f.write(f"**Abstract:**\n{paper.abstract}\n\n")
            f.write("---\n\n")
    return str(filepath)


# Configuración de herramientas MCP para ArXiv
arxiv_mcp_tool = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://arxiv-mcp-sq0a.onrender.com/mcp",
    )
)

MODEL = "qwen3:14b-q4_K_M"
GOOGLE_MODEL = "gemini-2.0-flash"
# Subagente especializado en guardar papers
saver_agent = Agent(
    name="saver_agent",
    model=GOOGLE_MODEL,# LiteLlm(model="ollama_chat/" + MODEL),
    description="Agente especializado en guardar colecciones de papers en archivos markdown organizados.",
    instruction=(
        "Eres un agente experto en organización y archivo de papers académicos. "
        "Tu función principal es recibir una lista de papers y guardarla en un archivo markdown estructurado, usando la herramienta save_papers_to_markdown. "
        "No realices búsquedas ni análisis, solo archiva y organiza la información recibida."
    ),
    tools=[save_papers_to_markdown],
)

# Agente principal con delegación al subagente
root_agent = Agent(
    name="research_assistant_agent",
    model=GOOGLE_MODEL,  # LiteLlm(model="ollama_chat/" + MODEL),
    description=(
        "Agente principal de investigación académica que coordina un equipo. Tu responsabilidad principal es proporcionar información y análisis sobre papers académicos."
    ),
    instruction=(
        "Eres el agente principal de investigación académica coordinando un equipo. Tu responsabilidad principal es proporcionar información y análisis sobre papers académicos. "
        "Utiliza la herramienta de búsqueda de ArXiv SOLO para solicitudes específicas de papers o temas de investigación. "
        "Tienes un sub-agente especializado: "
        "1. 'saver_agent': Se encarga de guardar colecciones de papers en markdown. Delega en él cuando el usuario solicite guardar, archivar o exportar papers. "
        "Analiza la consulta del usuario. Si es una solicitud de guardado/exportación, delega en 'saver_agent'. "
        "Si es una búsqueda o análisis de papers, manéjalo tú mismo usando la herramienta de ArXiv. "
        "Para cualquier otra cosa, responde apropiadamente o indica que no puedes manejarlo."
    ),
    tools=[arxiv_mcp_tool],
    sub_agents=[saver_agent],
)