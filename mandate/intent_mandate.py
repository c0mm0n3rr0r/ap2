from typing import Optional, List
from pydantic import BaseModel, Field

class IntentMandate(BaseModel):
    """Represents the user's purchase intent."""

    user_cart_confirmation_required: bool = Field(
        True,
        description=(
            "If false, the agent can make purchases on the user's behalf once all "
            "purchase conditions have been satisfied."
        ),
    )

    natural_language_description: str = Field(
        ...,
        description="Natural language description of the user's intent.",
    )

    merchants: Optional[List[str]] = Field(
        None,
        description="Merchants allowed to fulfill the intent.",
    )

    skus: Optional[List[str]] = Field(
        None,
        description="Specific SKUs allowed.",
    )

    requires_refundability: Optional[bool] = Field(
        False,
        description="If true, items must be refundable.",
    )

    intent_expiry: str = Field(
        ...,
        description="ISO-8601 expiry timestamp for the intent mandate.",
    )
