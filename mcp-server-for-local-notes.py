from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalNotes")

@mcp.tool()
def add_notes_to_file(content:str) -> str:
    """
    Append the given content to user's local notes.
    Args:
        content: The text content to append to the file.
    """
    filename = "notes.txt"
    try:
        with open(filename, "a") as f:
            f.write(content + "\n")
        return f"Content added to {filename}."
    except Exception as e:
        return f"An error occurred: {e}"

@mcp.tool()
def read_notes_from_file() -> str:
    """
    Read and return the content of the local notes.
    """
    filename = "notes.txt"
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "No notes found. The file does not exist."
    except Exception as e:
        return f"An error occurred: {e}"
    
if __name__ == "__main__":
    mcp.run()