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
        # companies = Variable.get("tickers")
        companies = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBAS3.SA"]
        tickers = yf.Tickers(companies)

        end_date = pendulum.now().strftime("%Y-%m-%d")
        tickers_hist = tickers.history(period="max", end=end_date, interval="1m")

        # Process the DataFrame into a list of dictionaries
        result = tickers_hist.reset_index().to_dict(orient="records")

        return result

    @task
    def print_stock_price(stock_prices: dict) -> None:
        """
        This task creates a print statement with the name of an
        Astronaut in space and the craft they are flying on from
        the API request results of the previous task, along with a
        greeting which is hard-coded in this example.
        """

        # print(f"{stock_prices["name"]}{stock_prices["price"]}")
        print(f"{stock_prices}")

    # Use dynamic task mapping to run the print_stock_price task for each
    # Stock in response from the get_stock task
    print_stock_price.expand(
        stock_prices=get_stock()  # Define dependencies using TaskFlow API syntax
    )


# Instantiate the DAG
stock_dag()
