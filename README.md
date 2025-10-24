# Playwright AI Agent (Core + MCP + API)

## What this repo contains
- Core Playwright automation (login, search, sort, extract)
- Optional Challenge 1: Full Playwright MCP integration (MCP WebSocket client, LLM planner, executor)
- Optional Challenge 2: FastAPI endpoint to trigger tasks remotely

## Requirements
- Python 3.10+
- Node.js 18+ (for Playwright MCP)
- Playwright MCP server running: `npx @playwright/mcp@latest` or `playwright-mcp`
NOTE: If you have a problem with npx not installing playwright do the following:
1. Clear npx cache
```
npx clear-npx-cache

```
2. Instead of running the package directly from the registry, install it first:
```
npm install @playwright/mcp@latest

wait until you see "added 2+ packages"
```
3. Then run it from node_modules:
```
npx playwright-mcp

```
- OpenAI API key set in `OPENAI_API_KEY`

## Setup (quick)
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m playwright install   # if using Playwright browser local
# Start MCP server in a separate terminal:
npx @playwright/mcp@latest
# Run locally:
python main.py

5. Check console logs for results.

````



