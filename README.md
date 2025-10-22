# Python Automator

## Overview
This Python project demonstrates a simple web automation bot using Playwright.
It can navigate a website, click elements, type text, and extract information.
The project is structured with modular components for maintainability.

## Project Structr
```text
playwright_bot/
│
├── browser/
│ ├── driver.py # Browser setup and lifecycle management
│ ├── actions.py # Functions to interact with web pages
│ ├── task.py # Example workflow task combining actions
├── utils/
│ ├── logger.py # Logging functions with colored output
├── main.py # Entry point to run the automation
├── requirements.txt # Python dependencies
├── README.md # This file
└── .gitignore # Files/folders to ignore in Git
```


## Setup Instructions


```bash


git clone <repo_url>
cd playwright_bot

2. Create and activate a virtual environment:
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt
python -m playwright install

4. Run the automation:
python main.py

5. Check console logs for results.
