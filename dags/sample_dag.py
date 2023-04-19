from airflow import DAG
from airflow.models import Connection
from airflow import settings
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from dependencies.extraction.preProcessing import main as main_tables
from dependencies.extraction.extract import main as main_extraction
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
import subprocess

# Connection parameters
conn_id = 'my_postgres_connection'
conn_type = 'postgres'
host = 'datasource'
login = 'example_user'
password = 'example_password'
schema = 'nbadb'
port = 5432

session = settings.Session()
existing_conn = session.query(Connection).filter(Connection.conn_id == conn_id).first()

if existing_conn:
    print(f"Connection '{conn_id}' already exists. Skipping creation...")
else:
    connection = Connection(
        conn_id=conn_id,
        conn_type=conn_type,
        host=host,
        login=login,
        password=password,
        schema=schema,
        port=port
    )

    session.add(connection)
    session.commit()
    print(f"Connection '{conn_id}' created successfully!")

session.close()

# Python callables:

def _tables_preprocessing():
    main_tables()
    return

def _tables_extraction():
    main_extraction()
    return

def run_flask_app():
    subprocess.run(['python', 'dependencies/load/app.py'])

# DAG structure 

with DAG(
    dag_id='first_sample_dag',
    start_date=datetime(2022, 5, 28),
    schedule_interval=None) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    db_ingestion = PythonOperator(
        task_id="database_ingestion",
        python_callable= _tables_preprocessing
    )

    db_extraction = PythonOperator(
        task_id="extracting_data",
        python_callable= _tables_extraction
    )

    db_transform = PostgresOperator(
        task_id='postgres_transform_data',
        postgres_conn_id='my_postgres_connection',
        sql='dependencies/transformation/sql/join_transform.sql'
    )

    flask_container = PythonOperator(
        task_id='flask_container_build',
        python_callable=run_flask_app,
    )

    end_task = EmptyOperator(
        task_id='end'
    )

start_task >> db_ingestion
db_ingestion >> db_extraction
db_extraction >> db_transform
db_transform >> flask_container
flask_container >> end_task