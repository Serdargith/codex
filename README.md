# Ortopedi Haberleri Instagram Automation

This project provides a scaffold for automating Instagram content planning, posting, and optimization for an orthopedics news account.

## Modules
- `ingest.py` – fetch content packs from Google Sheets.
- `poster.py` – publish images to Instagram using the Graph API.
- `scraper.py` – store competitor data in SQLite.
- `analyzer.py` – compute engagement metrics and recommendations.
- `notifier.py` – send summaries via Slack.
- `scheduler.py` – schedule tasks with APScheduler.
- `main.py` – entry point that ties everything together.

Fill in `config.py` with your credentials. By default the job runs at the top of every hour; adjust `POST_SCHEDULE` if you need a different cron expression. Install dependencies via `pip install -r requirements.txt`.

## Free scheduling via GitHub Actions

You can run the automation without hosting costs by using [GitHub Actions](https://docs.github.com/en/actions). A workflow file is included in `.github/workflows/scheduler.yml` that runs `main.py` at the start of every hour. Set the required secrets (e.g. `INSTAGRAM_ACCESS_TOKEN`) in your repository settings and enable the workflow.
