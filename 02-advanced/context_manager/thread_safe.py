import threading
from contextlib import contextmanager

class ThreadSafeResource:
    def __init__(self):
        self.lock = threading.Lock()  # Create a lock to ensure thread safety
        self.resource = 0  # Some shared resource
    
    def modify_resource(self):
        """Simulates modifying the shared resource."""
        print(f"Resource before modification: {self.resource}")
        self.resource += 1
        print(f"Resource after modification: {self.resource}")

    @contextmanager
    def thread_safe_access(self):
        """Context manager to handle thread-safe access to the shared resource."""
        # Acquire the lock before entering the context
        self.lock.acquire()
        try:
            yield self  # Provide the resource to the `with` block
        finally:
            # Release the lock when exiting the context
            self.lock.release()

# Example usage of the thread-safe context manager
def thread_task(resource):
    with resource.thread_safe_access():
        resource.modify_resource()

# Create a shared resource
shared_resource = ThreadSafeResource()

# Create multiple threads that will access the shared resource
threads = [threading.Thread(target=thread_task, args=(shared_resource,)) for _ in range(5)]

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final value of resource: {shared_resource.resource}")
