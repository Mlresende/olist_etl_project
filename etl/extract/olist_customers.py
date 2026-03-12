from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

partition_date = datetime.now().strftime("%Y-%m-%d")

spark = SparkSession.builder.appName("extract_olist_customers").getOrCreate()

raw_df = spark.read.csv("./raw/olist_customers_dataset.csv", header=True)

customers_df = raw_df.select(
    col("customer_id").cast("string").alias("customer_id"),
    col("customer_unique_id").cast("string").alias("customer_unique_id"),
    col("customer_zip_code_prefix").cast("string").alias("customer_zip_code_prefix"),
    col("customer_city").cast("string").alias("customer_city"),
    col("customer_state").cast("string").alias("customer_state"),
    lit(partition_date).cast("string").alias("partition_date")
)

customers_df.write.mode("append").partitionBy("partition_date").parquet(
    "./processed/olist_customers.db"
)