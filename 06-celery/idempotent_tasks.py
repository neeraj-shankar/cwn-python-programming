from celery import Celery
import payements
app = Celery("myapp", broker='redis://localhost:6378/0', backend='redis://localhost:6378/0')

@app.task(bind=True, retries=3)
def process_payement(self, order_id, amount):

    # order = Orders.objects.get(id=order_id)
    order = {
        'order_id': 'am-202601182034',
        'status': 'PAID',
        'amount': '20'
    }

    # 1. Check if already paid
    if order['status'] == 'PAID':
        return 'ALREADY PROCESSED'
    
    # 2. Use a unique key for the external API
    respsone = payements.charge(
        amount=amount,
        idempotency_key=f'order-{order_id}'
    )

    return f"New Order Successfully processed: {order_id}"