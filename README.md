# Ortopedi Haberleri Instagram Automation

This project provides a scaffold for automating Instagram content planning, posting, and optimization for an orthopedics news account.

## Modules
- `ingest.py` – fetch content packs from Google Sheets.
- `poster.py` – publish images to Instagram using the Graph API.
- `scraper.py` – store competitor data in SQLite.
- `analyzer.py` – compute engagement metrics and recommendations.
- `notifier.py` – send summaries via Slack and email.
- `scheduler.py` – schedule tasks with APScheduler.
- `main.py` – entry point that ties everything together.
- `webhook.py` – simple Flask app to handle Instagram webhook verification.

Fill in `config.py` with your credentials. By default the job runs once per day at 06:00; adjust `POST_SCHEDULE` if you need a different cron expression. Install dependencies via `pip install -r requirements.txt`.

## Free scheduling via GitHub Actions

You can run the automation without hosting costs by using [GitHub Actions](https://docs.github.com/en/actions). A workflow file is included in `.github/workflows/scheduler.yml` that runs `main.py` daily at 06:00. Set the required secrets (e.g. `INSTAGRAM_ACCESS_TOKEN`) in your repository settings and enable the workflow.

After each run the system sends a PDF summary by email. Configure the SMTP and recipient details in `config.py` or environment variables.
