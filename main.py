#AlphaVantage API key: ZAPAOIYTE4U33ASM

import requests
import json
import pandas as pd
from datetime import datetime, timedelta

api_key = "ZAPAOIYTE4U33ASM"
base_url = "https://www.alphavantage.co/query"

end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=1825)).strftime('%Y-%m-%d')

base_currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNH']

dfs = []

for base_currency in base_currencies:
    params = {'function': 'FX_DAILY',
              'from_symbol': base_currency,
              'to_symbol': 'ALL',
              'outputsize': 'compact',
              'datatype': 'csv',
              'apikey': api_key,
              'start_date': start_date,
              'end_date': end_date}
    response = requests.get(base_url, params=params)
    df = pd.read_csv(response.text)
