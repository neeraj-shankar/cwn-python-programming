"""
Sorting Complex Data:
Imagine you have a list of employees and need to sort them by different criteria:
"""

employees = [
    {'name': 'Alice', 'age': 30, 'salary': 70000},
    {'name': 'Bob', 'age': 25, 'salary': 65000},
    {'name': 'Charlie', 'age': 35, 'salary': 80000}
]

sorted_by_salary = sorted(employees, key=lambda emp: emp['salary'], reverse=False)
names = [emp['name'] for emp in sorted_by_salary]
print(sorted_by_salary)
print(names)