from mcp import StdioServerParameters, ClientSession, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

server_params = StdioServerParameters(
    command = "uv",
    args = ["run", "weather.py"]
)

async def my_run():
    try:
        print("Starting mcp client...")

        """ The line below connects to the MCP server over stdio using server params, 
        then pass the "read" and "write" streams to a ClientSession. 
        
        stdio_client() returns two stream objects needed for bidirectional communication 
        with the MCP server, and unpacking them directly as a tuple makes the code cleaner 
        than accessing them via indices.
        """
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating client session...")
            async with ClientSession (read, write) as session:
                print("Initializing MCP...")
                await session.initialize()

                print("Listing tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling get_weather tool...")
                result = await session.call_tool("get_weather", arguments={"location": "New York"})

                print("Weather result:", result)
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(my_run())
