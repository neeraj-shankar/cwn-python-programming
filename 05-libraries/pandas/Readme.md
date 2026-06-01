# 🐼 Pandas & 🔢 NumPy — The Complete Field Guide

> A practical reference covering core concepts, real-world use cases, performance patterns, and common pitfalls.  
> Dataset used in examples: `employees.csv` (30 rows, 13 columns)

---

## Table of Contents

1. [NumPy Fundamentals](#1-numpy-fundamentals)
2. [Pandas Fundamentals](#2-pandas-fundamentals)
3. [Data Loading & Inspection](#3-data-loading--inspection)
4. [Selecting & Filtering Data](#4-selecting--filtering-data)
5. [Handling Missing Values](#5-handling-missing-values)
6. [Data Transformation](#6-data-transformation)
7. [GroupBy & Aggregation](#7-groupby--aggregation)
8. [Merging & Joining](#8-merging--joining)
9. [DateTime Operations](#9-datetime-operations)
10. [Pivot Tables & Cross-tabulation](#10-pivot-tables--cross-tabulation)
11. [Performance Optimization](#11-performance-optimization)
12. [Common Pitfalls](#12-common-pitfalls)

---

## 1. NumPy Fundamentals

NumPy is the backbone of scientific computing in Python. Pandas is built on top of it.  
Every pandas column is internally a NumPy array (or an Arrow array in newer versions).

### 1.1 ndarray — The Core Object

```python
import numpy as np

# 1D array
arr = np.array([10, 20, 30, 40, 50])

# 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(arr.shape)      # (5,)
print(matrix.shape)   # (2, 3)
print(arr.dtype)      # int64
```

### 1.2 Array Creation Shortcuts

```python
np.zeros((3, 4))          # 3×4 matrix of 0s
np.ones((2, 5))           # 2×5 matrix of 1s
np.eye(4)                 # 4×4 Identity matrix
np.arange(0, 100, 5)      # [0, 5, 10, ..., 95]
np.linspace(0, 1, 50)     # 50 evenly spaced points between 0 and 1
np.random.seed(42)
np.random.randint(1, 100, size=(5, 5))   # Random integers
np.random.normal(loc=70000, scale=15000, size=100)  # Normal distribution
```

### 1.3 Vectorized Operations (The NumPy Superpower)

```python
salaries = np.array([95000, 72000, 130000, 55000, 80000])

# ALL of these operate element-wise — no Python loops needed
salaries * 1.10           # 10% raise for everyone
salaries - salaries.mean()  # deviation from mean
np.sqrt(salaries)
np.log(salaries)

# Comparison → boolean array
salaries > 80000          # array([True, False, True, False, False])
salaries[salaries > 80000] # fancy indexing: [95000, 130000]
```

> **Why this matters:** A vectorized operation on 1M elements runs in milliseconds.  
> The equivalent Python `for` loop takes seconds.

### 1.4 Broadcasting

Broadcasting allows NumPy to operate on arrays of different shapes automatically.

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)
b = np.array([10, 20, 30]) # shape (3,)

a + b  # b is broadcast across both rows
# array([[11, 22, 33],
#        [14, 25, 36]])
```

### 1.5 Useful Statistical Functions

```python
arr = np.array([45000, 72000, 95000, 130000, 180000])

np.mean(arr)       # 104400.0
np.median(arr)     # 95000.0
np.std(arr)        # standard deviation
np.percentile(arr, 75)   # 75th percentile
np.argmax(arr)     # index of max value → 4
np.cumsum(arr)     # cumulative sum
np.corrcoef(arr, np.arange(5))  # correlation matrix
```

### 1.6 Reshaping & Stacking

```python
arr = np.arange(12)
arr.reshape(3, 4)        # 1D → 2D
arr.reshape(2, 2, 3)     # 1D → 3D
arr.flatten()            # back to 1D (copy)
arr.ravel()              # back to 1D (view, faster)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.vstack([a, b])        # vertical stack → shape (2, 3)
np.hstack([a, b])        # horizontal stack → shape (6,)
np.concatenate([a, b], axis=0)
```

---

## 2. Pandas Fundamentals

### 2.1 Series — 1D Labeled Array

```python
import pandas as pd

# A Series is a NumPy array + an index
s = pd.Series([95000, 72000, 130000], index=["E001", "E002", "E003"], name="salary")

s["E001"]         # 95000  — label-based access
s[0]              # 95000  — position-based access
s[s > 80000]      # filtering
s.mean()          # 99000.0
s.value_counts()  # frequency count
```

### 2.2 DataFrame — 2D Labeled Table

```python
# A DataFrame is a dict of Series sharing the same index
df = pd.DataFrame({
    "name":   ["Aarav", "Priya", "Rohan"],
    "salary": [95000, 72000, 130000],
    "dept":   ["Engineering", "Engineering", "Engineering"]
})

df.shape          # (3, 3)
df.columns        # Index(['name', 'salary', 'dept'])
df.dtypes         # data type of each column
df.index          # RangeIndex(start=0, stop=3)
```

### 2.3 Data Types in Pandas

| Pandas dtype | NumPy equivalent | Best For |
|---|---|---|
| `int64` | `np.int64` | Whole numbers |
| `float64` | `np.float64` | Decimals |
| `object` | varies | Strings, mixed |
| `bool` | `np.bool_` | True/False |
| `datetime64[ns]` | `np.datetime64` | Dates and times |
| `category` | — | Low-cardinality strings (saves memory) |

```python
# Cast to efficient types
df["department"] = df["department"].astype("category")
df["joining_date"] = pd.to_datetime(df["joining_date"])
df["salary"] = df["salary"].astype("int32")   # halves memory vs int64
```

---

## 3. Data Loading & Inspection

### 3.1 Reading Data

```python
# CSV
df = pd.read_csv("employees.csv")

# With options
df = pd.read_csv("employees.csv",
    parse_dates=["joining_date"],   # auto-parse date columns
    dtype={"salary": "int32"},      # specify dtypes upfront
    na_values=["N/A", "None", ""],  # what to treat as NaN
    usecols=["name", "salary", "department"]  # load only needed columns
)

# Excel
df = pd.read_excel("employees.xlsx", sheet_name="Sheet1")

# JSON, Parquet, SQL
df = pd.read_json("data.json")
df = pd.read_parquet("data.parquet")  # fastest format for large data

import sqlite3
conn = sqlite3.connect("company.db")
df = pd.read_sql("SELECT * FROM employees", conn)
```

### 3.2 First Look at the Data

```python
df.head(5)          # first 5 rows
df.tail(5)          # last 5 rows
df.sample(10)       # random 10 rows
df.shape            # (30, 13)
df.info()           # dtypes + non-null counts
df.describe()       # stats for numeric columns
df.describe(include="all")   # stats for ALL columns including strings
df.nunique()        # unique count per column
df.value_counts("department")  # frequency of each department
```

---

## 4. Selecting & Filtering Data

### 4.1 Column Selection

```python
df["salary"]                         # Series
df[["name", "salary", "department"]] # DataFrame (list of columns)
```

### 4.2 Row Selection — loc vs iloc

| | `.loc[]` | `.iloc[]` |
|---|---|---|
| Based on | **Labels** (index values) | **Integer position** |
| Slicing end | **Inclusive** | **Exclusive** (like Python lists) |

```python
df.loc[0, "salary"]              # row label 0, column "salary"
df.loc[0:4, ["name", "salary"]]  # rows 0–4 (inclusive), two columns
df.loc[df["department"] == "Engineering", "salary"]  # filtered rows, one column

df.iloc[0, 3]           # row 0, column index 3
df.iloc[0:5, 0:4]       # first 5 rows, first 4 columns
df.iloc[-1]             # last row
```

### 4.3 Boolean Filtering

```python
# Single condition
df[df["salary"] > 100000]

# Multiple conditions — use & | ~ (NOT "and", "or", "not")
df[(df["salary"] > 80000) & (df["department"] == "Engineering")]
df[(df["is_remote"] == True) | (df["location"] == "Mumbai")]

# .isin() — membership test
df[df["department"].isin(["Engineering", "Finance"])]

# .between() — range check
df[df["salary"].between(60000, 100000)]

# String filtering
df[df["name"].str.startswith("A")]
df[df["job_title"].str.contains("Manager", case=False)]

# .query() — readable SQL-like syntax
df.query("salary > 80000 and department == 'Engineering'")
df.query("experience_years >= 10 and is_remote == True")
```

---

## 5. Handling Missing Values

### 5.1 Detecting Missing Values

```python
df.isnull().sum()           # count NaNs per column
df.isnull().mean() * 100    # % missing per column
df[df["manager_id"].isnull()]  # rows where manager_id is NaN (top-level managers)
```

### 5.2 Filling Missing Values

```python
# Fill with a constant
df["manager_id"].fillna("NO_MANAGER", inplace=True)

# Fill with column statistics
df["salary"].fillna(df["salary"].mean(), inplace=True)
df["performance_score"].fillna(df["performance_score"].median(), inplace=True)

# Forward fill / Backward fill (useful for time series)
df["salary"].ffill()
df["salary"].bfill()

# Fill with group mean (sophisticated)
df["salary"] = df.groupby("department")["salary"].transform(
    lambda x: x.fillna(x.mean())
)
```

### 5.3 Dropping Missing Values

```python
df.dropna()                         # drop rows with ANY NaN
df.dropna(subset=["salary"])        # drop rows where salary is NaN
df.dropna(thresh=10)                # keep rows with at least 10 non-NaN values
df.dropna(axis=1)                   # drop columns with any NaN
```

---

## 6. Data Transformation

### 6.1 Adding & Modifying Columns

```python
# New column from arithmetic
df["monthly_salary"] = df["salary"] / 12
df["salary_after_tax"] = df["salary"] * 0.70

# New column using .apply() with lambda
df["experience_band"] = df["experience_years"].apply(
    lambda x: "Junior" if x <= 3 else ("Mid" if x <= 8 else "Senior")
)

# New column using np.where (vectorized if/else — much faster than apply)
df["level"] = np.where(df["salary"] >= 100000, "Senior IC / Manager", "IC")

# New column using np.select (multi-condition — like switch/case)
conditions = [
    df["experience_years"] <= 2,
    df["experience_years"].between(3, 7),
    df["experience_years"] > 7
]
choices = ["Junior", "Mid-Level", "Senior"]
df["band"] = np.select(conditions, choices, default="Unknown")
```

### 6.2 String Operations (.str accessor)

```python
df["name"].str.upper()
df["name"].str.lower()
df["name"].str.strip()                     # remove whitespace
df["name"].str.split(" ", expand=True)     # split into two columns
df["job_title"].str.replace("Sr.", "Senior")
df["name"].str.len()                       # character count
df["name"].str.extract(r"(\w+)$")         # regex: extract last word (surname)
```

### 6.3 Sorting

```python
df.sort_values("salary", ascending=False)
df.sort_values(["department", "salary"], ascending=[True, False])
df.nlargest(5, "salary")     # top 5 earners — faster than sort + head
df.nsmallest(5, "salary")    # bottom 5
```

### 6.4 Renaming & Dropping

```python
df.rename(columns={"name": "full_name", "dept": "department"}, inplace=True)
df.drop(columns=["monthly_salary", "salary_after_tax"])
df.drop(index=[0, 1, 2])            # drop specific rows
df.reset_index(drop=True)           # reset row index after filtering
```

### 6.5 Binning / Bucketing

```python
# Equal-width bins
df["salary_bucket"] = pd.cut(df["salary"], bins=4,
                              labels=["Low", "Medium", "High", "Very High"])

# Quantile-based bins (equal-frequency)
df["salary_quartile"] = pd.qcut(df["salary"], q=4,
                                 labels=["Q1", "Q2", "Q3", "Q4"])
```

---

## 7. GroupBy & Aggregation

GroupBy is pandas' most powerful analytical tool — split → apply → combine.

### 7.1 Basic GroupBy

```python
# Single aggregation
df.groupby("department")["salary"].mean()
df.groupby("department")["salary"].agg(["mean", "median", "max", "count"])

# Multiple columns
df.groupby(["department", "gender"])["salary"].mean()

# Multiple columns, multiple aggregations
df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
    headcount=("employee_id", "count"),
    avg_experience=("experience_years", "mean")
)
```

### 7.2 transform() — Keep Original Shape

Use `transform()` when you need the result back in the original DataFrame (same index).

```python
# Add dept average salary as a new column
df["dept_avg_salary"] = df.groupby("department")["salary"].transform("mean")

# Compute each employee's salary relative to their dept average
df["salary_vs_dept"] = df["salary"] - df["dept_avg_salary"]
```

### 7.3 filter() — Filter Groups

```python
# Keep only departments with more than 5 employees
df.groupby("department").filter(lambda g: len(g) > 5)
```

### 7.4 apply() on Groups

```python
# Custom function on each group
def top_earner(group):
    return group.nlargest(2, "salary")

df.groupby("department").apply(top_earner)
```

---

## 8. Merging & Joining

### 8.1 merge() — SQL-style Joins

```python
employees = df[["employee_id", "name", "manager_id", "salary"]]
managers  = df[["employee_id", "name"]].rename(columns={"name": "manager_name"})

# Inner join — only matched rows
pd.merge(employees, managers,
         left_on="manager_id", right_on="employee_id",
         how="inner", suffixes=("_emp", "_mgr"))

# Left join — all employees, manager info if available
pd.merge(employees, managers,
         left_on="manager_id", right_on="employee_id", how="left")
```

| Join Type | Keeps |
|---|---|
| `inner` | Only matching rows in BOTH |
| `left` | All left rows, NaN where no match on right |
| `right` | All right rows, NaN where no match on left |
| `outer` | All rows from both, NaN where no match |

### 8.2 concat() — Stack DataFrames

```python
# Stack vertically (new rows)
all_data = pd.concat([df_2023, df_2024], axis=0, ignore_index=True)

# Stack horizontally (new columns)
pd.concat([df_names, df_salaries], axis=1)
```

---

## 9. DateTime Operations

```python
# Parse string column to datetime
df["joining_date"] = pd.to_datetime(df["joining_date"])

# Extract components
df["join_year"]  = df["joining_date"].dt.year
df["join_month"] = df["joining_date"].dt.month
df["join_day"]   = df["joining_date"].dt.day_name()   # "Monday", "Tuesday"...
df["quarter"]    = df["joining_date"].dt.quarter

# Calculate tenure
today = pd.Timestamp.today()
df["tenure_days"]  = (today - df["joining_date"]).dt.days
df["tenure_years"] = df["tenure_days"] // 365

# Resampling (for time-series data — monthly hire count)
df.set_index("joining_date").resample("ME")["employee_id"].count()

# Date filtering
df[df["joining_date"] >= "2020-01-01"]
df[df["joining_date"].dt.year == 2021]
```

---

## 10. Pivot Tables & Cross-tabulation

### 10.1 Pivot Table

```python
# Average salary by department and gender
pd.pivot_table(df,
    values="salary",
    index="department",
    columns="gender",
    aggfunc="mean",
    fill_value=0,
    margins=True   # adds row/column totals
)
```

### 10.2 crosstab() — Frequency Tables

```python
# How many employees per dept × location?
pd.crosstab(df["department"], df["location"])

# As percentages
pd.crosstab(df["department"], df["is_remote"], normalize="index") * 100
```

### 10.3 melt() — Wide to Long (Unpivot)

```python
# Useful when columns are actually values
df_long = pd.melt(df,
    id_vars=["employee_id", "name"],
    value_vars=["salary", "experience_years"],
    var_name="metric",
    value_name="value"
)
```

---

## 11. Performance Optimization

### 11.1 Use Vectorization — Avoid Python Loops

```python
# ❌ Slow — Python loop
for i in range(len(df)):
    df.at[i, "bonus"] = df.at[i, "salary"] * 0.1

# ✅ Fast — Vectorized
df["bonus"] = df["salary"] * 0.1
```

### 11.2 Prefer np.where / np.select over apply()

```python
# ❌ Slow — apply with lambda
df["level"] = df["salary"].apply(lambda x: "High" if x > 100000 else "Low")

# ✅ Fast — np.where (10–50× faster on large data)
df["level"] = np.where(df["salary"] > 100000, "High", "Low")
```

### 11.3 Use category dtype for Strings

```python
# ❌ Default: stores full string for each row
df["department"].dtype  # object — 8 bytes per pointer + string data

# ✅ Category: stores integers + a lookup table
df["department"] = df["department"].astype("category")
# Memory drops 3–10× for low-cardinality string columns
```

### 11.4 Use Efficient Read Options

```python
# Load only what you need
df = pd.read_csv("big_file.csv",
    usecols=["salary", "department"],   # don't load unused columns
    dtype={"salary": "int32"},           # use smaller dtypes
    nrows=10000                          # load a sample first
)
```

### 11.5 Use .str Accessor Instead of apply for Strings

```python
# ❌ Slow
df["name"].apply(lambda x: x.lower())

# ✅ Fast
df["name"].str.lower()
```

### 11.6 Chunked Reading for Large Files

```python
# Process a file too large to fit in memory
results = []
for chunk in pd.read_csv("huge_file.csv", chunksize=50000):
    result = chunk.groupby("department")["salary"].mean()
    results.append(result)

final = pd.concat(results).groupby(level=0).mean()
```

### 11.7 Use Parquet Instead of CSV

```python
# Save as Parquet — 5–10× smaller, 10× faster to read
df.to_parquet("employees.parquet", index=False)
df = pd.read_parquet("employees.parquet")
```

### 11.8 NumPy Performance Over Pandas for Pure Math

```python
# When you only need a fast computation on an array
arr = df["salary"].to_numpy()   # extract as NumPy array
np.percentile(arr, [25, 50, 75])  # faster than df["salary"].quantile()
```

---

## 12. Common Pitfalls

### ⚠️ Pitfall 1: Chained Indexing (SettingWithCopyWarning)

```python
# ❌ Dangerous — may or may not modify the original df
df[df["department"] == "Engineering"]["salary"] = 90000

# ✅ Correct — use .loc always when assigning
df.loc[df["department"] == "Engineering", "salary"] = 90000
```

**Why:** Chained indexing creates an intermediate copy; assignment goes to the copy, not the original DataFrame.

---

### ⚠️ Pitfall 2: Modifying While Iterating

```python
# ❌ Dangerous — never modify a DataFrame you're iterating
for idx, row in df.iterrows():
    df.at[idx, "bonus"] = row["salary"] * 0.1  # works but very slow

# ✅ Correct — vectorize it
df["bonus"] = df["salary"] * 0.1
```

**Also:** `iterrows()` converts each row to a Series — very slow on large datasets. Prefer `itertuples()` if you must iterate, or better yet, use vectorization.

---

### ⚠️ Pitfall 3: Comparing with NaN

```python
# ❌ Wrong — NaN != NaN in Python (IEEE 754 standard)
df[df["manager_id"] == None]   # returns nothing
df[df["manager_id"] == np.nan] # returns nothing

# ✅ Correct
df[df["manager_id"].isnull()]
df[df["manager_id"].notna()]
```

---

### ⚠️ Pitfall 4: Integer Columns with NaN Become float

```python
# Pandas classic gotcha: int + NaN = float64
s = pd.Series([1, 2, None, 4])
s.dtype   # float64 (!)

# ✅ Fix: use nullable integer type (pandas 1.0+)
s = pd.Series([1, 2, None, 4], dtype="Int64")  # capital I
s.dtype   # Int64 — nullable integer
```

---

### ⚠️ Pitfall 5: apply() is Slower Than You Think

```python
# ❌ apply() is essentially a Python loop — slow on large data
df["log_salary"] = df["salary"].apply(np.log)

# ✅ NumPy ufuncs work directly on Series
df["log_salary"] = np.log(df["salary"])   # 10–100× faster
```

---

### ⚠️ Pitfall 6: reset_index() After Filtering

```python
# After filtering, the original index is preserved
engineering = df[df["department"] == "Engineering"]
engineering.index  # [0, 1, 2, 13, 14, 20, ...] — gaps!

# This causes bugs when using .iloc
engineering.iloc[1]  # gives row at position 1, not label 1

# ✅ Always reset after filtering if you'll use iloc
engineering = df[df["department"] == "Engineering"].reset_index(drop=True)
```

---

### ⚠️ Pitfall 7: inplace=True is Not Always Safe

```python
# inplace=True modifies the original — fine in scripts, risky in notebooks
df.sort_values("salary", inplace=True)

# ✅ Prefer assignment — more explicit, works everywhere
df = df.sort_values("salary")

# ⚠️ inplace=True also prevents method chaining
```

---

### ⚠️ Pitfall 8: groupby() Drops NaN Keys by Default

```python
# Rows where the group key is NaN are silently excluded
df.groupby("manager_id")["salary"].mean()
# Top-level managers (NaN manager_id) are NOT in this result!

# ✅ Include NaN groups
df.groupby("manager_id", dropna=False)["salary"].mean()
```

---

### ⚠️ Pitfall 9: Date Parsing Is Not Automatic

```python
df = pd.read_csv("employees.csv")
df["joining_date"].dtype   # object — still a string!

# ✅ Option 1: parse at read time
df = pd.read_csv("employees.csv", parse_dates=["joining_date"])

# ✅ Option 2: convert after loading
df["joining_date"] = pd.to_datetime(df["joining_date"])
```

---

### ⚠️ Pitfall 10: Memory Explosion on Large Merges

```python
# ❌ Merging on a non-unique column creates a cartesian product
# If left has 1M rows and right has 1M rows → 1 Trillion rows

# ✅ Always verify uniqueness before merging
assert df["employee_id"].nunique() == len(df), "Duplicate employee IDs!"
```

---

## Quick Reference Cheat Sheet

```
SELECTION        df["col"] | df[["a","b"]] | df.loc[row, col] | df.iloc[i, j]
FILTERING        df[condition] | df.query("expr") | .isin() | .between()
MISSING          .isnull() | .fillna() | .dropna() | .ffill() | .bfill()
TRANSFORM        .apply() | np.where() | np.select() | .str.xxx | pd.cut()
GROUPBY          .groupby().agg() | .transform() | .filter() | .apply()
MERGE            pd.merge(left, right, on=, how=) | pd.concat([df1, df2])
DATETIME         pd.to_datetime() | .dt.year | .dt.month | .resample()
PIVOT            pd.pivot_table() | pd.crosstab() | pd.melt()
PERFORMANCE      np.where > apply | .astype("category") | read parquet
PITFALLS         .loc for assignment | reset_index | NaN != NaN | parse_dates
```

---

*Happy Data Wrangling! 🚀*