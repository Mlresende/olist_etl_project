from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

partition_date = datetime.now().strftime("%Y-%m-%d")

spark = SparkSession.builder.appName("extract_olist_order_items").getOrCreate()

raw_df = spark.read.csv("./raw/olist_order_items_dataset.csv", header=True)

orders_items_df = raw_df.select(
    col("order_id").cast("string").alias("order_id"),
    col("order_item_id").cast("string").alias("order_item_id"),
    col("product_id").cast("integer").alias("product_id"),
    col("seller_id").cast("string").alias("seller_id"),
    col("shipping_limit_date").cast("timestamp").alias("shipping_limit_date"),
    col("price").cast("double").alias("price"),
    col("freight_value").cast("double").alias("freight_value"),
    lit(partition_date).cast("string").alias("partition_date")
)
orders_items_df.write.mode("append").partitionBy("partition_date").parquet(
    "./processed/olist_order_items.db"
)