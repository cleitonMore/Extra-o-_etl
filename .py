import requests
import pandas as pd
import sqlite3
from datetime import datetime
import os

# Função de Extração de Dados da API CoinGecko
def extract_data():
    api_url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',  # Moeda de referência (USD)
        'order': 'market_cap_desc',  # Ordenar por capitalização de mercado
        'per_page': 10,  # Quantas criptomoedas por página
        'page': 1,  # Número da página
        'sparkline': False  # Sem dados de gráfico histórico
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Verifica se há erros HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

# Função de Transformação de Dados
def transform_data(data):
    if not data:
        print("Nenhum dado retornado pela API.")
        return pd.DataFrame()  # Retorna DataFrame vazio

    # Converter dados para DataFrame
    df = pd.DataFrame(data)

    # Selecionar colunas relevantes
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'high_24h', 'low_24h', 'price_change_percentage_24h']]

    # Adicionar a data de extração
    df['data_extracao'] = datetime.now()

    return df

# Função de Carga em Banco de Dados Temporário (in-memory)
def save_to_temp_sqlite(df):
    if df.empty:
        print("DataFrame vazio. Nenhum dado será carregado.")
        return

    # Conectar ao banco de dados temporário na memória
    conn = sqlite3.connect(':memory:')  # Cria o banco de dados temporário na memória

    # Salvar os dados no banco de dados temporário
    df.to_sql('cryptocurrencies', conn, if_exists='replace', index=False)

    # Verificar se os dados foram carregados corretamente
    print("Dados salvos no banco de dados temporário na memória.")

    # Fazer uma consulta no banco de dados temporário para exibir os dados
    query_result = pd.read_sql('SELECT * FROM cryptocurrencies', conn)
    print("Dados recuperados do banco de dados temporário:")
    print(query_result.head())

    # Fechar a conexão ao banco de dados temporário (será descartado após o fechamento)
    conn.close()

# Função de Carga em CSV
def save_to_csv(df, output_dir):
    if df.empty:
        print("DataFrame vazio. Nenhum dado será salvo.")
        return

    filepath = os.path.join(output_dir, 'cryptocurrencies.csv')
    df.to_csv(filepath, index=False)
    print(f"Dados salvos com sucesso no arquivo CSV: {filepath}")

# Função de Carga em Parquet
def save_to_parquet(df, output_dir):
    if df.empty:
        print("DataFrame vazio. Nenhum dado será salvo.")
        return

    filepath = os.path.join(output_dir, 'cryptocurrencies.parquet')
    df.to_parquet(filepath, index=False)
    print(f"Dados salvos com sucesso no arquivo Parquet: {filepath}")

# Função para criar diretório na Área de Trabalho
def create_desktop_directory():
    # Obtém o caminho da área de trabalho
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    # Define o nome da pasta onde os dados serão salvos
    folder_name = "Dados salvos do projeto do Cleiton"
    output_dir = os.path.join(desktop_path, folder_name)

    # Verifica se a pasta já existe, se não, cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    return output_dir

# Pipeline ETL com Opções de Salvamento
def etl_pipeline():
    # Extração
    data = extract_data()

    # Transformação
    transformed_data = transform_data(data)

    # Cria o diretório na Área de Trabalho
    output_dir = create_desktop_directory()

    # Perguntar ao usuário como deseja salvar os dados
    print("\nComo você gostaria de salvar os dados?")
    print("1. Banco de Dados Temporário (memória)")
    print("2. CSV")
    print("3. Parquet")
    save_option = input("Escolha uma opção (1/2/3): ").strip()

    # Carga conforme a escolha do usuário
    if save_option == '1':
        save_to_temp_sqlite(transformed_data)
    elif save_option == '2':
        save_to_csv(transformed_data, output_dir)
    elif save_option == '3':
        save_to_parquet(transformed_data, output_dir)
    else:
        print("Opção inválida. Nenhum dado foi salvo.")

# Executa o pipeline ETL
if __name__ == "__main__":
    etl_pipeline()

