# Implement a rate limiter that only allow function call every 5 seconds
import time

def rate_limiter(seconds):
    last_called = 0
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal last_called 
            elapsed = time.time() - last_called
            
            if elapsed < seconds:
                print(f"Hold on. you can request after {seconds - elapsed:.2f} seconds")
                return 
            
            last_called = time.time()
            return func(*args, **kwargs)
            
        return wrapper
    return decorator
    

@rate_limiter(4)
def fetch_data():
    print(f"Going online to fetch data")
    return f"Successful"
    
for _ in range (5):
    fetch_data()
    time.sleep(2)