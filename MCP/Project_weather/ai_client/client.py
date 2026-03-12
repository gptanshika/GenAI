import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server/server.py"]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "weather",
                {"city": "Bhopal"}
            )

            # Extract actual text
            weather = result.content[0].text

            print(f"Weather in Bhopal: {weather}")

asyncio.run(main())