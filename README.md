# MCP Server Udemy Course

This repository demonstrates building and using Model Context Protocol (MCP) servers and clients.

## Project Structure

### MCP Server
- **`weather.py`** - MCP server implementation using FastMCP that exposes a `get_weather` tool to retrieve weather information for a given location

### MCP Clients
- **`mcp-client-single-server.py`** - Basic MCP client that connects to a single server (weather.py) and calls its tools
- **`mcp-client-multiple-servers.py`** - Advanced MCP client that connects to multiple servers in parallel using `asyncio.gather()` (weather server + Airbnb server)

## Setup Steps

1. **Initialize project**
   ```bash
   uv init
   ```

2. **Create virtual environment**
   ```bash
   uv venv
   ```

3. **Activate virtual environment**
   ```bash
   .venv\Scripts\activate
   ```

4. **Add MCP dependency**
   ```bash
   uv add mcp[cli]
   ```

5. **Test your MCP server with MCP Inspector**
   ```bash
   mcp dev weather.py
   ```
   This opens the MCP Inspector in your browser, allowing you to interactively test your server's tools and debug responses.

6. **Install the MCP server in Claude**
   - Go to Claude app in Desktop --> <user> --> Settings --> Developer --> Edit Config
   - It opens Windows folder where the claude_desktop_config.json lives. 
   - Edit claude_desktop_config.json. Add MCP server json here.

7. **Install the MCP server in VS Code**
   ```bash
   mcp install weather.py
   ```

## Running the Code

### Run Single Server Client
```bash
uv run mcp-client-single-server.py
```

### Run Multiple Servers Client
```bash
uv run mcp-client-multiple-servers.py
```

### Run Weather Server Standalone
```bash
uv run weather.py
```

## Key Concepts

- **MCP Server**: Exposes tools/capabilities that clients can discover and use
- **MCP Client**: Connects to servers, lists available tools, and calls them
- **Parallel Server Connections**: Use `asyncio.gather()` to connect to multiple servers simultaneously for better performance.