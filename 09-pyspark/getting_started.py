from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("My App").getOrCreate()

print(spark)