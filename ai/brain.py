from browser.driver import BrowserDriver
from browser.mcp_client import send_mcp_request_async
from utils.logger import log_info, log_error

async def plan_and_execute_async(page, goal: str):
    """
    Plans and executes actions via MCP for a given goal.
    """
    try:
        log_info(f"🎯 Starting automation with goal: {goal}")
        # Take a snapshot of the page and send to MCP
        context = {"goal": goal}
        mcp_response = await send_mcp_request_async("plan", context)
        log_info(f"📄 MCP plan: {mcp_response}")
        return mcp_response
    except Exception as e:
        log_error(f"brain error: {e}")
        return None

def plan_and_execute_sync(page, goal: str):
    """
    Synchronous wrapper for backward compatibility.
    Only call this if there is no running event loop.
    """
    import asyncio
    try:
        return asyncio.run(plan_and_execute_async(page, goal))
    except RuntimeError:
        # If already inside a running event loop
        import nest_asyncio
        nest_asyncio.apply()  # patch event loop to allow nested asyncio.run
        return asyncio.run(plan_and_execute_async(page, goal))
