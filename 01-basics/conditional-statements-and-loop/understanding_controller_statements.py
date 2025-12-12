##############################################################################
## for Statement: iterates over the elements of a sequence
## (such as a list, tuple, or string).
## Example: Create a program to calculate averge height
##############################################################################

students_data = {
    "student1": {"name": "Alice", "marks": 95, "age": 18},
    "student2": {"name": "Bob", "marks": 88, "age": 19},
    "student3": {"name": "Charlie", "marks": 75, "age": 17},
    "student4": {"name": "David", "marks": 92, "age": 20},
    "student5": {"name": "Eva", "marks": 85, "age": 18},
    "student6": {"name": "Frank", "marks": 78, "age": 19},
    "student7": {"name": "Grace", "marks": 94, "age": 20},
    "student8": {"name": "Henry", "marks": 89, "age": 18},
    "student9": {"name": "Ivy", "marks": 82, "age": 17},
    "student10": {"name": "Jack", "marks": 91, "age": 19},
}

overall_marks = 0
student_count = 0

# Loop through the student data and print average marks for entire data set
for record in students_data.values():
    student_count += 1
    print(f"Record: {record}")
    for subkey in record.keys():
        if subkey == "marks":
            overall_marks += record.get("marks")
    average_mark = overall_marks / student_count
    print(f"Averge of marks: {average_mark}")  # Averge of marks: 86.9


##############################################################################
## if-else Statement: If the condition is true, the indented block of code is
## executed. Otherwise the else part
## Example: FizzBuzz Game: The program should print number from 1 to 100. But
## when a number divisible by 3, print message should Fizz.
## when the number is divisible by 5 then its called Buzz
## if the number is divisible by both 3 and 5 its called Fizzbuzz
##############################################################################

for num in range(1, 101, 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)


##############################################################################
## for-else controll statement: The else clause in a loop is executed when the
## loop condition becomes false
## This can help use handle cases when we want check if all elements matches
## a certain condition before we take action on them
##############################################################################

# check if all numbers in a list are positive
numbers = [2, 5, 1, 10]

for num in numbers:
    if num <= 0:
        print(f"All numbers in the are not positive")
        break
else:
    print(f"All numbers are positive")  # All numbers are positive

##############################################################################
## match statement: A match statement takes an expression and compares its
## value to successive patterns given as one or more case blocks
## Example: The program to validate different status codes
##############################################################################


def http_error(status):
    match status:
        case 400:
            print(f"Message: {status}: Bad Request.")
        case 404:
            print(f"Message: {status}: Resource Not Found.")
        case _:
            # gets executed when none of the case matches
            print(f"Message: {status}: The status code is not valid.")


# making the function call with input data

input_status = 404
http_error(input_status)  # Message: 404: Resource Not Found.

##############################################################################
## enumerate is a built-in function in Python that is used to iterate over a 
## sequence (such as a list, tuple, or string) along with an index, providing 
## both the item and its position.
## Syntax: enumerate(iterable, start=0)
##############################################################################

fruits = ["Apple", "Orange", "Mango", "Blueberry"]

print(list(enumerate(fruits))) # [(0, 'Apple'), (1, 'Orange'), (2, 'Mango'), (3, 'Bluberry')]

for index, fruit in enumerate(fruits, start=0):
    print(f"Index: {index}, Value: {fruit}")
