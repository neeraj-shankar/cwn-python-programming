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

## The Chain (|)
- A Chain is for tasks that must happen sequentially. 
- The most important thing to know is that the **output** of the first task automatically becomes the **first argument** of the second task.

## The Group
- A Group is for parallel execution. Use this when you have 100 independent things to do and you want to use all your worker's cores.

## The Chord (The "Aggregation" Pattern)
- A Chord is a group with a callback. It says: "Run all these parallel tasks, and once every single one is finished, send all their results as a list to this final task."

## Indemptoncy
- Idempotency is perhaps the most critical concept in distributed systems like Celery. 
- Because Celery follows an "at-least-once" delivery guarantee, there is always a small chance that a task is executed more than once 
- (e.g., if the worker crashes right after finishing the work but before sending the "ACK" back to RabbitMQ/Redis).

### The Core Strategy: The "State Check"
The most reliable way to achieve idempotency is to ensure that every task checks the state of the system before performing an action.

1. *Unique Task IDs*: Every business action should have a unique identifier (like an order_id or a transaction_uuid).
2. *Database Constraints*: Use a UNIQUE constraint in your database on that identifier.
3. *Status Tracking:* Before processing, check if the record is already marked as "Processed" or "Paid."

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

### 4. In the Celery architecture, which component is responsible for receiving task messages and placing them in a queue for workers to consume?
- The broker, such as Redis or RabbitMQ, acts as the transport and storage layer for task messages between producers and workers.

### 5. Which Celery Canvas primitive should you use if you want to run a series of tasks in parallel and then execute a final 'callback' task once they are all finished?
- A chord consists of a header group (parallel tasks) and a callback that executes only after the entire header group completes.

### 6. What does the 'bind=True' argument in a task decorator allow you to do?
- This allows you to access task properties or methods like 'self.retry()' and 'self.update_state()'.
- `bind=True` allows a Celery task to access the task instance via self, enabling retries, access to request metadata, and advanced task control.

### 7. If you need to ensure a task is 'Idempotent,' what are you trying to achieve?
- The task can be executed multiple times without changing the result beyond the initial application.
- Idempotency is crucial for reliability, ensuring that accidental retries don't cause duplicate side effects like double payments.


### 8. How can make the task idempotent ?
- Idempotency ensures that retrying a task does not cause duplicate side effects. 
- Since distributed systems can execute tasks more than once, we design tasks to be retry-safe using **idempotency keys**, **state checks**, **database constraints**, **atomic transactions**, and *idempotent external APIs*.

### 9. Why would you set 'ignore_result=True' on a specific task?
- To improve performance and save storage in the Result Backend.
- If you don't need the return value, ignoring it reduces the overhead of writing to and maintaining the backend (e.g., Redis or SQL).

### 10. A task is received by a worker but the worker crashes before finishing. After some time, the task reappears in the queue. Which configuration setting primarily controls this 'reappearance' time?
- **visibility_timeout**: This setting defines the number of seconds to wait for the worker to acknowledge the task before the broker redelivers it to another worker.

### 11. If you are running 1,000 short-lived tasks per second that perform light network requests, which worker pool type is most efficient for high throughput?
- **eventlet or gevent**: These use green threads/co-routines to handle thousands of concurrent I/O connections within a single process with minimal overhead.

### 12. You have a task that updates a database. To ensure that a task is only removed from the queue after the database commit is successful, which setting should you enable?
- **task_acks_late**: By default, tasks are acknowledged just before execution; enabling this ensures acknowledgment happens only after the task returns.

### 13. What is the danger of setting 'worker_prefetch_multiplier = 0'?
- The worker will stop accepting tasks entirely. A zero value actually tells the worker to keep prefetching as many tasks as possible without limit.