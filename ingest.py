"""Utility to ingest content packs from a Google Sheet."""

import gspread
from google.oauth2.service_account import Credentials

import config

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def get_content_packs():
    """Retrieve content packs listed in the Google Sheet."""
    creds = Credentials.from_service_account_file(
        config.GOOGLE_SHEETS_CREDENTIALS_JSON, scopes=SCOPES
    )
    gc = gspread.authorize(creds)
    worksheet = gc.open_by_key(config.GOOGLE_SHEETS_DOCUMENT_KEY).worksheet("ContentPacks")
    rows = worksheet.get_all_records()
    packs = []
    for row in rows:
        if row:
            packs.append(row)
    return packs

if __name__ == "__main__":
    from pprint import pprint

    pprint(get_content_packs())
