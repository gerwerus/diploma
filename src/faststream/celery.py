import os

from celery import Celery

app = Celery("config")
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")

app.autodiscover_tasks()

# Task names
ACCOUNT_BALANCE_UPDATE = "account_balance_update"
