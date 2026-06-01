"""
===================================================================================================
The "Success" Scenario: Coordinating Two Threads
-----------------------------------------------------------
Two threads try to increment a shared counter. Without the lock, you would experience a Race Condition. 
With the lock, one thread is forced to wait (block) while the other finishing its work.

---------------------------------------------------------------------
What happens here:

    1. Thread-1 acquires the lock.
    2. Thread-2 tries to acquire the lock but sees it's "Locked." It enters a blocked state (it stops executing).
    3. Thread-1 finishes and releases the lock.
    4. The OS wakes up Thread-2, which then proceeds.
===================================================================================================
"""
import threading
import time

shared_counter = 0
lock = threading.Lock()

def increment_counter(thread_name):
    global shared_counter
    print(f"{thread_name} attempting to acquire lock.")

    with lock: # Thread will 'block' here if another thread has the lock
        print(f"{thread_name} acquired lock, increasing counter")
        current_value = shared_counter
        time.sleep(10) # Simulating an I/O delay or heavy work
        shared_counter = current_value + 1
        print(f"{thread_name} releasing lock. Counter: {shared_counter}")

# Create two threads 
t1 = threading.Thread(target=increment_counter, args=("Thread-1", ))
t2 = threading.Thread(target=increment_counter, args=("Thread-2", ))

t1.start()
t2.start()

t1.join()
t2.join()

"""
===================================================================================================
The "Risk" Scenario: Self-Deadlock
---------------------------------------------------------------------
This happens when a thread is "forgetful." It already has the lock, but it calls a function or 
a piece of code that tries to acquire that same lock again. 

Because the lock is Primitive, it doesn't care who owns it—it only knows that it's currently "Locked."
---------------------------------------------------------------------

Why it fails:
---------------------------------------------------------------------
    1. The main_function locks the door and keeps the key.
    2. It then calls nested_function.
    3. nested_function sees the door is locked and decides to sit down and wait for the door to open.
    4. Since the person who has the key is the one waiting for the door to open, the program deadlocks.

===================================================================================================
"""

import threading

primitive_lock = threading.Lock() # Creates deadlock
reentrant_clock = threading.RLock() # Safe for nested function
def nested_function():
    print("Nested function: Trying to acquire lock.")
    with reentrant_clock:
        print(f"Nested Function: Acquired the lock.")


def main_function():
    print("Main Function: Trying to acquire to lock..")

    with reentrant_clock:
        print("Main function: Acquired the lock. Calling nested function")
        nested_function()

main_function()

"""
===================================================================================================

Semaphore
---------------------------------------------------------------------
A Semaphore acts like a "bouncer" for a club. While a Lock only allows one person in at a time, 
a Semaphore has a set capacity (e.g., 3). It tracks how many "permits" are available.
---------------------------------------------------------------------

The "Pass" Use Case: Throttling Resource Access
---------------------------------------------------------------------
Imagine you have 10 threads trying to hit a database, but your database can only handle 3 connections 
at once without crashing. 

The Semaphore ensures that 3 "Pass" through, while the others wait in line.

===================================================================================================
"""

import threading
import time 
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(funcName)s %(process)d %(thread)d %(message)s"
)

log = logging.getLogger(__name__)

# Allowing only 3 threads at a time
connection_limit = threading.Semaphore(3)


def access_database(thread_id):
    with connection_limit:

        log.info(f" >>> [PASS] Thread: {thread_id} secured a connection.")
        work_time = random.uniform(1, 2)
        time.sleep(work_time)

        log.info(f" <<< [RELEASE] Thread: {thread_id} finishing work after {work_time:.2f}s.")

# Launching 6 threads
threads = []

for i in range(1, 7):
    t = threading.Thread(target=access_database, args=(i, ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()




"""
===================================================================================================
The "Fail" Use Case: The Signal Mismatch
---------------------------------------------------------------------
A common mistake (and a way to "Fail" the logic) is when the `release()` calls don't match the acquire() calls, 
or a thread releases a semaphore it never acquired. 

Unlike a Lock, a Semaphore doesn't track which thread owns it.
---------------------------------------------------------------------

Scenario: The "Permit Leak"
---------------------------------------------------------------------
If a thread crashes or exits without releasing, the capacity shrinks forever until the system hangs.
===================================================================================================
"""

sem = threading.Semaphore(2)
def faulty_worker():

    log.info(f"Worker attempting to acquire....")
    sem.acquire()
    log.info("Worker acquired the locked..")

    raise Exception("System Crashed")

try:
    faulty_worker()
except:
    log.error("Worker crashed before releasing the lock")

# Using the remaining available thread
log.info(f"Available Permits: {sem._value}")
sem.acquire() 
log.info(f"Acquired lock on available permist. Permit left: {sem._value}")
sem.release()
log.info(f"Trying get final lock...{sem._value}")
sem.acquire()