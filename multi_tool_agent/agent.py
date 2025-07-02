from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import httpx
from geopy.geocoders import Nominatim
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams


async def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city using Open-Meteo API."""
    geolocator = Nominatim(user_agent="weather_agent")
    try:
        location = geolocator.geocode(city, timeout=10)
        if not location:
            return {"status": "error", "error_message": f"No se pudo encontrar la ciudad '{city}'."}
        lat, lon = location.latitude, location.longitude
    except Exception as e:
        return {"status": "error", "error_message": f"Error al buscar la ciudad: {e}"}

    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        "&current_weather=true&temperature_unit=celsius&windspeed_unit=kmh"
    )
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)
            data = response.json()
        if "current_weather" not in data:
            return {"status": "error", "error_message": f"No se pudo obtener el clima para '{city}'."}
        weather = data["current_weather"]
        report = (
            f"El clima en {city.title()} es {weather['temperature']}°C, "
            f"viento {weather['windspeed']} km/h. Código de clima: {weather['weathercode']}."
        )
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "error_message": f"Error al consultar el clima: {e}"}

arxiv_mcp_tool = MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://arxiv-mcp-sq0a.onrender.com/mcp",
        )
    )

MODEL_QWEN = "qwen3:8b"

root_agent = Agent(
    name="weather_time_agent",
    model=LiteLlm(model="ollama_chat/" + MODEL_QWEN),
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, arxiv_mcp_tool],
)