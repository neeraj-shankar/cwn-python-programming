"""
Basic python program to understand decorators in python

Here's a more practical example of a decorator that measures the execution time of a function:

"""
import time


def measure_time(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        print(f"The {original_function.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper_function()


@measure_time
def find_sum():
    num1 = 2
    num2 = 3
    total_sum = num1 + num2
    time.sleep(2)
    print(f"The sum of the two number is --> {total_sum}")


find_sum()

