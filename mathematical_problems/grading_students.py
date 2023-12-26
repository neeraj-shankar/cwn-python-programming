"""
HackerLand University has the following grading policy:

1. Every student receives a grade in the inclusive range from 0 to 100.
2. Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

1. If the difference between the grade and the next multiple of 5 is less than 3, round garde up to the next
multiple of 5 .
2. If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Examples
-----------------------------------------------------------
grade = 84 round to 85 ( 85-84 is less than 3)
grade = 29 do not round ( result is less than 40)
grade = 57 do not round up ( as 60 - 57 is 3 or higher)

"""


class StudentGradingSystem(object):

    """
    Using naive approach to solve the problem
    """
    @staticmethod
    def using_naive_approach(grades):

        updated_grade = []
        for grade in grades:
            remainder_found = grade % 5
            if grade >= 38 and remainder_found >= 3:
                grade = grade - remainder_found + 5
                updated_grade.append(grade)
            else:
                updated_grade.append(grade)

        return updated_grade


"""
Object and function calls
"""
fptr = open("output_file.txt", 'w')

grades_count = int(input().strip())

grades_list = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades_list.append(grades_item)

result = StudentGradingSystem.using_naive_approach(grades_list)
print(f"The grades returned from method --> {result}")
jointed_value = '\n'.join(map(str, result))
print(f"The grades mapped as string --> {jointed_value}")
fptr.write('\n'.join(map(str, result)))
fptr.write('\n')
fptr.close()
