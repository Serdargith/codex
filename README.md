# codex

This project ingests content pack definitions from a Google Sheet.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Provide a Google service account credentials JSON file and update
   `config.GOOGLE_SHEETS_CREDENTIALS_JSON` with its path. Also set
   `config.GOOGLE_SHEETS_DOCUMENT_KEY` to the ID of your Google Sheet.

The script uses `gspread` to access the sheet; the older `googleapiclient`
packages are no longer required.

## Usage

Run the ingestion script:

```bash
python ingest.py
```
