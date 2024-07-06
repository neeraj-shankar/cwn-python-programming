import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


# Decorator function for logging
def log_function_execution(original_function):
    def wrapper_function(*args, **kwargs):
        logging.info(f"Calling {original_function.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = original_function(*args, **kwargs)
        logging.info(f"{original_function.__name__} returned {result}")
        return result
    return wrapper_function


# Applying the decorator to a function
@log_function_execution
def add_numbers(a, b):
    return a + b


@log_function_execution
def multiply_numbers(a, b):
    return a * b


# Calling the decorated functions
result_sum = add_numbers(3, 5)

result_product = multiply_numbers(4, 6)