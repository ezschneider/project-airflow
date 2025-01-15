from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def hello_world():
    print("Hello, World!")


default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
}

with DAG(
    "hello_world_dag",
    default_args=default_args,
    description="A simple hello world DAG",
    schedule_interval="@hourly",
    catchup=False,
) as dag:
    hello_world_task = PythonOperator(
        task_id="hello_world_task",
        python_callable=hello_world,
        dag=dag,
    )

    hello_world_task
