"""
Design a class based decorator, display the execution time and count total number of times
a function being called.
"""

import time


class TimingDecorator:

    def __init__(self, func):
        """
        Takes the function to be decorated.
        """
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwds):

        start = time.perf_counter()

        self.counter += 1
        result = self.func(*args, **kwds)

        end = time.perf_counter()

        print(f"{self.func.__name__} to {end - start:.2f} to execute and its called {self.counter} times")

        return result


# Example use case


@TimingDecorator
def calculator(a, b):
    product = a * b
    print(f"Product of a and b: ", product)
    return product


"""
Implement a class based descriptor that, validates the to be always positive
"""

class PositiveNumber():

    def __init__(self):
        self._values = {}

    def __get__(self, instance, owner):
        print(f"I am owner: {owner} and this my instance: {instance}")
        return self._values.get(instance)
    
    def __set__(self, instance, value):

        if value < 0:
            raise ValueError("Value must be greater than 0")
        
        self._values[instance] = value

# Example usage

class Profile():

    age = PositiveNumber()
        
if __name__ == "__main__":

    # for _ in range(10):
    #     res = calculator(10, 10)

    p = Profile()
    p.age = 20
    print(p.age)