# browser/actions.py
from playwright.sync_api import Page, TimeoutError
from utils.logger import log_info, log_error

def navigate_to(page: Page, url: str):
    try:
        log_info(f"Navigate to {url}")
        page.goto(url)
    except TimeoutError as e:
        log_error(f"Timeout navigating to {url}: {e}")
        raise
    except Exception as e:
        log_error(f"Error navigating to {url}: {e}")
        raise

def click_element(page: Page, selector: str):
    try:
        log_info(f"Clicking {selector}")
        page.wait_for_selector(selector, timeout=10000)
        page.click(selector)
    except TimeoutError as e:
        log_error(f"Timeout waiting for {selector}: {e}")
        raise
    except Exception as e:
        log_error(f"Error clicking {selector}: {e}")
        raise

def type_text(page: Page, selector: str, text: str):
    try:
        log_info(f"Typing into {selector}: {text}")
        page.wait_for_selector(selector, timeout=10000)
        page.fill(selector, text)
    except TimeoutError as e:
        log_error(f"Timeout typing into {selector}: {e}")
        raise
    except Exception as e:
        log_error(f"Error typing into {selector}: {e}")
        raise

def get_text(page: Page, selector: str) -> str:
    try:
        page.wait_for_selector(selector, timeout=10000)
        val = page.text_content(selector)
        return val.strip() if val else ""
    except TimeoutError:
        log_error(f"Timeout reading text from {selector}")
        return ""
    except Exception as e:
        log_error(f"Error reading {selector}: {e}")
        return ""
