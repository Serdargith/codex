"""Scheduler setup using APScheduler."""

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

import config


def setup_scheduler(job_func) -> BackgroundScheduler:
    """Configure and return an APScheduler instance."""
    scheduler = BackgroundScheduler()
    trigger = CronTrigger.from_crontab(config.POST_SCHEDULE)
    scheduler.add_job(job_func, trigger, id="instagram_post")
    scheduler.start()
    logging.info("Scheduler started with cron %s", config.POST_SCHEDULE)
    return scheduler
