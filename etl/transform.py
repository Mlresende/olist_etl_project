from pyspark.sql.functions import col, datediff, to_timestamp, month, count, avg, coalesce, lit, sum as _sum, desc

def prepare_orders(df_order_dataset):
    df_filtered = df_order_dataset \
        .filter(col("order_status") == "delivered") \
        .filter(
            col("order_delivered_carrier_date").isNotNull() &
            col("order_delivered_customer_date").isNotNull() &
            col("order_approved_at").isNotNull()
        )
    df_prepared = df_filtered.withColumn(
        "tempo_entrega_real_dias",
        datediff(col("order_delivered_customer_date"), col("order_purchase_timestamp"))
    )
    return df_prepared

def join_datasets(df_orders, df_order_items, df_products, df_customer):
    df_joined = df_orders.join(df_order_items, "order_id", "left") \
        .join(df_products, "product_id", "left") \
        .join(df_customer, "customer_id", "left")
    return df_joined

def agregacoes(df_joined):
    df_estado = df_joined.groupBy("customer_state") \
        .agg(count("*").alias("quantidade")) \
        .orderBy(desc("quantidade"))

    df_categoria = df_joined.groupBy("product_category_name") \
        .agg(count("*").alias("quantidade")) \
        .orderBy(desc("quantidade"))

    df_mes = df_joined.withColumn("order_approved_at_ts", to_timestamp(col("order_approved_at"), "yyyy-MM-dd HH:mm:ss")) \
        .withColumn("month", month(col("order_approved_at_ts"))) \
        .groupBy("month") \
        .agg(count("*").alias("quantidade")) \
        .orderBy("month")

    return df_estado, df_categoria, df_mes

def calcular_ticket_medio(df_joined):
    df_joined = df_joined.withColumn(
        "price_nonull",
        coalesce(col("price"), lit(0))
    ).withColumn(
        "freight_value_nonull",
        coalesce(col("freight_value"), lit(0))
    ).withColumn(
        "valor_total_frete",
        col("price_nonull") + col("freight_value_nonull")
    )

    ticket_medio_client = df_joined.agg(avg("valor_total_frete").alias("ticket_medio")).collect()[0]["ticket_medio"]
    ticket_medio_pedido = df_joined.agg(avg("price_nonull").alias("ticket_medio")).collect()[0]["ticket_medio"]

    return ticket_medio_client, ticket_medio_pedido
