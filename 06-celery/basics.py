from celery import Celery
import logging
import time

"""
Setting up basic task in celery

1. Running Celery Instance
celery -A basics worker --loglevel=info
"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | PID:%(process)d | TID:%(thread)d | %(funcName)s | %(levelname)s | %(message)s"
)

app = Celery('myapp', broker='redis://localhost:6378/0', backend='redis://localhost:6378/0')

# Basic task with no parameters
@app.task
def remove_duplicates():
    logging.info("Detecting the duplicates entry in arr")
    arr = [2, 3, 3, 7, 7, 9, 0, 0, 0, 10, 12]

    seen = set()
    result = []
    for num in arr:

        if num not in seen:
            result.append(num)
        seen.add(num)
    logging.info("Duplicate items removed from the list. Result stored")
    return result

# Running Task with dedicated Queue
"""
1. for executing fast calls
celery -A basics worker -l info -Q high_priority -n worker_fast

2. For executing slow worker calls
celery -A basics worker -l info -Q low_priority --concurrency=1 -n worker_slow

3. Start Flower for monitoring
celery -A basics flower --broker=redis://localhost:6378/0 --port=5555

"""
# Configuring the queues
app.conf.task_queues = {
    'high_priority':{'exchange': 'high_priority', 'routing_key': 'high_priority'},
    'low_priority':{'exchange': 'low_priority', 'routing_key': 'low_priority'}
}
@app.task
def fetch_data(api, duration):
    logging.info(f"Sending request to fetch data from fast api: {api}")
    time.sleep(duration)
    logging.info(f"Data Received from {api} in {duration} seconds")
    return f"{api} Data"
    
@app.task
def fetch_data_slow(api, duration):
    logging.info(f"Sending request to fetch data from slow api: {api}")
    time.sleep(duration)
    logging.info(f"Data Received from slow {api} in {duration} seconds")
    return f"{api} Data"
    

@app.task
def add_nums(a, b):
    logging.info(f"Adding {a} and {b}")

    result = a + b
    logging.info(f"Final Computed Value: {result}")

    return result