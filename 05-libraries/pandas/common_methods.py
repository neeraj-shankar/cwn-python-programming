import pandas as pd

"""
===================================================================================================
1. apply(): 
-----------------------------------------------------------------------------------------
| Object              | Meaning                                |
| ------------------- | -------------------------------------- |
| `Series.apply()`    | Apply function to each value           |
| `DataFrame.apply()` | Apply function row-wise or column-wise |
| `GroupBy.apply()`   | Apply function to each group           |
-----------------------------------------------------------------------------------------

===================================================================================================
"""

"""
======================================= using apply() ============================================
1. Problem Statement:
-----------------------------------------------------------
Given a dataframe of employees with columns name, department, salary. Return a dictionary 
where each salary group is a key and value is list employees name with same salary.
-----------------------------------------------------------
"""

class ApplyUseCases:

    def __init__(self):
        self.df = pd.DataFrame({
            "Employee": ["A", "B", "C", "D", "E", "F"],
            "Age": [25, 30, 25, 40, 30, 25],
            "Salary": [50000, 60000, 50000, 70000, 60000, 50000]
        })


    def get_employee_list(self):
        """
        Salary Bucket
            ↓
        Collect all Employee values
            ↓
        Convert collection into Python list
            ↓
        Return one result per bucket
        """

        #=================================================================
        # Using manaual approach
        # Create groups using salary 
        emp_grouped_by_salary = self.df.groupby("Salary")

        # Iterate each group and put them into dict
        result = {}
        emp_groups = []
        for salary, group_df in emp_grouped_by_salary:
            
            employee_series = group_df["Employee"]
            result[salary] = list(employee_series)
            emp_groups.append(list(employee_series))
        print(result) # {50000: ['A', 'C', 'F'], 60000: ['B', 'E'], 70000: ['D']}
        print(emp_groups) # [['A', 'C', 'F'], ['B', 'E'], ['D']]
        # ================================================================

        # ================================================================
        # Using the pandas apply() method 

        emp_grouped_by_salary = self.df.groupby("Salary") # Create salary bucket 
        result = emp_grouped_by_salary["Employee"].apply(list)
        for  sal, res in result:
            print(sal, res)
        print(dict(result)) # {50000: ['A', 'C', 'F'], 60000: ['B', 'E'], 70000: ['D']}
if __name__ == "__main__":

    auc = ApplyUseCases()

    auc.get_employee_list()