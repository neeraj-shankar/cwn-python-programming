# Celery - A comprehensive Guide

## Celery Messaging Model
- Celery follows AMQP concepts:
```arduino
Task → Exchange → Queue → Worker
```
1. **Producer** (your app) sends a task
2. **Exchange** routes the task
3. **Queue** stores the task
4. **Worker** consumes the task

## **Routing**
Routing is a powerful concept because it prevents your "heavy" tasks (like video processing) from clogging up the pipes for your "critical/fast" tasks (like sending a password reset email). In Celery, you do this using *Queues*.

### 1. Defining the Queues
```python
from celery import Celery

app = Celery('tasks', 
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

# Optional: Configuration to define named queues
app.conf.task_queues = {
    'high_priority': {'exchange': 'high_priority', 'routing_key': 'high_priority'},
    'low_priority': {'exchange': 'low_priority', 'routing_key': 'low_priority'},
}
```

### 2. Sending Tasks to Specific Queues
```python
# In your Python shell:
from tasks import add, sleepy_task

# This goes to the fast lane
add.apply_async((2, 2), queue='high_priority')

# This goes to the slow lane
sleepy_task.apply_async((1,), queue='low_priority')
```

### 3. Starting Specialist Workers
```bash
# Start Celery worker that consumes from high_priority queue.
celery -A myapp worker -l info -Q high_priority -n worker_fast

# Start Celery worker that consumes from low_priority queue
celery -A tasks worker -l info -Q low_priority --concurrency=1 -n worker_slow
```

#### **Note**
- We use `.apply_async(args=(...) , queue='...')` instead of `.delay()` because .delay() doesn't support custom routing options.

#### By separating them:

- **Isolation:** If 1,000 "Low Priority" tasks arrive, they will sit in their own queue. Your "High Priority" worker is still idle and ready to process an urgent email instantly.

- **Resource Allocation:** You can run the "Slow" worker on a cheaper machine with less RAM, and the "Fast" worker on a high-performance instance.

- **Monitoring:** In Flower, you will see exactly which queue is backing up.

## FAQs

### 1. Why would you ever want **Concurrency = 1**?
In a real-world project, you might set a specific queue to concurrency 1 if:

- **Limited Resources:** You are interacting with a legacy database that can only handle one connection at a time.
- **API Rate Limits:** You are scraping a website that will ban you if you send more than one request at a time.
- **Strict Ordering:** You need to process financial transactions in the exact order they were received.

#### **Note**
- Even with `concurrency=1`, Celery will "reserve" (prefetch) extra tasks from Redis so they are ready to go the moment the first one finishes. 
- If you want a worker to only take exactly what it is working on and nothing more, you use: `--concurrency=1 -Ofair`

### 2. What's difference between delay() and apply_async()
- `delay()` is a convenience wrapper around `apply_async()` that sends tasks with default options, whereas apply_async() provides full control over task execution, routing, retries, and scheduling.

### 3. Explain this bash command: "celery -A routing_tasks worker -l info -Q high_priority -n worker_fast"
- Starts a Celery worker for the routing_tasks app that listens only to the high_priority queue, logs at INFO level, and runs with a custom worker name worker_fast.
- This command starts a Celery worker for a specific app, sets the logging level, restricts the worker to consume only from the high_priority queue, and assigns a custom worker name for easier identification and monitoring.
