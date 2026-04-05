from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read File App").getOrCreate()

# Reading a CSV File with common options
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").option("sep", ",").load("sales-data-sample.csv")

df.show()
df.printSchema()

print("Priting Available columns")
print(df.columns)

for col in df.columns:
    df = df.withColumnRenamed(col, col.strip())

#Filter and save data'
high_sales_df = df.filter(df["Profit"] > 50)
high_sales_df.show()

# Writing the result back to a CSV
high_sales_df.write.format("csv").mode("overwrite").option("header", "true").save("high_profit_sales")

# Always stop the session
spark.stop()