"""
Implement the Fibonacci sequence recursively and iteratively.

In mathematics, the Fibonacci sequence is a sequence in which each number
is the sum of the two preceding ones. Numbers that are part of the Fibonacci
sequence are known as Fibonacci numbers, 
"""

class FibonacciSeries:
    def __init__(self, data) -> None:
        
        self.data = data

    def find_fibonacci_sequence_iterative(self):
        
        a = 0
        b = 1
        for _ in range(self.data):
            a = b
            b  = a + b
        return a
    

    def find_fibonacci_sequence_recursive(self, n):

        if n <= 1:
            return n
        else:
            return self.find_fibonacci_sequence_recursive(n - 1) + self.find_fibonacci_sequence_recursive(n -2)


if __name__ == "__main__":
    
    number = 5


    result = FibonacciSeries(number).find_fibonacci_sequence_iterative()
    print(f"The sequence for fibonacci number {number}: {result}")

    result = FibonacciSeries(number).find_fibonacci_sequence_recursive(number)
    print(f"The sequence for fibonacci number {number}: {result}")
