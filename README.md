# Multi Tool Agent

This project implements an intelligent Python agent capable of answering questions about the weather and current time in any city worldwide.

## Main Features
- **Weather lookup**: Uses the public [Open-Meteo API](https://open-meteo.com/) to get the current weather for any city, first geolocating the city name.
- **Time lookup**: Gets the local time for any city using geolocation and the Open-Meteo API to determine the timezone.
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
You can import and use the agent in your own Python code, or extend it with new tools.

Example usage of the main functions:
```python
from multi_tool_agent.agent import get_weather, get_current_time
import asyncio

# Get weather (must be called with await if async)
result = asyncio.run(get_weather("Buenos Aires"))
print(result)

# Get local time
result = asyncio.run(get_current_time("Madrid"))
print(result)
```

## Notes
- The agent uses geolocation, so it requires an Internet connection.
- Ollama and the `qwen3:8b` model must be running locally for the agent to work.
- If the city is not found or the API does not respond, a friendly error message is returned.
- If you need to use API keys, set them in the `.env` file as shown above.

## License
MIT
