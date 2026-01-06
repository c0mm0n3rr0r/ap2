from datetime import datetime, timezone
from mandate.intent_mandate import IntentMandate
from store.catalog import list_products, get_product

def search_products():
    return list_products()

def view_product(sku):
    return get_product(sku)

def execute_purchase(sku: str, mandate_dict: dict):
    intent = IntentMandate(**mandate_dict)
    product = get_product(sku)

    expiry = datetime.fromisoformat(intent.intent_expiry.replace("Z", "+00:00"))
    if datetime.now(timezone.utc) > expiry:
        return {"status": "DENIED", "reason": "intent_expired"}

    if intent.merchants and product["merchant"] not in intent.merchants:
        return {"status": "DENIED", "reason": "merchant_not_allowed"}

    if intent.skus and product["sku"] not in intent.skus:
        return {"status": "DENIED", "reason": "sku_not_allowed"}

    if intent.requires_refundability and not product["refundable"]:
        return {"status": "DENIED", "reason": "refundability_required"}

    if intent.user_cart_confirmation_required:
        return {"status": "DENIED", "reason": "user_confirmation_required"}

    return {
        "status": "PURCHASED",
        "sku": sku,
        "price": product["price"],
        "merchant": product["merchant"],
    }
