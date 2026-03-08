import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TAVILY_API_Key")
headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get("https://api.tavily.com/v1/search", headers=headers, params={"query": "test"})
print(response.status_code, response.text)