"""
Implementation of a iterator class that counts downwards till 0

How it works under the hood:
-------------------------------------------------
1. When you start the for loop, Python calls iter(counter), which triggers __iter__.

2. In each iteration, Python calls next(counter), which triggers __next__.

3. The class keeps track of its own state (self.current) between calls.

4. When self.current hits 0, the StopIteration exception is raised, and the loop ends gracefully.
-------------------------------------------------
"""

class CountDown:

    def __init__(self, start):
        
        self.current = start

    def __iter__(self):

        return self
    
    def __next__(self):

        # Validation to check stop when value goes less than or equal to 0
        if self.current <=0:
            raise StopIteration
        
        # Store the Value so that it can be returned
        value = self.current

        # Decrement the value of the current state
        self.current -= 1

        # Finally Return the value
        return value
    
if __name__ == "__main__":

    counter = CountDown(5)

    print(type(counter)) # <class '__main__.CountDown'>
    print(counter) # <__main__.CountDown object at 0x102a00fd0>

    for _ in range(5):
        print(counter.current)

    for num in counter:
        print(num)