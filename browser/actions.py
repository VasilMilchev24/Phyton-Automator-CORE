from playwright.sync_api import Page, TimeoutError
from utils.logger import log_info, log_error

def navigate_to(page:Page, url:str):
    try:
        log_info(f"Navigation to {url}...")
        page.goto(url)
        log_info(f"Successfully navigated to {url}.")
    except Exception as e:
        log_error(f"Failed to navigete to {url}: {e}")

def click_element(page:Page, selector:str):
    try:
        log_info(f"Clicking element '{selector}'")
        page.click(selector)
        log_info(f"Successfully clicked element '{selector}'")
    except Exception as e:
        log_error(f"Failed to click element '{selector}': {e}")

def type_text(page:Page,selector:str,text:str):
    try:
        log_info(f"Typing into '{selector}': {text}")
        page.fill(selector,text)
        log_info(f"Successfully typed into '{selector}'")
    except TimeoutError:
        log_error(f"timeout while typeing into '{selector}'")
    except Exception as e:
        log_error(f"Failed to type into '{selector}': {e}")

def get_text(page:Page,selector:str)->str:
    try:
        log_info(f"Retrieving text from '{selector}'...")
        text=page.text_content(selector)
        log_info(f"Successfully retrieved text '{text}'")
        return text if text else ""
    except TimeoutError:
        log_error(f"Timeout while retrieving text from '{selector}'")
    except Exception as e:
        log_error(f"Failed to retrieve text from '{selector}': {e}")
    return ""