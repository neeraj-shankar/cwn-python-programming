# packages/products/inventory.py
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    def is_available(self):
        return self.stock > 0

def check_inventory(product_id):
    """Check if product is in stock"""
    return f"Checking inventory for {product_id}"