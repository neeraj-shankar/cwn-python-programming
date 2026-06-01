import pandas as pd

"""
===================================================================================================
Section A: Reading Data from csv file
---------------------------------------------------------------------
Useful Arguments for pd.read_csv
-------------------------------------------------
1. sep --> when csv file is not "," seperated we use other separator like |, \t, etc
2. header --> Controls which row is treated as header, header=0, first row = column names
3. names --> Manually assign column names 
4. usecols --> only loads selected columns.
5. nrows --> loads only first n rows
6. index_col --> set a column as dataframe index. one column that uniquely idenfies a row
7. dtype --> passed as dict, helps set dtypes of specified column in the dict.
8. parse_dates --> Automatically convert to date columns
9. encoding --> Handles special characters.
10. chunksize --> Read huge files in chunks.
11. compression --> Read compress file directly. compression="gzip" for csv.gz
===================================================================================================
"""

# Read data from csv file and load into dataframe
employees_df = pd.read_csv("./employees.csv")
print(employees_df.head(5))

# Production style reading
df = pd.read_csv(
    "employees.csv",
    usecols=["emp_code", "name", "salary", "joining_date"],
    dtype={"employee_id": str},
    parse_dates=["joining_date"],
    na_values=["NA", "null"],
    encoding="utf-8"
)
print(df.head(5))

###############################################################################
############################# Common Dataframe Properties #####################
###############################################################################
# Get the shape --> dimension of the dataframe
print(f"Dimnesion of the dafarame: {df.shape}")
# Get the column names of the dataframe
print(f"Columns in the dataframe: \n {df.columns}")
# Check the data type of each column of the dataframe
print(f"Data types of the columns in the dataframe: \n{df.dtypes}")
print(df.describe(include="all"))