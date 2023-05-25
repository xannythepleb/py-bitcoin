import requests
import re

def get_bitcoin_price_from_coindesk():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    return round(float(price.replace(',', '')))

def get_bitcoin_price_from_coingecko():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    return price

def get_bitcoin_price_from_bitfinex():
    url = "https://api.bitfinex.com/v1/pubticker/btcusd"
    response = requests.get(url)
    data = response.json()
    price = data["last_price"]
    return round(float(price))

def get_bitcoin_price_from_kraken():
    url = "https://api.kraken.com/0/public/Ticker?pair=BTCUSD"
    response = requests.get(url)
    data = response.json()
    price = data["result"]["XXBTZUSD"]["c"][0]
    return round(float(price))

def get_bitcoin_price_from_binance():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    price = data["price"]
    return round(float(price))

def get_mempool_fees():
    url = "https://mempool.space/api/v1/fees/recommended"
    response = requests.get(url)
    data = response.json()
    return data

print("\nChoose an API to fetch Bitcoin price:")
print("\n1. CoinDesk")
print("2. CoinGecko")
print("3. Bitfinex")
print("4. Kraken")
print("5. Binance")
api_choice = input("\nEnter your choice (1, 2, 3, 4, or 5): ")

if api_choice == "1":
    bitcoin_price = get_bitcoin_price_from_coindesk()
elif api_choice == "2":
    bitcoin_price = get_bitcoin_price_from_coingecko()
elif api_choice == "3":
    bitcoin_price = get_bitcoin_price_from_bitfinex()
elif api_choice == "4":
    bitcoin_price = get_bitcoin_price_from_kraken()
elif api_choice == "5":
    bitcoin_price = get_bitcoin_price_from_binance()
else:
    print("\nInvalid choice")
    exit()

mempool_fees = get_mempool_fees()

print(f"\n  1 BTC = ${bitcoin_price:,}")
print(f"  1 BTC = 1 BTC")
print(f"\n  The recommended tx fees are: ")
for key, value in mempool_fees.items():
    formatted_key = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', key).lower()
    capitalized_key = formatted_key.capitalize()
    print(f"   {capitalized_key}: {value} sats/vB")


print(f"\n    #FreeRoss\n")

