# browser/executor.py
from browser.actions import navigate_to, click_element, type_text, get_text
from utils.logger import log_info, log_error
from utils.errors import PlanExecutionError

def execute_plan(page, plan):
   
    results = []
    for idx, step in enumerate(plan):
        try:
            action = step.get("action")
            target = step.get("target")
            value = step.get("value")
            log_info(f"Executing step {idx+1}: {action} -> {target} ({value})")

            if action == "goto":
                navigate_to(page, target)
            elif action == "click":
                click_element(page, target)
            elif action == "type":
                type_text(page, target, value or "")
            elif action == "select_option":
                try:
                    page.select_option(target, value=value)
                except Exception:
                    log_error(f"select_option failed for {target}={value}")
                    raise
            elif action == "extract_text":
                text = get_text(page, target)
                results.append({"target": target, "text": text})
            else:
                log_error(f"Unknown action: {action}")
        except Exception as e:
            log_error(f"Error executing step {idx+1}: {e}")
            raise PlanExecutionError(f"Step {idx+1} failed: {e}")
    return results
