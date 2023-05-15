from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from mage_ai.orchestration.airflow import create_dags
import os


ABSOLUTE_PATH = os.path.abspath(os.path.dirname(__file__))
project_path = os.path.join(ABSOLUTE_PATH, 'mage_projects/demo/demo_etl_pipeline')

create_dags(
    project_path,
    DAG,
    PythonOperator,
    dag_settings=dict(
        start_date=datetime(2022, 8, 5),  # Change this to any start date you want
    ),
    globals_dict=globals(),
)
