class SuppressError:
    def __enter__(self):
        print("Entering context...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Suppressed Exception: {exc_value}")
            return False  # Suppress the exception

# Using the context manager
with SuppressError():
    print("Inside the block...")
    raise ValueError("An intentional error!")  # This will be suppressed
print("Execution continues...")
