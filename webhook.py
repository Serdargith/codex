"""Flask app to handle Instagram webhooks."""

from flask import Flask, request

import config

app = Flask(__name__)


@app.route("/webhook", methods=["GET", "POST"])
def webhook() -> tuple[str, int]:
    """Verify and respond to webhook requests."""
    if request.method == "GET":
        if (
            request.args.get("hub.mode") == "subscribe"
            and request.args.get("hub.verify_token") == config.WEBHOOK_VERIFY_TOKEN
        ):
            return request.args.get("hub.challenge"), 200
        return "Invalid token", 403
    return "Webhook received", 200


if __name__ == "__main__":
    app.run(port=5000)
