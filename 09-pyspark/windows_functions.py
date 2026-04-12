from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as F
# Initialize the spark session 
spark = SparkSession.builder.appName("Windows Functions").getOrCreate()

# Load CSV file
df = spark.read.csv('simple-sales-data.csv', header=True, inferSchema=True)

df.show(5)

# Standard group by vs window function

print("=========================Standard Group By ==================================")
df.groupBy("department").agg(F.sum("sales")).show()

print("========================= WINDOWS FUNCTION ==================================")
windowspec = Window.partitionBy("department")
df.withColumn("dept_total", F.sum("sales").over(windowspec)).show()

# Define the window specification
# This groups department and orders by date
windowspec = Window.partitionBy("department").orderBy("date")

# Apply the running total
result_df = df.withColumn("running total", F.sum("sales").over(windowspec))

# Show the result
result_df.orderBy("department", "date").show()

spark.stop()