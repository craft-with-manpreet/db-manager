# Author: Manpreet Singh
# Email: dev.manpreet.io@gmail.com
# GitHub: https://github.com/craft-with-manpreet
# Portfolio: https://dev-manpreet.web.app
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings

job_stores = {
    'default': SQLAlchemyJobStore(url=settings.SQLALCHEMY_DATABASE_URI)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}


def get_trigger(frequency, interval=1):
    if frequency == 'seconds':
        return IntervalTrigger(seconds=interval)
    elif frequency == 'minutes':
        return IntervalTrigger(minutes=interval)
    elif frequency == 'hourly':
        return IntervalTrigger(hours=interval)
    elif frequency == 'everyday':
        return CronTrigger(day_of_week='*', hour=0, minute=0, second=0)  # Daily at midnight
    elif frequency == 'monthly':
        return CronTrigger(day=1, hour=0, minute=0, second=0)  # Monthly on the 1st at midnight
    elif frequency == 'yearly':
        return CronTrigger(month=1, day=1, hour=0, minute=0, second=0)  # Yearly on January 1st at midnight
    else:
        raise ValueError("Invalid frequency")


scheduler_instance = BackgroundScheduler(jobstores=job_stores, job_defaults=job_defaults)
scheduler_instance.start()
