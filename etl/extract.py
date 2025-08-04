from pyspark.sql import SparkSession

def load_data(spark, base_path=r".\data\raw"):
    df_customer = spark.read.option("header", "true").option("inferSchema", "true").csv(f"{base_path}/olist_customers_dataset.csv")
    df_order_items = spark.read.option("header", "true").option("inferSchema", "true").csv(f"{base_path}/olist_order_items_dataset.csv")
    df_order_dataset = spark.read.option("header", "true").option("inferSchema", "true").csv(f"{base_path}/olist_orders_dataset.csv")
    df_products = spark.read.option("header", "true").option("inferSchema", "true").csv(f"{base_path}/olist_products_dataset.csv")
    return df_customer, df_order_items, df_order_dataset, df_products
