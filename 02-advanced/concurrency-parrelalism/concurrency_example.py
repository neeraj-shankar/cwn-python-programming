import time
import requests

def fetch_data(api_id):
    print(f"[{time.time():.2f}] Starting API {api_id}")
    
    # Simulate CPU work (preparing request)
    start = time.time()
    _ = sum(i**2 for i in range(100000))  # CPU work
    cpu_time = time.time() - start
    print(f"[{time.time():.2f}] API {api_id}: CPU work done ({cpu_time:.3f}s)")
    
    # Simulate I/O wait (network request)
    print(f"[{time.time():.2f}] API {api_id}: Waiting for network...")
    time.sleep(2)  # Network I/O
    
    print(f"[{time.time():.2f}] API {api_id}: COMPLETE ✓")
    return f"Data from API {api_id}"

# Sequential execution
print("=" * 60)
print("SEQUENTIAL EXECUTION")
print("=" * 60)

start_time = time.time()

result1 = fetch_data(1)
result2 = fetch_data(2)
result3 = fetch_data(3)

total_time = time.time() - start_time
print(f"\n⏱️  Total time: {total_time:.2f}s")