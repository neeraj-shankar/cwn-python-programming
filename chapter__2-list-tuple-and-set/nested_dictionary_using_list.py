"""
A simple python program to create nested dictionary using the list and dictionary itself
"""

####################################################################################################################
# Using the zip anf dict methods
# Time complexity: O(n*n), where n is the length of the test_list. The zip() + loop takes O(n*n) time
# Auxiliary Space: O(n), extra space of size n is required
####################################################################################################################
student_info = {
    "Neeraj": "Computer Science",
    "Asati": "General Science",
    "Gulshan": "No Science",
}

student_passing_year = [2020, 2018, 2098]

resultant_student_info = {}
for key, item in zip(student_passing_year, student_info.items()):
    print(f"The key status --> {key}")
    print(f"The item status --> {item}")
    resultant_student_info[key] = dict([item])

print(f"The resultant nested dictionary is --> {resultant_student_info}")
# output --> {2020: {'Neeraj': 'Computer Science'}, 2018: {'Asati': 'General Science'}, 2098: {'Gulshan': 'No Science'}}


####################################################################################################################
# Using the zip and list comprehension
####################################################################################################################
new_student_info = {index: {key: student_info[key]} for index, key in zip(student_passing_year, student_info)}
print(f"The new nested dictionary --> {new_student_info}")
