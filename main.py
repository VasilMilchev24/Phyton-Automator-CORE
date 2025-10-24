from browser.driver import BrowserDriver
from ai.brain import plan_and_execute_sync
from utils.logger import log_info, log_error

def run_goal(goal: str):
    driver = BrowserDriver(headless=False)
    try:
        driver.start()
        res = plan_and_execute_sync(driver.page, goal)
        log_info("FINAL RESULT:")
        log_info(str(res))
    except Exception as e:
        log_error(f"Main run error: {e}")
    finally:
        driver.stop()

if __name__ == "__main__":
    user_goal = input("Enter goal (e.g. 'Search woman dress, sort by lowest, return name price link'): ")
    run_goal(user_goal)
