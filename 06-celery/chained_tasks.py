from celery import Celery
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | PID:%(process)d | TID:%(thread)d | %(funcName)s | %(levelname)s | %(message)s"
)

app = Celery('chained-tasks', broker='redis://localhost:6378/0', backend='redis://localhost:6378/0')

@app.task
def fetch_user_data(user_id):
    logging.info(f"Sending request for {user_id}")
    result = {'id': 10, 'name': 'alice', 'score': 9}
    logging.info(f"User Data fethed succcessfully..")

    return result

@app.task
def process_user_data(data):
    logging.info(f"Processing the user data...")
    new_score = data['score'] * 10
    logging.info(f"Data Processed with new score: {new_score}")
    return new_score
