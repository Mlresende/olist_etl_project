from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

partition_date = datetime.now().strftime("%Y-%m-%d")

spark = SparkSession.builder.appName("extract_olist_orders").getOrCreate()

raw_df = spark.read.csv("./raw/olist_orders_dataset.csv", header=True)

orders_df = raw_df.select(
    col("order_id").cast("string").alias("order_id"),
    col("customer_id").cast("string").alias("customer_id"),
    col("order_status").cast("string").alias("order_status"),
    col("order_purchase_timestamp").cast("timestamp").alias("order_purchase_timestamp"),
    col("order_approved_at").cast("timestamp").alias("order_approved_at"),
    col("order_delivered_carrier_date").cast("timestamp").alias("order_delivered_carrier_date"),
    col("order_delivered_customer_date").cast("timestamp").alias("order_delivered_customer_date"),
    col("order_estimated_delivery_date").cast("timestamp").alias("order_estimated_delivery_date"),
    lit(partition_date).cast("string").alias("partition_date")
)

orders_df.write.mode("append").partitionBy("partition_date").parquet(
    "./processed/olist_orders.db"
)