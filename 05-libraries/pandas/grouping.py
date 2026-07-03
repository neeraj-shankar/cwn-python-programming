import pandas as pd

"""
===================================================================================================

Basic Operations using Group by in Pandas
-----------------------------------------------------------
Basic Syntax: df.groupby('column_name')
"""


# Read the CSV File and load into dataframe
# df = pd.read_csv('employees.csv', encoding='utf-8', usecols=['emp_code', 'name', 'age', 'salary'])


df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E", "F", "G"],
    "Age": [25, 30, 25, 40, 30, 25, 35],
    "Salary": [50000, 60000, 50000, 70000, 60000, 50000, None]
})

print(df.dtypes)
# Basic grouping by employee salary
group_by_sal = df.groupby('Salary')
print(group_by_sal.head())

# Get Employees and Age count based on common salary
print("******************************")
print(group_by_sal.count())

# Get the count of employees having same salary
print("******************************")
print(group_by_sal.size())

# Get Employees getting same salary
emp_with_same_sal = group_by_sal.get_group(50000)
print(emp_with_same_sal)

# Another Interesting example if we want see list employees having same salary
print(group_by_sal['Employee'].apply(list))
