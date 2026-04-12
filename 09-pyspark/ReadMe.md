# PySpark

## SparkSession
- The SparkSession is the *"unified entry point"* for any PySpark application.

### Why do we need it?
- Before Spark 2.0, developers had to manage multiple "contexts" depending on what they were doing:

    1. **SparkContext:** For basic RDD operations.

    2. **SQLContext:** For Spark SQL and DataFrames.

    3. **HiveContext:** For working with Hive tables.

- **SparkSession** simplifies this by wrapping all of them into one object. It still creates a SparkContext under the hood, but you rarely need to interact with it directly anymore.

### How to Create a SparkSession?
- To start a PySpark script, you use the **Builder Pattern**. Here is the standard way to initialize it:

```python
from pyspark.sql import SparkSession

# Initialize the SparkSession
spark = SparkSession.builder \
    .appName("MyFirstSparkApp") \
    .master("local[*]") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Your code here...

# Always stop the session when done to free resources
spark.stop()

```

#### Key methods used above:

1. **`.appName():`** Sets a name for your application (visible in the Spark Web UI).

2. **`.master():`** Defines where the cluster is. local[*] means "run locally using all available cores."

3. **`.config():`** Used to set manual configurations (like memory limits or shuffle partitions).

4. **`.getOrCreate():`** This is clever—it returns an existing session if one is already running, otherwise it creates a new one.


## READ/WRITE

### The READ Concept **(DataFrameReader)**
When you read data, you are pulling external data into a Spark DataFrame. Spark is "lazy," meaning it doesn't actually load the data into memory the moment you run the command; it just creates a pointer and a plan for how to read it.

```python
df = spark.read \
    .format("format") \
    .option("key", "value") \
    .schema(user_defined_schema) \
    .load("path")
```
- **Format:** csv, json, parquet, orc, jdbc (for databases), or delta.
- **Options:** Specific configurations like header=True for CSVs or multiLine=True for JSON.
- **Schema:** (Optional but recommended) Telling Spark exactly what the columns and types are.
- **Load:** The physical path to the file or folder.

### The WRITE Concept **(DataFrameWriter)**
Once you have processed your data in a DataFrame, you need to save it back to storage. This is where you define how and where the data should live.

```python
df.write \
    .format("format") \
    .mode("saveMode") \
    .option("key", "value") \
    .save("path")
```

- When writing, you must tell Spark what to do if the destination folder already exists. This is controlled by .mode():

| Mode      | Behavior                                                                   |
| --------- | -------------------------------------------------------------------------- |
| overwrite | Deletes existing data and replaces it with the new DataFrame.              |
| append    | Adds the new data to the existing files in the folder.                     |
| ignore    | If data exists, Spark does nothing (no error, no write).                   |
| error     | (Default) Throws an error if the path already exists to prevent data loss. |


### Comparison: JSON vs. CSV in Spark

| Feature      | CSV                              | JSON                                    |
| ------------ | -------------------------------- | --------------------------------------- |
| Schema       | External (must infer or provide) | Self-describing (keys are column names) |
| Nested Data  | Not supported (Flat rows only)   | Supported (Structs and Arrays)          |
| Speed        | Generally faster to read         | Slower due to parsing braces/keys       |
| Standard Use | Legacy systems / Simple tables   | APIs / Web logs / Nested structures     |


## Data Transformations
PySpark DataFrame operations are divided into two main categories: **Transformations** and **Actions**.

### **1. The Core Concept: Transformations vs. Actions**
Spark uses Lazy Evaluation, meaning it doesn't execute your code until you absolutely ask for a result.

- **Transformations:** These create a new DataFrame from an existing one (e.g., filtering, selecting). They are "lazy" and just build a plan.
- **Actions:** These trigger the actual computation and return a result to the driver or save it to storage (e.g., show(), count(), write).

### 2. Common Transformations

#### A. Selecting and Renaming

```python
# Selecting columns
df.select("name", "price").show()

# Renaming a column
df = df.withColumnRenamed("profit", "earnings")
```

#### B. Filtering (Where)

```python
# Filter for high price products
high_price_df = df.filter(df["price"] > 2000)

# Multiple conditions
df.filter((df["price"] > 2000) & (df["name"] == "Ankit")).show()
```

#### C. Adding New Columns (withColumn)

```python
# Calculate Total Cost (Price + Profit)
df = df.withColumn("total_cost", df["price"] + df["profit"])
```

#### D. Grouping and Aggregating

```python
from pyspark.sql import functions as F

# Group by product and find average price
df.groupBy("product").agg(F.avg("price").alias("avg_price")).show()
```

### 3. Common Actions

| **Action**   | **Description**                                                                             |
| ------------ | ------------------------------------------------------------------------------------------- |
| `.show(n)`   | Prints the first **n rows** in a readable table format (default is 20).                     |
| `.count()`   | Returns the **total number of rows** in the DataFrame (triggers full computation).          |
| `.collect()` | ⚠️ **Danger:** Pulls **all data to driver memory**. Use only on small or filtered datasets. |
| `.first()`   | Returns the **first row** as a `Row` object (useful for quick checks).                      |
| `.write`     | Saves the DataFrame to **storage systems** (file, DB, etc.), e.g., CSV, Parquet.            |


## Pyspark - Advanced

### Window Functions

Window functions allow you to perform calculations across a "window" of rows related to the current row, without collapsing them into a single output row (like a standard groupBy does).

- **The Components:** You need a WindowSpec defined by partitionBy() (grouping), orderBy() (sorting), and optionally rowsBetween() (framing).

- **Common Functions:** `rank()`, `dense_rank()`, `row_number()`, and lead/lag analytics.

#### Standard group by vs window function
- **groupBy:** Reduces the number of rows. If you group by "Department," you get exactly one row per department. You lose the individual employee details.
- **Window Function:** Maintains the original row count. You get the aggregate (like a sum or average) attached to every single row in the original dataset.

| Function | Input Rows | Output Rows    | Purpose                                   |
| -------- | ---------- | -------------- | ----------------------------------------- |
| Group By | 1,000      | 5 (if 5 depts) | Summary reports, aggregations, totals     |
| Window   | 1,000      | 1,000          | Rankings, running totals, moving averages |

- **Directional Calculations:** 
    - Standard groupBy is "unordered." It just looks at a bucket of data and sums it up.

    - Window Functions allow for ordering, which enables "directional" logic that groupBy simply cannot do, such as:
        1. Running Totals: Adding today's sales to all previous days' sales.
        2. Lead/Lag: Looking at what the sales were yesterday compared to today on the same row.
        3. Ranking: Finding the top 3 performers within each group.