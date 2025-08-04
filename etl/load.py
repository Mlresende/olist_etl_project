def save_aggregations(df_estado, df_categoria, df_mes, output_path=r".\data\processed"):
    df_estado.coalesce(1).write.mode("overwrite").csv(f"{output_path}/estado", header=True)
    df_categoria.coalesce(1).write.mode("overwrite").csv(f"{output_path}/categoria", header=True)
    df_mes.coalesce(1).write.mode("overwrite").csv(f"{output_path}/mes", header=True)