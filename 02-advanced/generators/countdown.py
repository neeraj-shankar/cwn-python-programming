"""
Implementation of a iterator class that counts downwards till 0
"""
class CountDown:
    """An iterator that counts down from a number"""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """Makes this object iterable - returns the iterator (itself)"""
        return self
    
    def __next__(self):
        """Gets the next value"""

        if(self.current <= 0):
            raise StopIteration
        
        self.current = self.current - 1

        return self.current + 1
# Use it
countdown = CountDown(5)
print(next(countdown))  # 5
print(next(countdown))  # 4
print(next(countdown))  # 3

# Or in a for loop
countdown2 = CountDown(3)
for num in countdown2:
    print(f"T-minus {num}")

