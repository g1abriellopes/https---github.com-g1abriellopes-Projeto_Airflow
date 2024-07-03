from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
from plugin.Scripts.Salvar_Excel import Imbaud

def cubo_financeiro():
    imbaud = Imbaud()
    imbaud.salvar_excel()

with DAG(
    'Biancoll',
    start_date=pendulum.datetime(2024, 7, 2, tz="UTC"),
    schedule_interval='@daily',
    catchup=False
) as dag:

    tarefa_executar_cubo_financeiro = PythonOperator(
        task_id='Executar_Cubo',
        python_callable=cubo_financeiro
    )

    tarefa_executar_cubo_financeiro
