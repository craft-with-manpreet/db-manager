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


def get_trigger(granularity, interval):
    if granularity == 'seconds':
        return IntervalTrigger(seconds=interval)
    elif granularity == 'minutes':
        return IntervalTrigger(minutes=interval)
    elif granularity == 'hours':
        return IntervalTrigger(hours=interval)
    elif granularity == 'days':
        return CronTrigger(day_of_week='*', hour=0, minute=0, second=0)  # Daily at midnight
    elif granularity == 'months':
        return CronTrigger(day=1, hour=0, minute=0, second=0)  # Monthly on the 1st at midnight
    elif granularity == 'years':
        return CronTrigger(month=1, day=1, hour=0, minute=0, second=0)  # Yearly on January 1st at midnight
    else:
        raise ValueError("Invalid granularity")


scheduler_instance = BackgroundScheduler(jobstores=job_stores, job_defaults=job_defaults)
scheduler_instance.start()
