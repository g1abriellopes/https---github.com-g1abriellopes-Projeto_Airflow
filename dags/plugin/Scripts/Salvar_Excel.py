import pandas as pd
from airflow.hooks.base import BaseHook
import os

class Imbaud:
    def __init__(self):
        self.datalake_path = self.get_datalake_path()
        self.download_path = self.get_downloads_path()
    
    def get_datalake_path(self):
        # Pegar a conexão configurada no Airflow para o caminho do DataLake
        connection = BaseHook.get_connection('DataLake')
        return connection.extra_dejson['path']
    
    def get_downloads_path(self):
        # Pegar a conexão configurada no Airflow para o caminho de downloads
        connection = BaseHook.get_connection('Dowload')
        return connection.extra_dejson['path']

    def salvar_excel(self):
        # Montar o caminho completo para o arquivo vendas.parquet
        arquivo = os.path.join(self.datalake_path)
        download = os.path.join(self.download_path)
        
        # Verificar se o arquivo existe antes de tentar lê-lo
        if os.path.exists(arquivo):
            df = pd.read_parquet(arquivo)
            df = df[df['Id Filial'] == 1]
            df.to_excel(download)
            return df
        else:
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")