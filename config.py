"""Configuration for credentials and settings.

Fill in the environment variables or replace with your own values.
"""

import os

# Instagram / Facebook credentials
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN", "YOUR_TOKEN")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID", "YOUR_ACCOUNT_ID")

# Google Sheets credentials
GOOGLE_SHEETS_CREDENTIALS_JSON = os.getenv("GOOGLE_SHEETS_CREDENTIALS_JSON", "path/to/credentials.json")
GOOGLE_SHEETS_SPREADSHEET_ID = os.getenv("GOOGLE_SHEETS_SPREADSHEET_ID", "SPREADSHEET_ID")

# Slack webhook URL
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/services/YOUR/WEBHOOK")

# Database path
DATABASE_PATH = os.getenv("DATABASE_PATH", "data.db")

# Scheduler settings
# Run the job at the beginning of every hour by default
POST_SCHEDULE = os.getenv("POST_SCHEDULE", "0 * * * *")
