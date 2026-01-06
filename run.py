from datetime import datetime, timedelta, timezone
from mandate.intent_mandate import IntentMandate
from agent.adk_agent import build_agent

def iso_in(minutes):
    return (datetime.now(timezone.utc) + timedelta(minutes=minutes)).isoformat()

def main():
    mandate = IntentMandate(
        user_cart_confirmation_required=False,
        natural_language_description=(
            "Buy the best value headphones. Saving money is the priority, "
            "but avoid low quality products."
        ),
        merchants=None,
        skus=None,
        requires_refundability=True,
        intent_expiry=iso_in(30),
    )

    agent = build_agent(mandate)

    agent.run(
        goal=(
            "Complete the purchase according to the intent mandate. "
            "Use available tools to explore products and purchase one."
        ),
        context={
            "intent_mandate": mandate.model_dump()
        }
    )

if __name__ == "__main__":
    main()
