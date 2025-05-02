from users.models import Account
from users.service.account_updater.entities import AccountUpdateBalanceScheme
from django.db import transaction
import logging


class AccountUpdater:
    def job(self, data: AccountUpdateBalanceScheme):
        with transaction.atomic():
            if acc := Account.objects.filter(id=data.account_id).first():
                amount = acc.balance + data.balance_change
                if amount >= 0:
                    acc.balance = amount
                    acc.save()
                else:
                    logging.error(f"Balance amount < 0 for account {data.account_id}")
            else:
                logging.error(f"There is no acc with id={data.account_id}")
