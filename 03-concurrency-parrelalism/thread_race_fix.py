"""
To fix this, we use a Lock. Only the thread holding the "key" can touch the counter. 
If another thread wants it, it has to wait in line.
"""
import threading 
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | PID:%(process)d | TID:%(thread)d | %(funcName)s | %(levelname)s | %(message)s"
)


lock = threading.Lock()
# Shared resource between threads
counter = 0

def increase_counter():
    global counter

    with lock: # The thread "grabs the key" here
        logging.info(f"Task being executed: ")
        for _ in range(100000000):
            counter += 1
    
    # The thread "releases the key" here

# Create two threads
thread1 = threading.Thread(target=increase_counter)
thread2 = threading.Thread(target=increase_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for the thread to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
print(f"Expected value: 2000000")
