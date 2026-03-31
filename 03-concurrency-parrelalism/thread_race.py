import threading
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | PID:%(process)d | TID:%(thread)d | %(funcName)s | %(levelname)s | %(message)s"
)

# The Shared resource
counter = 0

def increase_counter():
    global counter
    logging.info(f"Task is being executed...")
    for _ in range(100000000):
        # This looks like one step, but the CPU sees 3 steps:
        # 1. Read 'counter' from RAM
        # 2. Add 1 to it
        # 3. Write 'counter' back to RAM
        counter += 1


# Create two threads
thread1 = threading.Thread(target=increase_counter)
thread2 = threading.Thread(target=increase_counter)

# Start them
thread1.start()
thread2.start()

# Wait for both to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
print(f"Expected value: 2000000")