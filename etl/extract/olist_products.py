from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

partition_date = datetime.now().strftime("%Y-%m-%d")

spark = SparkSession.builder.appName("extract_olist_products").getOrCreate()

raw_df = spark.read.csv("./raw/olist_products_dataset.csv", header=True)

products_df = raw_df.select(
    col("product_id").cast("string").alias("product_id"),
    col("product_category_name").cast("string").alias("product_category_name"),
    col("product_name_lenght").cast("integer").alias("product_name_lenght"),
    col("product_description_lenght").cast("integer").alias("product_description_lenght"),
    col("product_photos_qty").cast("integer").alias("product_photos_qty"),
    col("product_weight_g").cast("double").alias("product_weight_g"),
    col("product_length_cm").cast("double").alias("product_length_cm"),
    col("product_height_cm").cast("double").alias("product_height_cm"),
    col("product_width_cm").cast("double").alias("product_width_cm"),
    lit(partition_date).cast("string").alias("partition_date")
)

products_df.write.mode("append").partitionBy("partition_date").parquet(
    "./processed/olist_products.db"
)