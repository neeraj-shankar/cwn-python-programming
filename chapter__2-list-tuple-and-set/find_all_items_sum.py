"""
A simple python program to find the sum of all the items in a dictionary
"""
from format_output import use_case_separator

student_marks = {
    "Neeraj": 100,
    "Ankit": 300,
    "Shankar": 600,
}


#####################################################################################################################
# Using the inbuilt sum() method
#####################################################################################################################


def find_sum_using_sum_method():
    marks_list = []
    for i in student_marks:
        marks_list.append(student_marks[i])

    total_marks = sum(marks_list)
    use_case_separator()
    print(f"The sum of total marks --> {total_marks}")


find_sum_using_sum_method()


#####################################################################################################################
# Using For loop to iterate through values using values() function
#####################################################################################################################
def using_value_method():
    total_marks = 0
    for i in student_marks.values():
        total_marks = total_marks + i

    print(f"The total marks using the value() --> {total_marks}")


use_case_separator()
using_value_method()
