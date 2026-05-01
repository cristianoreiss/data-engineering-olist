import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# Carregar as variáveis do .env para o ambiente
load_dotenv()

postgres_host = os.getenv("DB_URL")

def extract_and_load(nome_tabela):
    path = f'/usr/local/datasets/{nome_tabela}.csv'
    df = pd.read_csv(path)

    engine = create_engine(postgres_host)
    nome_destino = f'raw_{nome_tabela.replace("olist_","").replace("_dataset","")}'
    df.to_sql(nome_destino,engine,if_exists='replace',index=False)

    print(f"Upload de {nome_tabela} concluído!")


if __name__== "__main__":
    extract_and_load()