# packages/payments/stripe_handler.py
def process_payment(amount, card_token):
    """Process payment through Stripe"""
    return f"Processing ${amount} via Stripe"

def refund_payment(transaction_id):
    """Refund a transaction"""
    return f"Refunding transaction {transaction_id}"