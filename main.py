import logging
from gate_api import ApiClient, Configuration, Order, SpotApi
import gate_api
import time
import datetime
s = []
logger = logging.getLogger(__name__)
configuration = gate_api.Configuration(host = "https://api.gateio.ws/api/v4",
    key = '',
    secret = '')
configuration1 = gate_api.Configuration(host = "https://api.gateio.ws/api/v4",
    key = '',
    secret = '')
while 1:
    for i in (configuration1, configuration):
        api_client = gate_api.ApiClient(i)
        spot_api = SpotApi(ApiClient(i))
        currencies = ['GT', 'TLOS', 'DOGE', 'HAO', 'WIT', 'APT', 'LTC', 'HT', 'BEAM', 'LN', 'STRAX', 'MINA', 'MXC', 'VRA',
                      'BTG', 'NEO', 'SSV', 'BEAM',
                      'HNS', 'SDN', 'OAX', 'DAG', 'SOLO', 'POWR']
        with open("new.txt", "w") as file:
            file.write(
                f"{s}, {datetime.datetime.now()}")
        for i in currencies:
            list_btc = spot_api.list_order_book(i + '_BTC')
            list_usdt = spot_api.list_order_book(i + '_USDT')
            list_usdt_btc = spot_api.list_order_book('BTC_USDT')
            d = ((10 / float(list_usdt_btc.asks[0][0])) / float(list_btc.asks[0][0])) * float(list_usdt.bids[0][0])
            d1 = ((10 / float(list_usdt.asks[0][0])) * float(list_btc.bids[0][0])) * float(list_usdt_btc.bids[0][0])
            if d > 10 or d1 > 10:
                s.append(d)
            else:
                pass
            time.sleep(1)
