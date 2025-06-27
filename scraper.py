"""Module for scraping competitor Instagram data."""

import logging
from typing import List, Dict

import requests
import sqlite3

import config

GRAPH_API_URL = "https://graph.facebook.com/v15.0"


def init_db():
    """Initialize the SQLite database for storing posts."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS competitor_posts (
            id TEXT PRIMARY KEY,
            account TEXT,
            caption TEXT,
            like_count INTEGER,
            comment_count INTEGER,
            timestamp TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def fetch_recent_posts(username: str) -> List[Dict[str, str]]:
    """Fetch recent posts for a competitor account using the Graph API."""
    # This assumes you know the Instagram business account ID for the username.
    # In practice you'd resolve username -> ID via additional API calls.
    endpoint = f"{GRAPH_API_URL}/{username}/media"
    params = {
        "fields": "id,caption,like_count,comments_count,timestamp",
        "access_token": config.INSTAGRAM_ACCESS_TOKEN,
        "limit": 20,
    }
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    data = response.json().get("data", [])
    logging.debug("Fetched %d posts for %s", len(data), username)
    return data


def store_posts(account: str, posts: List[Dict[str, str]]):
    """Store fetched posts in the database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    cursor = conn.cursor()
    for post in posts:
        cursor.execute(
            """
            INSERT OR REPLACE INTO competitor_posts (id, account, caption, like_count, comment_count, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                post.get("id"),
                account,
                post.get("caption"),
                post.get("like_count"),
                post.get("comments_count"),
                post.get("timestamp"),
            ),
        )
    conn.commit()
    conn.close()
