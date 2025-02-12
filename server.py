from py_clob_client.constants import POLYGON
from py_clob_client.client import ClobClient

HOST = "https://clob.polymarket.com"
API_KEY = "ENTER_YOUR_KEY"
CHAIN_ID = POLYGON


client = ClobClient(HOST, key=API_KEY, chain_id=CHAIN_ID, signature_type=2)



def get_all_markets(client):
    all_markets = []
    next_cursor = ''

    all_markets, next_cursor = [], ''
    while True:
        # 调用API获取市场数据
        # This line calls the API to retrieve market data
        response = client.get_markets(next_cursor=next_cursor)

        # 将当前页的市场数据添加到所有市场列表中
        all_markets.extend(response['data'])


        # 检查是否有下一页
        next_cursor = response.get('next_cursor')
        print(next_cursor)
        if not next_cursor:
            break

    return all_markets
    
