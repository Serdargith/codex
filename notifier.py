"""Module for sending notifications via Slack or email."""

import logging
import smtplib
from email.message import EmailMessage
from pathlib import Path
from typing import List

import requests
from reportlab.pdfgen import canvas

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


def generate_pdf(posted: List[str], recommendations: str, output: Path) -> None:
    """Create a simple PDF report summarizing results."""
    c = canvas.Canvas(str(output))
    c.setFont("Helvetica", 12)
    y = 800
    c.drawString(50, y, "Instagram Automation Report")
    y -= 40
    c.drawString(50, y, "Posts published:")
    for url in posted:
        y -= 20
        c.drawString(70, y, url)
    y -= 40
    c.drawString(50, y, "Recommendations:")
    y -= 20
    for line in recommendations.split("\n"):
        c.drawString(70, y, line)
        y -= 20
    c.save()


def send_email_with_pdf(pdf_path: Path) -> None:
    """Email the PDF report using SMTP credentials."""
    msg = EmailMessage()
    msg["Subject"] = "Instagram Automation Report"
    msg["From"] = config.SMTP_USERNAME
    msg["To"] = config.EMAIL_RECIPIENT
    msg.set_content("See attached report.")
    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=pdf_path.name,
        )
    try:
        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
            server.send_message(msg)
        logging.info("Sent email report")
    except Exception as exc:  # noqa: BLE001
        logging.error("Failed to send email: %s", exc)


def send_summary(posted: List[str], recommendations: str) -> None:
    """Send summary via Slack and email."""
    message = (
        f"Posts published: {', '.join(posted)}\n"
        f"Recommendations: {recommendations}"
    )
    send_slack_message(message)

    pdf_path = Path("report.pdf")
    generate_pdf(posted, recommendations, pdf_path)
    send_email_with_pdf(pdf_path)
