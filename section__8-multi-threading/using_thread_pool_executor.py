import concurrent.futures
import time
import threading
import os

def task(name):
    thread_id = threading.get_ident()
    process_id = os.getpid()
    print(f"Task {name} started (Thread ID: {thread_id}, Process ID: {process_id})")
    time.sleep(10)
    print(f"Task {name} finished (Thread ID: {thread_id}, Process ID: {process_id})")

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(5):
        executor.submit(task, f"Task {i}")