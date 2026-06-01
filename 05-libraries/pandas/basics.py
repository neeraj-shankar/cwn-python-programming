
import pandas as pd
"""
===================================================================================================
Basic Operations in Pandas
-------------------------------------------------------------------------------
"""

# Create a hashmap for employee data
employees = {
    "name": ['Alice', 'Joice', 'Margita', 'Sam'],
    "salary": [9000, 8500, 7000, 9600],
    "dept": ['Engineering', 'HR', 'Finance', 'Engineering']

}

# Create a dataframe out of it
emp_df = pd.DataFrame(employees)
print(emp_df)

# Get the dimension of the data 
print(emp_df.shape)

# Get the column names
print(emp_df.columns)

# Get the data types of each column
print(emp_df.dtypes)