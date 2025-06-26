"""Module for ingesting new content packs from Google Sheets or other sources."""

from typing import List, Dict
from googleapiclient.discovery import build
from google.oauth2 import service_account

import config


def get_service() -> 'googleapiclient.discovery.Resource':
    """Authenticate and return the Google Sheets service."""
    credentials = service_account.Credentials.from_service_account_file(
        config.GOOGLE_SHEETS_CREDENTIALS_JSON,
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
    )
    return build("sheets", "v4", credentials=credentials)


def fetch_content_packs() -> List[Dict[str, str]]:
    """Fetch new content packs from the configured Google Sheet.

    Returns a list of dictionaries with keys: image_url, caption, hashtags.
    """
    service = get_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=config.GOOGLE_SHEETS_SPREADSHEET_ID,
                                range="ContentPacks!A2:C").execute()
    rows = result.get('values', [])

    packs = []
    for row in rows:
        if len(row) >= 3:
            packs.append({
                'image_url': row[0],
                'caption': row[1],
                'hashtags': row[2],
            })
    return packs
