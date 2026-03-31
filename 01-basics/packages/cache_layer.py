import time
import sys
# First import - does actual work
start = time.perf_counter()
import json  # Not yet imported
first_time = time.perf_counter() - start

# Clear from cache to test
del sys.modules['json']

# Second import - from cache
import json  # Re-import
start = time.perf_counter()
import json  # This one is cached
second_time = time.perf_counter() - start

print(f"First import: {first_time:.6f}s")
print(f"Cached import: {second_time:.6f}s")
# First import: 0.000150s
# Cached import: 0.000002s  (75x faster!)