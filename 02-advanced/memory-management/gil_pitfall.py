"""
CPU-Bound Tasks Don't Parallelize: This is the biggest limitation. 
If you have a computationally intensive task and try to use multiple threads, you won't see speedup. 

In fact, you might see slowdown due to thread-switching overhead.
"""


import threading
import time

def cpu_intensive_task():
    count = 0
    for i in range(50_000_000):
        count += i
    return count

# Single-threaded
start = time.time()
cpu_intensive_task()
print(f"Single thread: {time.time() - start:.2f}s")

# Multi-threaded (2 threads)
start = time.time()
threads = []
for _ in range(2):
    t = threading.Thread(target=cpu_intensive_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print(f"Two threads: {time.time() - start:.2f}s")