import pandas as pd 

# Read the csv file and load into dataframe
df = pd.read_csv("employees.csv")

print(df.head(10))

# Group the employees into a list list
result = (
    df.groupby('department_name')['name'].apply(list).to_dict()
)

print(result)