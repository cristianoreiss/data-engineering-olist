from datetime import timedelta
from include.extract_and_load import extract_and_load
from airflow.sdk import Asset, dag, task
from pendulum import datetime

@dag(
    start_date = datetime(2026, 5, 1, 9),
    schedule = "@daily",
    default_args={
        "owner":"Cristiano",
        "retries": 2,
        "retry_delay": timedelta(minutes=5)
    },
    catchup=False
)
def pipeline_olist():

    @task
    def task_extract_and_load():
        TABELAS_OLIST = [
            'olist_customers_dataset',
            'olist_geolocation_dataset',
            'olist_order_items_dataset',
            'olist_order_payments_dataset',
            'olist_order_reviews_dataset',
            'olist_orders_dataset',
            'olist_products_dataset',
            'olist_sellers_dataset',
            'product_category_name_translation'
        ]

        for nome_tabela in TABELAS_OLIST:
            extract_and_load(nome_tabela)
    
    @task
    def task_load_staging():
        pass

    task_extract_and_load() >> task_load_staging()

pipeline_olist()