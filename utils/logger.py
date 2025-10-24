from colorama import init, Fore, Style
import datetime

class MCPConnectionError(Exception):
    """Raised when connection to the MCP server fails."""
    pass

init(autoreset=True)

def _now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_info(msg: str):
    print(f"{_now()} {Fore.CYAN}[INFO]{Style.RESET_ALL} {msg}")

def log_success(msg: str):
    print(f"{_now()} {Fore.GREEN}[OK]{Style.RESET_ALL} {msg}")

def log_error(msg: str):
    print(f"{_now()} {Fore.RED}[ERROR]{Style.RESET_ALL} {msg}")
