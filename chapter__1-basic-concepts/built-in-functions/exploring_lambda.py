##############################################################################
## Using lambda function to user class object to sort using given condition
##############################################################################


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


# Creating list of Student objects
students = [
    Student("Alice", 20, "A"),
    Student("Bob", 22, "B"),
    Student("Charlie", 21, "C"),
    Student("David", 19, "A"),
]

# User-defined condition: Sort by age
sorted_students_by_age = sorted(students, key=lambda x: x.age)
for student in sorted_students_by_age:
    print(f"{student.name}: Age {student.age}, Grade {student.grade}")  # David: Age 19, Grade A
                                                                        # Alice: Age 20, Grade A
                                                                        # Charlie: Age 21, Grade C
                                                                        # Bob: Age 22, Grade B
    

##############################################################################
## Filtering a List with a Condition
##############################################################################

# Here, we are trying to create a list of even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even Numbers: {even_numbers}") # Even Numbers: [2, 4, 6, 8, 10]

