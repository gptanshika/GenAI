from typing import Any
import asyncio
import httpx
from mcp.server.fastmcp import FastMCP
from geopy.geocoders import Nominatim

mcp = FastMCP("Weather APP Server")

async def get_coordinated(city:str,country = None):
    geolocator = Nominatim(user_agent="my_geocoding_app")
    location_string = f"{city},{country}" if country else city 
    try:
        location = await asyncio.to_thread(geolocator.geocode, location_string)
        if location:
            return location.latitude, location.longitude
        else:
            return None,None
    except Exception as e:
        print(f"Error occured during geocoding: {e}")
        return None, None

async def get_weather(city:str,country=None)->str:
    try:
        lat,lon = await get_coordinated(city,country)
        if not lat and lon:
            print("Enable to fetch city coordinate from get_coordinated")
            return "Error"
        else:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                data = response.json()
            temp = data["current_weather"]["temperature"]
            return f"{temp}°C"
    except Exception as e:
        print(f"Error occured during weather details: {e}")
        return "Error"
    

@mcp.tool()
async def weather(city:str):
    return await get_weather(city)

if __name__ == "__main__":
    # mcp.run()
    print(asyncio.run(get_coordinated("Indore")))
    print(asyncio.run(get_weather("Indore")))
    


    

        


