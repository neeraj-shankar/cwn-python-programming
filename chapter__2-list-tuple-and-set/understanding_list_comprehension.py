""" 
A simple Python Program to demonstrate list comprehension 

Defination --> It helps creating a new lists by iterating over an existing sequence or iterable objects and applying an expression or condition
 eg --> new_list = [expresssion for item in iterable]           
"""

def undestanding_list_comprehension():
    natural_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Multiple of 5 
    multiple_of_five = [ 5 * num for num in natural_nums]
    print(f"The list number which can be divided by 5 --> {multiple_of_five}")

    # filter only even numbers 
    even_nums = [ num for num in natural_nums if num % 2 == 0]
    print(f"The list of natural numbers as follows --> {even_nums}")



if __name__ == "__main__":

    undestanding_list_comprehension()