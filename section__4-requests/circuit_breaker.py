"""
1. CLOSED → normal operation
2. OPEN → fail fast, don’t call API
3. HALF_OPEN → test if API recovered

Key Intution
------------------
A circuit breaker wraps an external call:
Client → CircuitBreaker → External API

Key Rules to follow the for circuit breaker
-----------------------------------------------------------
1. If failures exceed threshold → OPEN
2. While OPEN → immediately reject calls
3. After timeout → go to HALF_OPEN
4. If success → CLOSED
5. If failure → OPEN again
"""

import time
from enum import Enum
import threading

class State(Enum):
    CLOSED = 'closed'
    OPEN = 'open'
    HALF_OPEN = 'half_open'

class CircuitBreaker():

    def __init__(self, failure_threshold, recovery_timeout, success_threshold):
        
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold

        self.state = State.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None

        self.lock = threading.Lock()

    
    def _can_attempt(self):

        if self.state == State.OPEN:
            if time.time() - self.last_failure_time >= self.recovery_timeout:
                self.state = State.HALF_OPEN

                return True 
            return False
        return True
    
    def call(self, func, *args, **kwargs):

        with self.lock:
            if not self._can_attempt():
                raise Exception("Circuit is open. Failing fast.")
            
        
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            self._on_failure()
            raise e
        
        self._on_success()
        return result
    
    def _on_failure(self):

        with self.lock():
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = State.OPEN
                print("Circuit moved to OPEN.")


    def _on_success(self):

        with self.lock():

            if self.state == State.HALF_OPEN:
                self.success_count += 1

                if self.success_count >= self.success_threshold:
                    self._reset()
            else:
                self.failure_count = 0

    def _reset(self):
        print("Circuit reset to CLOSED")
        self.state = State.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None

if __name__ == "__main__":

    import random

    def unstable_api():
        if random.random() < 0.7:
            raise Exception("API failed")
        return "Success"


    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=5)

    for i in range(15):
        try:
            print("Call:", cb.call(unstable_api))
        except Exception as e:
            print("Error:", e)
        time.sleep(1)



