"""
A simple python program to sort the list of student objects list using the age as key
"""


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


a = Student('Ajay', 12, 'Third')
b = Student('Neeraj', 21, 'First')
c = Student('Sahil', 15, 'Second')
d = Student('Asati', 23, 'Second')

stu_list = [a, b, c, d]

# Sort stu_list based on age
sorted_stu_list = sorted(stu_list, key=lambda student: student.age)

# Print the sorted list
for student in sorted_stu_list:
    print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
