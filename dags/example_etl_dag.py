from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('example_etl_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    start = DummyOperator(task_id='start')
    extract = DummyOperator(task_id='extract')
    transform = DummyOperator(task_id='transform')
    load = DummyOperator(task_id='load')
    end = DummyOperator(task_id='end')

    start >> extract >> transform >> load >> end
