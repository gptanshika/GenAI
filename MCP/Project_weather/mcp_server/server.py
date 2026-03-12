from mcp.server.fastmcp import FastMCP
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from services.weather_service import get_weather

mcp = FastMCP("Weather MCP Server")

@mcp.tool()
def weather(city: str):
    return get_weather(city)

if __name__ == "__main__":
    mcp.run()