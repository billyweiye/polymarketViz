import requests

from py_clob_client.constants import POLYGON
from py_clob_client.client import ClobClient

HOST = "https://clob.polymarket.com"
API_KEY = "ENTER_YOUR_KEY"
CHAIN_ID = POLYGON


client = ClobClient(HOST, key=API_KEY, chain_id=CHAIN_ID, signature_type=2)


def get_latest_market_data():
    # Define parameters for the API request
    params = {
        "limit": 1,
        "active": True,
        "archived": False,
        "order": "creationDate",
        "ascending": False
    }

    try:
        # Make the API request to retrieve market data
        response = requests.get("https://gamma-api.polymarket.com/events", params=params)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        # Handle any HTTP errors or request issues
        print(f"An error occurred: {e}")
        return None

    # Return the JSON content of the response
    return response.json()
    
def get_all_trades(client):
    # 调用API获取交易数据
    response = client.get_trades()

    