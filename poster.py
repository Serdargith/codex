"""Module responsible for posting images to Instagram."""

from typing import List, Dict
import logging
import requests

import config

GRAPH_API_URL = "https://graph.facebook.com/v15.0"


def create_media_object(image_url: str, caption: str) -> str:
    """Create an Instagram media object and return the media ID."""
    endpoint = f"{GRAPH_API_URL}/{config.INSTAGRAM_ACCOUNT_ID}/media"
    payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": config.INSTAGRAM_ACCESS_TOKEN,
    }
    response = requests.post(endpoint, data=payload)
    response.raise_for_status()
    media_id = response.json().get("id")
    logging.debug("Created media object %s", media_id)
    return media_id


def publish_media(media_id: str) -> None:
    """Publish a previously created media object."""
    endpoint = f"{GRAPH_API_URL}/{config.INSTAGRAM_ACCOUNT_ID}/media_publish"
    payload = {
        "creation_id": media_id,
        "access_token": config.INSTAGRAM_ACCESS_TOKEN,
    }
    response = requests.post(endpoint, data=payload)
    response.raise_for_status()
    logging.info("Published media %s", media_id)


def post_content(pack: Dict[str, str]) -> None:
    """Post a content pack to Instagram."""
    media_id = create_media_object(pack['image_url'], f"{pack['caption']} {pack['hashtags']}")
    publish_media(media_id)
