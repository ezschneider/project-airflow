# Stock DAG

Este projeto contém uma DAG do Apache Airflow para obter dados de ações usando a biblioteca `yfinance`.

## Estrutura do Projeto

```
.
├── .astro/
│   ├── config.yaml
│   ├── dag_integrity_exceptions.txt
│   └── test_dag_integrity_default.py
├── dags/
│   └── stockdag.py
├── Dockerfile
├── poetry.lock
├── pyproject.toml
└── ...
```

## Pré-requisitos

- Docker
- Poetry
- Astro CLI

## Configuração do Ambiente

1. **Clone o repositório:**

    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. **Instale o Poetry:**

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Instale as dependências do projeto:**

    ```sh
    poetry install
    ```

## Executando a DAG

1. **Inicie o ambiente do Astro:**

    ```sh
    astro dev start
    ```

2. **Acesse a interface do Airflow:**

    Abra o navegador e vá para [http://localhost:8080](http://localhost:8080). Use as credenciais padrão (admin / admin) para fazer login.

3. **Ative a DAG:**

    Na interface do Airflow, ative a DAG `stock_dag`.

## Configuração de Variáveis

Certifique-se de configurar a variável `tickers` no Airflow com uma lista de tickers de ações. Você pode fazer isso na interface do Airflow em **Admin -> Variables**.

## Estrutura da DAG

A DAG `stock_dag` é definida no arquivo `stockdag.py`. Ela contém as seguintes tarefas:

- `get_stock`: Obtém dados de ações usando a biblioteca `yfinance`.

## Docker

O projeto inclui um Dockerfile para configurar o ambiente de execução. O Dockerfile usa a imagem base `quay.io/astronomer/astro-runtime:12.6.0` e instala as dependências do Poetry.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
