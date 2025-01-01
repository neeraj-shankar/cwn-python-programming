"""
A simple python program to demonstrate the calculation of the string length without counting spaces
"""


class LengthCounter:
    # class variable string to calculate the length
    input_string = "Let's break the ice."

    # using list comprehension and isspace() method
    def first_way(self):
        total_length = sum(not char.isspace() for char in self.input_string)
        print(f"The total length without spaces --> {total_length}")


"""
class object and function calls
"""
test_obj = LengthCounter()
test_obj.first_way()
