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

# Email settings
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "user@example.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "password")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT", "recipient@example.com")

# Database path
DATABASE_PATH = os.getenv("DATABASE_PATH", "data.db")

# Scheduler settings
# Run the job at 06:00, 13:00, and 20:00 by default
POST_SCHEDULE = os.getenv("POST_SCHEDULE", "0 6,13,20 * * *")
