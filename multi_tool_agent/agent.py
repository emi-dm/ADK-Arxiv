from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
import os
import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional


def save_papers_to_markdown(papers: List[Dict[str, Any]], filename: Optional[str] = None) -> str:
    """
    Tool to save a list of papers extracted from ArXiv MCP to a markdown file.
    
    Args:
        papers: List of paper dictionaries containing title, authors, abstract, etc.
        filename: Optional filename for the markdown file
    
    Returns:
        str: Path to the saved markdown file
    """
    # Validación estricta del input
    required_fields = {"title", "authors", "abstract", "url", "published", "categories"}
    if not isinstance(papers, list) or not all(isinstance(p, dict) for p in papers):
        raise ValueError("El parámetro 'papers' debe ser una lista de diccionarios.")
    for p in papers:
        if not required_fields.issubset(p.keys()):
            raise ValueError(
                f"Cada paper debe contener los campos: {', '.join(required_fields)}. Faltan en: {p}"
            )
    
    if filename is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"research_papers_{timestamp}.md"
    
    # Ensure the filename has .md extension
    if not filename.endswith('.md'):
        filename += '.md'
    
    # Create papers directory if it doesn't exist
    papers_dir = Path("papers")
    papers_dir.mkdir(exist_ok=True)
    
    filepath = papers_dir / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("# Research Papers Collection\n\n")
        f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        
        for i, paper in enumerate(papers, 1):
            # Extract paper information
            title = paper.get('title', 'Unknown Title')
            authors = paper.get('authors', 'Unknown Authors')
            abstract = paper.get('abstract', 'No abstract available')
            url = paper.get('url', '')
            published = paper.get('published', 'Unknown Date')
            categories = paper.get('categories', 'Unknown Category')
            
            # Write paper section
            f.write(f"## {i}. {title}\n\n")
            f.write(f"**Authors:** {authors}\n\n")
            f.write(f"**Published:** {published}\n\n")
            f.write(f"**Categories:** {categories}\n\n")
            
            if url:
                f.write(f"**URL:** [{url}]({url})\n\n")
            
            f.write(f"**Abstract:**\n{abstract}\n\n")
            f.write("---\n\n")
    
    return str(filepath)


# Configuración de herramientas MCP para ArXiv
arxiv_mcp_tool = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://arxiv-mcp-sq0a.onrender.com/mcp",
    )
)

MODEL_QWEN = "qwen3:8b"

root_agent = Agent(
    name="research_assistant_agent",
    model=LiteLlm(model="ollama_chat/" + MODEL_QWEN),
    description=(
        "Advanced AI research assistant specialized in academic paper discovery, analysis, and organization with session memory."
    ),
    instruction=(
        "You are an expert research assistant with access to ArXiv papers and session memory capabilities. Your primary responsibilities include:\n\n"
        "## Core Functions:\n"
        "1. **Paper Discovery**: Search for relevant academic papers based on user queries, topics, or research areas\n"
        "2. **Paper Analysis**: Analyze and summarize research papers, identifying key contributions, methodologies, and findings\n"
        "3. **Research Organization**: Help organize and categorize papers by topic, relevance, or research themes\n"
        "4. **Literature Review Support**: Assist in conducting comprehensive literature reviews and identifying research gaps\n"
        "5. **Citation and Reference Management**: Help format citations and manage bibliographic information\n"
        "6. **Session Continuity**: Remember previous searches, papers discussed, and research topics within the current session\n\n"
        "## Key Capabilities:\n"
        "- Search ArXiv database for papers using keywords, authors, categories, or specific criteria\n"
        "- Extract and summarize key information from academic papers\n"
        "- Identify relationships between different research papers and topics\n"
        "- Generate comprehensive reading lists for specific research areas\n"
        "- Create structured markdown documents with collected papers for easy reference\n"
        "- Maintain research context and build upon previous searches in the session\n"
        "- Track research progress and suggest next steps based on session history\n\n"
        "## Session Memory Features:\n"
        "- Remember papers already discussed to avoid repetition\n"
        "- Track research themes and topics explored in the current session\n"
        "- Build upon previous searches to provide more targeted recommendations\n"
        "- Maintain a running context of the user's research interests\n\n"
        "## Best Practices:\n"
        "- Always provide detailed explanations of your search strategies\n"
        "- Include relevant metadata (authors, publication dates, categories) in your responses\n"
        "- Always include the URL of each paper extracted from the MCP tool in your responses, unless it is not available.\n"
        "- Never summarize or modify the content returned by the MCP tool. Always display the full content exactly as received, including all available fields.\n"
        "- When saving papers to markdown, always pass the raw, unmodified response from the MCP tool directly to the save_papers_to_markdown function. Never generate or invent paper data yourself.\n"
        "- Reference previous papers or searches when relevant to the current query\n"
        "- Suggest related search terms or areas when appropriate\n"
        "- Organize information in a clear, hierarchical structure\n"
        "- Offer to save collections of papers to markdown files for future reference\n"
        "- Use session context to provide more personalized and relevant recommendations\n\n"
        "When a user requests paper searches or research assistance, be thorough in your approach, leverage session memory "
        "to provide contextual responses, and offer to save the results in an organized markdown format for easy access and reference. "
        "Always acknowledge if you're building upon previous searches or referencing papers from earlier in the session."
    ),
    tools=[arxiv_mcp_tool, save_papers_to_markdown],
)