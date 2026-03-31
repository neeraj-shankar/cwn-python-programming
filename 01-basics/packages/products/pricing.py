# packages/products/pricing.py
def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    return price * (1 - discount_percent / 100)

def apply_tax(price, tax_rate=0.08):
    """Apply sales tax"""
    return price * (1 + tax_rate)