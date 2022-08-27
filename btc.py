import requests
from datetime import datetime
req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
response = req.json()
sell_price = response['btc_usd']['sell']
print('Цена продажи на', datetime.now().strftime(
    '%Y-%m-%d'), 'составляет', sell_price, '$')
