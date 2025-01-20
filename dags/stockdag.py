"""
## Astronaut ETL Stock DAG

This DAG queries the list of stock exchanges from the API and
calculates if is a good time to buy based on the stock price and
other factors.

There are three tasks, the first is one to get the data from the API,
the second calculates based on a funcion, and finaly notify if the price is good.
Both tasks are written in Python using Airflow's TaskFlow API, which allows you
to easily turn Python functions into Airflow tasks, and automatically infer
dependencies and pass data.
"""

from airflow.decorators import dag, task
from airflow.models import Variable
import yfinance as yf
import pendulum


# Define the basic parameters of the DAG
@dag(
    start_date=pendulum.datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "ezschneider", "retries": 3},
    tags=["stock", "etl"],
)
def stock_dag():
    # Define tasks
    @task
    def get_stock() -> list[dict]:
        """
        This task uses the requests library to retrieve a list of Astronauts
        currently in space. The results are pushed to XCom with a specific key
        so they can be used in a downstream pipeline. The task returns a list
        of Astronauts to be used in the next task.
        """
        companies = Variable.get("tickers", deserialize_json=True)

        tickers = yf.Tickers(companies)

        end_date = pendulum.now().strftime("%Y-%m-%d")
        tickers_hist = tickers.history(period="max", end=end_date, interval="1m")

        # Process the DataFrame into a list of dictionaries
        result = tickers_hist.reset_index().to_dict(orient="records")
        print(f"{result[-1]}")

    get_stock()


# Instantiate the DAG
stock_dag()
