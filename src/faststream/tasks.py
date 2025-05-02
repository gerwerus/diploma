from celery import shared_task

from celery_app import ACCOUNT_BALANCE_UPDATE


@shared_task(name=ACCOUNT_BALANCE_UPDATE)
def account_balance_update(json_data: dict):
    pass