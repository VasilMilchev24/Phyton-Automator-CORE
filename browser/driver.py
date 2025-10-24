from playwright.sync_api import sync_playwright
from utils.logger import log_info, log_error

class BrowserDriver:
    def __init__(self,headless:bool=True):
        self.headless=headless
        self.playwright=None
        self.browser=None
        self.page=None

    def start(self):
        try:
            log_info("Starting Playwright...")
            self.playwright=sync_playwright().start()

            self.browser=self.playwright.chromium.launch(headless=self.headless)
            self.page=self.browser.new_page()
            self.page.set_default_timeout(10000)

            log_info("✅ Browser started successfully.")

        except Exception as e:
            log_error(f"Failed to start browser: {e}")
            self.stop()

    def stop(self):
        try:
            if self.browser:
                log_info("Closing browser...")
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
            log_info("Browser stoped.")
        except Exception as e:
            log_error(f"Error during browser stop: {e}")