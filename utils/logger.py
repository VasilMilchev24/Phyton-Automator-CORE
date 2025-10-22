from colorama  import init, Fore, Style

init(autoreset=True)

def log_info(message:str):
    print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL}{message}")

def log_error(message:str):
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL}{message}")