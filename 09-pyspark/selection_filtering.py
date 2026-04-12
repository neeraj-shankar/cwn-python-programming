from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Data Selection and Filtering").getOrCreate()

# Read File data
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").option("sep", ",").load("sales-data-sample.csv")
df.printSchema()

# Only city and customer name
selected_data = df.select(col("City"), col("CustomerName")).alias("city_and_customer")
selected_data.show(10)