"""Module for sending notifications via Slack or email."""

import logging
import requests
from typing import List

import config


def send_slack_message(message: str) -> None:
    """Send a message to Slack using the configured webhook."""
    payload = {"text": message}
    response = requests.post(config.SLACK_WEBHOOK_URL, json=payload)
    try:
        response.raise_for_status()
        logging.info("Sent Slack notification")
    except requests.HTTPError as exc:
        logging.error("Failed to send Slack message: %s", exc)


def send_summary(posted: List[str], recommendations: str) -> None:
    """Send a formatted summary message."""
    message = (
        f"Posts published: {', '.join(posted)}\n"
        f"Recommendations: {recommendations}"
    )
    send_slack_message(message)
