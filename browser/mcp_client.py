import json
import websockets
import asyncio
from utils.logger import log_info, log_error

# Custom exception for MCP connection errors
class MCPConnectionError(Exception):
    """Raised when connection to the MCP server fails."""
    pass

# MCP server URL
MCP_SERVER_URL = "ws://localhost:3000"

async def send_mcp_request_async(command: str, context: dict):
    """
    Sends a command and context to the MCP server asynchronously via WebSocket
    and returns the parsed JSON response.
    """
    try:
        async with websockets.connect(MCP_SERVER_URL) as websocket:
            payload = json.dumps({
                "command": command,
                "context": context
            })
            await websocket.send(payload)
            log_info(f"📡 Sent MCP command: {command}")

            response = await websocket.recv()
            log_info("📥 Received response from MCP.")
            return json.loads(response)
    except Exception as e:
        log_error(f"❌ MCP connection or response failed: {e}")
        raise MCPConnectionError(str(e))

def send_mcp_request(command: str, context: dict):
    """
    Synchronous wrapper for the async MCP request.
    Works even if there is already a running event loop.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        future = asyncio.ensure_future(send_mcp_request_async(command, context))
        raise RuntimeError(
            "send_mcp_request called from running event loop; please use the async version instead."
        )
    else:
        return asyncio.run(send_mcp_request_async(command, context))
