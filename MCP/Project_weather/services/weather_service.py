import requests

def get_weather(city: str):

    coordinates = {
        "Bhopal": (23.2599, 77.4126),
        "Delhi": (28.6139, 77.2090),
        "Mumbai": (19.0760, 72.8777)
    }

    lat, lon = coordinates.get(city)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url).json()

    temp = response["current_weather"]["temperature"]

    return f"{temp}°C"