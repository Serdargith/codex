"""Main entry point tying modules together."""

import logging
from typing import List

import config
from ingest import fetch_content_packs
from poster import post_content
from scraper import init_db, fetch_recent_posts, store_posts
from analyzer import get_competitor_stats, recommend_hashtags
from notifier import send_summary
from scheduler import setup_scheduler

logging.basicConfig(level=logging.INFO)


def job():
    """Scheduled job that runs the full workflow."""
    logging.info("Starting scheduled job")

    # Initialize DB
    init_db()

    # Fetch new content packs
    packs = fetch_content_packs()
    posted_urls: List[str] = []

    for pack in packs:
        try:
            post_content(pack)
            posted_urls.append(pack['image_url'])
        except Exception as exc:  # noqa: BLE001
            logging.error("Failed to post content: %s", exc)

    # Competitor scraping (stub with example usernames)
    competitors = ["competitor1", "competitor2"]
    for comp in competitors:
        posts = fetch_recent_posts(comp)
        store_posts(comp, posts)

    stats = get_competitor_stats()
    hashtags = recommend_hashtags(stats)
    recommendations = f"Top hashtags: {', '.join(hashtags)}"

    send_summary(posted_urls, recommendations)
    logging.info("Job completed")


if __name__ == "__main__":
    scheduler = setup_scheduler(job)
    try:
        # Keep the main thread alive to let scheduler run
        import time
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
