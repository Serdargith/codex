"""Module that analyzes post metrics and generates optimization recommendations."""

import sqlite3
from typing import List, Dict

import logging

import config


def compute_engagement_rate(likes: int, comments: int, followers: int) -> float:
    """Return engagement rate as a percentage."""
    if followers == 0:
        return 0.0
    return ((likes + comments) / followers) * 100


def get_competitor_stats() -> List[Dict[str, str]]:
    """Retrieve competitor post statistics from the database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT account, caption, like_count, comment_count, timestamp FROM competitor_posts"
    )
    rows = cursor.fetchall()
    conn.close()

    stats = []
    for row in rows:
        stats.append({
            "account": row[0],
            "caption": row[1],
            "like_count": row[2],
            "comment_count": row[3],
            "timestamp": row[4],
        })
    return stats


def recommend_hashtags(posts: List[Dict[str, str]]) -> List[str]:
    """Return the top hashtags based on like_count."""
    hashtag_scores = {}
    for post in posts:
        caption = post.get("caption", "")
        words = [w for w in caption.split() if w.startswith("#")]
        for tag in words:
            hashtag_scores[tag] = hashtag_scores.get(tag, 0) + post.get("like_count", 0)
    sorted_tags = sorted(hashtag_scores.items(), key=lambda x: x[1], reverse=True)
    return [tag for tag, _ in sorted_tags[:5]]
