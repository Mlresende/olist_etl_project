from pyspark.sql import SparkSession
from etl.extract import load_data
from etl.transform import prepare_orders, join_datasets, agregacoes, calcular_ticket_medio
from etl.load import save_aggregations

def main():
    spark = SparkSession.builder.appName("olist_etl").getOrCreate()

    df_customer, df_order_items, df_order_dataset, df_products = load_data(spark)
    df_orders_prepared = prepare_orders(df_order_dataset)
    df_joined = join_datasets(df_orders_prepared, df_order_items, df_products, df_customer)

    # Mostrar schema para debug
    df_joined.printSchema()

    df_estado, df_categoria, df_mes = agregacoes(df_joined)
    save_aggregations(df_estado, df_categoria, df_mes)

    ticket_medio_client, ticket_medio_pedido = calcular_ticket_medio(df_joined)
    print(f"Ticket médio (preço + frete): R$ {ticket_medio_client:.2f}")
    print(f"Ticket médio (somente preço): R$ {ticket_medio_pedido:.2f}")

if __name__ == "__main__":
    main()
