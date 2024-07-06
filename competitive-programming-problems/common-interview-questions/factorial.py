"""
Calculate the factorial of a number
"""


class Factorial:

    def __init__(self, data):
        self.data = data

    def find_factorial_loop(self):

        factorial = 1
        for i in range(1, self.data + 1):
            factorial *= i
        return factorial


if __name__ == "__main__":
    raw_data = 5

    result = Factorial(raw_data).find_factorial_loop()
    print(f"The Factorial of {raw_data}: {result}")
