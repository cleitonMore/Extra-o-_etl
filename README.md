Projeto de ETL - Extração de Dados de Criptomoedas
Este projeto é um pipeline ETL (Extract, Transform, Load) que extrai dados de criptomoedas da API CoinGecko, transforma esses dados em um formato estruturado e carrega-os em diferentes destinos (banco de dados temporário, CSV ou Parquet).

Funcionalidades
Extração de Dados: Coleta dados de 10 criptomoedas (ordenadas pela capitalização de mercado) em tempo real usando a API pública CoinGecko.
Transformação de Dados: Os dados extraídos são transformados em um formato legível e filtrado para incluir apenas as informações mais relevantes.
Carga de Dados: O usuário pode escolher entre três opções para armazenar os dados transformados:
Banco de dados temporário em memória (SQLite).
Arquivo CSV.
Arquivo Parquet.
Tecnologias Utilizadas
Python 3.9+
Pandas: Manipulação de dados.
Requests: Para fazer chamadas à API.
SQLite3: Banco de dados temporário.
Parquet: Formato de armazenamento otimizado para grandes volumes de dados.
Como Executar o Projeto
1. Clonar o Repositório
bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Configurar o Ambiente
Certifique-se de ter o Python 3.9 ou superior instalado. Em seguida, crie um ambiente virtual e instale as dependências.

bash
Copiar código
# Criação de ambiente virtual
python -m venv venv

# Ativação do ambiente virtual (Windows)
venv\Scripts\activate

# Ativação do ambiente virtual (Linux/MacOS)
source venv/bin/activate

# Instalação das dependências
pip install -r requirements.txt
3. Executar o Pipeline ETL
Com o ambiente configurado, basta rodar o script principal para iniciar o pipeline ETL:

bash
Copiar código
python seu_script_etl.py
O pipeline solicitará como você deseja salvar os dados:

Banco de Dados Temporário (SQLite): Carrega os dados em um banco de dados temporário na memória e exibe os dados diretamente no terminal.
CSV: Salva os dados em um arquivo cryptocurrencies.csv na área de trabalho.
Parquet: Salva os dados em um arquivo cryptocurrencies.parquet na área de trabalho.
4. Escolha de Armazenamento
Após rodar o script, você será solicitado a escolher entre as três opções de armazenamento:

bash
Copiar código
Como você gostaria de salvar os dados?
1. Banco de Dados Temporário (memória)
2. CSV
3. Parquet
Escolha uma opção (1/2/3):
Os arquivos gerados (CSV ou Parquet) serão salvos na pasta "Dados salvos do projeto do Cleiton", que será criada automaticamente na sua área de trabalho.

Estrutura do Projeto
plaintext
Copiar código
├── README.md                 # Documentação do projeto
├── requirements.txt           # Dependências do projeto
├── seu_script_etl.py          # Script principal de execução do pipeline ETL
└── .gitignore                 # Arquivos a serem ignorados no Git
