from dotenv import load_dotenv
import os

load_dotenv()

SITE_USERNAME = os.getenv("SITE_USERNAME")
SITE_PASSWORD = os.getenv("SITE_PASSWORD")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

if not SITE_USERNAME or not SITE_PASSWORD:
    print("⚠️ Warning: Missing SITE_USERNAME or SITE_PASSWORD in .env file.")
