from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image
import pyautogui
import io

mcp = FastMCP("ScreenshotTool")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Capture a screenshot of the current screen and return it as an image. Use this tool 
    when the user requests a screenshot of their activity.
    """
    screenshot = pyautogui.screenshot()
    img_byte_arr = io.BytesIO()
    screenshot.convert("RGB").save(img_byte_arr, format='JPEG', quality=60, optimize=True)
    return Image(data=img_byte_arr.getvalue(), format='jpeg')

if __name__ == "__main__":
    mcp.run()