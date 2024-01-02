
from function_based_decorators import timing_decorator, log_function_call

@timing_decorator
@log_function_call
def add(x, y):
    sum = x + y
    return sum


if __name__ == "__main__":
    a = 10
    b = 70
    result = add(a, b)
    print(result)