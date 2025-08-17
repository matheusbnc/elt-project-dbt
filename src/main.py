import os
from bigquery_connector import BigQueryConnector

if __name__ == "__main__":
    project_id = "etl-project-dbt"
    dataset_name = "bronze"

    # Diretório base do projeto
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, "data", "csv")

    # Lista de arquivos e tabelas
    arquivos_tabelas = [
        {"csv": os.path.join(data_dir, "stg_clientes.csv"), "tabela": "raw_clientes"},
        {"csv": os.path.join(data_dir, "stg_data.csv"), "tabela": "raw_data"},
        {"csv": os.path.join(data_dir, "stg_localidades.csv"), "tabela": "raw_localidades"},
        {"csv": os.path.join(data_dir, "stg_produtos.csv"), "tabela": "raw_produtos"},
        {"csv": os.path.join(data_dir, "stg_vendas.csv"), "tabela": "raw_vendas"},
    ]

    connector = BigQueryConnector(project_id)
    connector.criar_dataset_bq(dataset_name)

    for item in arquivos_tabelas:
        connector.carregar_csv(dataset_name, item["tabela"], item["csv"])
