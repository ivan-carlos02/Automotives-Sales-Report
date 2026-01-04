"""
================================
Nama        : Ivan Carlos Tambunan

Script ini untuk membuat DAG untuk mengambil data dari database PostgreSQL, membersihkan data tersebut, dan kemudian memasukkan data ke ElasticSearch.
================================
"""

# Import library
import pandas as pd
import datetime as dt
from datetime import timedelta
from airflow import DAG
from elasticsearch import helpers
from elasticsearch import Elasticsearch
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

# Buat fungsi untuk mengambil dan membersihkan data
def fetching_data():
    """
    Fungsi untuk mengambil data dari database PostgreSQL
    """
    postgres_hook = PostgresHook(postgres_conn_id='postgres_default') # Koneksikan ke PostgreSQL
    
    engine = postgres_hook.get_sqlalchemy_engine() # Ambil data dari tabel

    query = """
            SELECT * 
            FROM table_m3
            """
    try:
        df = pd.read_sql(query, engine) # Buat hasil query ke dalam dataframe
    
        df.to_csv('/opt/airflow/dags/data_raw.csv', index=False) # Simpan data ke file csv raw

    finally:
        engine.dispose() # Tutup koneksi ke database

def data_cleaning():
    """
    Fungsi untuk membersihkan data agar data menjadi mudah dibaca
    """
    df = pd.read_csv('/opt/airflow/dags/data_raw.csv') 

    df = df.dropna() # Drop missing value

    df = df.drop_duplicates() # Drop data duplikat

    df.columns = df.columns.str.lower() # Lowercase semua nama kolom

    df.columns = df.columns.str.replace(r'\d+', '', regex=True) # Hapus angka pada nama kolom

    df['order_product'] = df['ordernumber'].astype(str) + '_' + df['productcode'] # Tambah kolom 'order_product' sebagai unique identifier tiap order + product  
    
    df.to_csv('/opt/airflow/dags/data_clean.csv', index=False) # Simpan data yang sudah dibersihkan ke file csv baru

def upload_elasticsearch():
    """
    Fungsi untuk mengupload data yang sudah dibersihkan ke ElasticSearch
    """
    
    df = pd.read_csv('/opt/airflow/dags/data_clean.csv') # Buat data clean kedalam dataframe
    
    es = Elasticsearch('http://elasticsearch:9200') # Definisikan koneksi ElasticSearch

    # Bulk upload data ke ElasticSearch
    actions = [
        {
        '_index': 'project_m3',
        '_id': r['order_product'],
        '_source': r.to_dict()
        }
    for i, r in df.iterrows()
    ]
    response = helpers.bulk(es, actions) 

# Definisikan default_args untuk DAG
default_args = {
    'owner': 'Ivan',
    'start_date': dt.datetime(2024, 11, 1, 9, 0, 0) - timedelta(hours=7),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=2),
}

# Definisikan DAG
with DAG('project_m3', 
         default_args=default_args,
         schedule_interval='10-30/10 9 * * 6',
         catchup=False
         ) as dag:
    
    fetch_data = PythonOperator(task_id='fetching_data',
                                 python_callable=fetching_data)

    clean_data = PythonOperator(task_id='data_cleaning',
                                python_callable=data_cleaning)

    upload_data = PythonOperator(task_id='post_to_elasticsearch',
                                 python_callable=upload_elasticsearch)
    
fetch_data >> clean_data >> upload_data