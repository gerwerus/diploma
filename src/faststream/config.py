from pydantic import Field
from pydantic_settings import BaseSettings


class KafkaSettings(BaseSettings):
    host: str = Field(alias='KAFKA_HOST')
    port: int = Field(alias='KAFKA_PORT')

    account_topic: str = "account-updater"

    @property
    def dsn(self) -> str:
        return f"{self.host}:{self.port}"


kafka_settings = KafkaSettings()