from faststream import FastStream
from faststream.confluent import KafkaBroker
from config import kafka_settings
from tasks import account_balance_update

broker = KafkaBroker(kafka_settings.dsn)
app = FastStream(broker)

@broker.subscriber(kafka_settings.account_topic)
async def handle_msg(data: dict) -> str:
    account_balance_update.delay(data)