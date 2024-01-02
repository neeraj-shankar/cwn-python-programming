import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Program Start Point: {start_time}")
        result = func(*args, **kwargs)
        time.sleep(1)
        end_time = time.time()
        print(f"Program end Point: {start_time}")
        print(f"{func.__name__} took: {end_time - start_time} seconds.")
        return result
    return wrapper


def log_function_call(original_function):
    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        print(f"Called {original_function.__name__} with positional args {args} and keyword arguments {kwargs}")
        return result
    return wrapper