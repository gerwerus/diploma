from decimal import Decimal
from pydantic import BaseModel, Field, field_validator, ConfigDict


class AccountUpdateBalanceScheme(BaseModel):
    """Schema for updating account balance with validation"""

    account_id: int = Field(
        ..., alias="id", examples=[42], description="Unique identifier of the account"
    )
    balance_change: Decimal = Field(
        ...,
        examples=[Decimal("-250.75"), Decimal("100.00")],
        description="Non-zero decimal value to change account balance (positive or negative)",
    )

    @field_validator("balance_change")
    def validate_balance_change(cls, value: Decimal) -> Decimal:
        """Validate that balance change is non-zero and properly formatted"""
        if value.is_zero():
            raise ValueError("Balance change must be non-zero")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "description": "Account balance update operation schema",
            "examples": [
                {"id": 1, "balance_change": -100.50},
                {"id": 2, "balance_change": "200.75"},
            ],
        },
    )
