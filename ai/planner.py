import os
import json
import openai
from utils.logger import log_info, log_error

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")

openai.api_key= OPENAI_API_KEY

PLAN_PROMPT_INSTRUCTIONS = """
You are an automation planner. You will be given:
- A 'page snapshot' JSON that contains keys: url, title, elements[].
- A user goal in plain English.

Return a strict JSON array of plan steps. Each step is an object with:
- action: one of ["goto", "click", "type", "select_option", "extract_text"]
- target: string (for goto -> url; for others -> selector or visible text)
- value: optional (for type/select_option)
Example plan:
[
  {"action":"click","target":"Sign in"},
  {"action":"type","target":"#email","value":"me@example.com"},
  {"action":"type","target":"#passwd","value":"Secret"},
  {"action":"click","target":"Sign in"},
  {"action":"type","target":"search box","value":"blue shirt"},
  {"action":"click","target":"Search"},
  {"action":"select_option","target":"#selectProductSort","value":"price:asc"},
  {"action":"extract_text","target":".product_list .product-name"}
]
Return ONLY the JSON array and NOTHING else.
"""

def ask_llm_for_plan(snapshot: dict, goal: str, model: str = "gpt-4o-mini"):
    """
    Sends snapshot + goal to OpenAI and asks for a JSON plan.
    Returns Python list (parsed JSON).
    """
    system = "You are a strict planner. Output only valid JSON as described."

    prompt = f"PAGE_SNAPSHOT:\n{json.dumps(snapshot, indent=2)}\n\nGOAL:\n{goal}\n\n{PLAN_PROMPT_INSTRUCTIONS}"

    log_info("Sending prompt to LLM for plan generation...")

    try:
        resp=openai.ChatCompletion.create(
            model=model,
            messages=[{"role":"system","content":system}, {"role":"user","content":prompt}],
            temperature=0.0,
            max_tokens=800
        )
        
        text = resp["choices"][0]["message"]["content"].strip()
        log_info(f"LLM raw response:\n{text}")
        plan = json.loads(text)
        log_info("Parsed plan JSON.")
        return plan
    except Exception as e:
        log_error(f"LLM plan error: {e}")
        raise