from celery import shared_task

from users.service.account_updater import AccountUpdateBalanceScheme, AccountUpdater
from config.celery import ACCOUNT_BALANCE_UPDATE


@shared_task(name=ACCOUNT_BALANCE_UPDATE)
def account_balance_update(json_data: dict):
    AccountUpdater().job(AccountUpdateBalanceScheme.model_validate(json_data))
