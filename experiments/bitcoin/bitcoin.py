import requests

response = requests.get("https://blockchain.info/q/24hrprice") # https://www.blockchain.com/api/q
value_weighted_24hr = response.json() # 24 hour weighted price from the largest exchanges

response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy") # https://developers.coinbase.com/api/v2?shell#get-buy-price
value_current = response.json()['data']['amount'] # includes 1% Coinbase fee






# goal: scrape value from https://www.coinbase.com/price/bitcoin