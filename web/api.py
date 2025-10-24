from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from browser.driver import BrowserDriver
from ai.brain import plan_and_execute_sync
from utils.logger import log_info, log_error

app = FastAPI()

class GoalIn(BaseModel):
    goal: str

@app.post("/run")
def run_goal_api(payload: GoalIn):
    driver = BrowserDriver(headless=True)
    try:
        driver.start()
        result = plan_and_execute_sync(driver.page, payload.goal)
        return {"status": "ok", "result": result}
    except Exception as e:
        log_error(f"API run error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        driver.stop()
