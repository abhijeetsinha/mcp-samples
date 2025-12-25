from mcp import StdioServerParameters, ClientSession, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

# Define parameters for multiple servers
weather_server_params = StdioServerParameters(
    command = "uv",
    args = ["run", "weather.py"]
)

airbnb_server_params = StdioServerParameters(
    command = "npx",
    args = ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
)

async def connect_to_weather_server():
    """Connect to weather server and perform operations"""
    async with stdio_client(weather_server_params) as (read, write):
        async with ClientSession(read, write) as session:
            print("Initializing weather server...")
            await session.initialize()
            
            print("Listing weather tools...")
            tools = await session.list_tools()
            print("Weather tools:", tools)
            
            print("Getting weather for New York...")
            result = await session.call_tool("get_weather", arguments={"location": "New York"})
            print("Weather result:", result)
            
            return result

async def connect_to_airbnb_server():
    """Connect to Airbnb server and perform operations"""
    async with stdio_client(airbnb_server_params) as (read, write):
        async with ClientSession(read, write) as session:
            print("Initializing Airbnb server...")
            await session.initialize()
            
            print("Listing Airbnb tools...")
            tools = await session.list_tools()
            print("Airbnb tools:", tools)

            print("Calling Airbnb tool...")
            result = await session.call_tool("airbnb_search", arguments={"location": "Vancouver"})
            print("Airbnb result:", result)
            
            return result

async def my_run():
    try:
        print("Starting MCP client with multiple servers in parallel...")
        
        # Run multiple server connections in parallel
        results = await asyncio.gather(
            connect_to_weather_server(),
            connect_to_airbnb_server()
        )
        
        print("\nAll servers completed!")
        print("Results:", results)
        
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(my_run())
