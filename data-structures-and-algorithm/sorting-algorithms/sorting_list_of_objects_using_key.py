"""
This is a simple python program to sort the list of students object using their age
"""


class SortingStudentsList(object):

    # constructor to initialize the students
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    """
    Using the inbuilt sorted method
    """