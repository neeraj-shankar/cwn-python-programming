"""
Different Ways of reversing a string

1. Using the slicing option

"""

class ReversingString:

    def __init__(self, in_str):
        self.in_str = in_str
    
    def using_slicing_way(self):

        reversed_str = self.in_str[::-1]
        return reversed_str

    def using_reversed_method(self):
        reversed_str = ''.join(reversed(self.in_str))
        return reversed_str
    
    def using_loop_way(self):
        reversed_string = ''
        for chr in self.in_str:
            reversed_string = chr + reversed_string
        return reversed_string
    
if __name__ == "__main__":
    
    input_string = "abc"    

    result = ReversingString(input_string).using_slicing_way()
    print(f"Reversed String with Slicing: {result}")

    result = ReversingString(input_string).using_reversed_method()
    print(f"Reversed String with Reversed Method: {result}")

    result = ReversingString(input_string).using_loop_way()
    print(f"Reversed String with Loop: {result}")


