from browser.driver import BrowserDriver
from browser.task import example_task
from utils.logger import log_info, log_error

def main():

    driver = BrowserDriver(headless=True)

    driver.start()

    try:
        example_task(driver.page)

    except Exception as e:
        log_error(f" Unexpected error in main: {e}")

    finally:
        driver.stop()

if __name__ == "__main__":
    main()
