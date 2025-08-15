# Imports
from google.cloud import bigquery
from dotenv import load_dotenv
import os
import logging
from typing import Optional

load_dotenv()
credenciais: Optional[str] = os.getenv("GCP_SERVICE_ACCOUNT")
if credenciais:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credenciais
else:
    raise EnvironmentError("Variável de ambiente 'GCP_SERVICE_ACCOUNT' não encontrada.")

# Configuração de logging
log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "etl_dbt_gcp.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=log_path,
    filemode="a"
)

class BigQueryConnector:
    """
    Classe para conectar e interagir com o Google BigQuery.

    Args:
        project_id (str): ID do projeto GCP.

    Attributes:
        client (bigquery.Client): Cliente BigQuery autenticado.
    """
    def __init__(self, project_id: str) -> None:
        try:
            self.client = bigquery.Client(project=project_id)
            logging.info(f"Cliente BigQuery inicializado para o projeto: {project_id}")
        except Exception as e:
            logging.error(f"Erro ao inicializar o cliente BigQuery: {e}")
            raise

    def criar_dataset_bq(self, dataset_name: str) -> Optional[bigquery.Dataset]:
        """
        Cria um dataset no BigQuery.

        Args:
            dataset_name (str): Nome do dataset a ser criado.

        Returns:
            bigquery.Dataset: Instância do dataset criado ou None em caso de erro.
        """
        dataset_id = f"{self.client.project}.{dataset_name}"
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"
        try:
            dataset = self.client.create_dataset(dataset, exists_ok=True)
            logging.info(f"Dataset criado: {dataset_id}")
            return dataset
        except Exception as e:
            logging.error(f"Erro ao criar dataset '{dataset_id}': {e}")
            return None

    def carregar_csv(self, dataset_name: str, table_name: str, csv_path: str) -> None:
        """
        Carrega um arquivo CSV para uma tabela do BigQuery.

        Args:
            dataset_name (str): Nome do dataset.
            table_name (str): Nome da tabela.
            csv_path (str): Caminho do arquivo CSV.

        Returns:
            None
        """
        table_id = f"{self.client.project}.{dataset_name}.{table_name}"
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            autodetect=True,
            skip_leading_rows=1,
        )
        try:
            with open(csv_path, "rb") as source_file:
                job = self.client.load_table_from_file(
                    source_file, table_id, job_config=job_config
                )
            job.result()  # Aguarda o término do job
            logging.info(f"CSV carregado em: {table_id}")
        except FileNotFoundError:
            logging.error(f"Arquivo CSV não encontrado: {csv_path}")
        except Exception as e:
            logging.error(f"Erro ao carregar CSV para '{table_id}': {e}")
