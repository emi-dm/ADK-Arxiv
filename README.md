# Multi Tool Agent

This project implements an intelligent Python agent focused on research assistance. It is capable of searching and retrieving scientific papers from arXiv.

## Main Features
- **Arxiv MCP integration**: Incorporates a Model Context Protocol (MCP) tool for searching and retrieving scientific papers from arXiv, enabling the agent to answer research-related queries.
- **Extensible agent**: Based on Google ADK, you can easily add new tools or models.
- **Modular code**: Main functions are in `multi_tool_agent/agent.py`.

## Project Structure
- `multi_tool_agent/agent.py`: Contains the main functions and agent definition.
- `multi_tool_agent/__init__.py`: Initializes the module.

## Requirements
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (required for fast and reliable dependency management)
- [Ollama](https://ollama.com/) (required to run the local LLM)
- Ollama model: `qwen3:8b` (must be pulled with `ollama pull qwen3:8b`)
- Packages: `httpx`, `geopy`, `google-adk` (and ADK dependencies)

## Installation
1. Install [uv](https://github.com/astral-sh/uv) if you don't have it:
   ```bash
   pip install uv
   ```
2. Install project dependencies using uv:
   ```bash
   uv pip install -r requirements.txt
   # or, for a quick setup:
   uv pip install httpx geopy google-adk
   ```
3. (Optional) Set up your virtual environment.
4. Install [Ollama](https://ollama.com/) and pull the required model:
   ```bash
   # Install Ollama (see https://ollama.com/download)
   ollama pull qwen3:8b
   ```

## Configuration
To ensure all dependencies are up to date and properly installed, run:
```bash
uv sync
```

### .env file configuration
Create a `.env` file in the project root to store environment variables. Example:
```env
# Example .env file
# Set your Google API key if required by google-adk or other services
GOOGLE_API_KEY=your_google_api_key_here

# Ollama API base URL (required if using Ollama locally)
OLLAMA_API_BASE="http://localhost:11434"

# Set other environment variables as needed by your project
```
- If you use Ollama locally, make sure to set `OLLAMA_API_BASE` as shown above.
- If you use any API keys or secrets, add them here and never commit your `.env` file to version control.
- The project will automatically load variables from `.env` if you use packages like `python-dotenv`.

## Usage
- Ollama and the `qwen3:8b` model must be running locally for the agent to work.
- If the city is not found or the API does not respond, a friendly error message is returned.
- If you need to use API keys, set them in the `.env` file as shown above.
- **To run the project, execute:**
  ```bash
  adk web
  ```
  from the root folder. This will start the ADK web server for your agent.

## License
MIT

---
**Author:** [emi-dm](https://emi-dm.github.io/)
