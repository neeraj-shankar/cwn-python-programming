"""
------------------------------------------------------------------------------
Problem Statement:
---------------------------------------
Find Key in nested dictionary given which has maximum value

Example
---------------------------------------
stu_data = {
    "First Student": {"Science": 80, "Maths": 76, "English": 95},
    "Second Student": {"Science": 60, "Maths": 94, "English": 97},
    "Third Student": {"Science": 90, "Maths": 72, "English": 67}

}

input_key = Science
output = 90
------------------------------------------------------------------------------
"""

# Approach 1: Using the loop Mechanism
stu_data = {
    "First Student": {"Science": 80, "Maths": 98, "English": 95},
    "Second Student": {"Science": 60, "Maths": 94, "English": 97},
    "Third Student": {"Science": 90, "Maths": 72, "English": 67}

}
max_value = 0
in_key = "Maths"
for v in stu_data.values():
    if v[in_key] > max_value:
        max_value = v[in_key]
print(max_value)

# Using the list comprehenstion and max
max_value = max(v[in_key]  for v in stu_data.values())
print(max_value)

#Using Lambda Function

max_value = max(stu_data, key = lambda sub:  stu_data[sub][in_key])
print(max_value)

res = lambda x: stu_data[x]
print(res)