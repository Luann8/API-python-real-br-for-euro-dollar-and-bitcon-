import requests
import json

response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
data = response.json()

usd_bid = data['USDBRL']['bid']
eur_bid = data['EURBRL']['bid']
btc_bid = data['BTCBRL']['bid']

print(f'O preço de venda do Dólar Americano é: {usd_bid} ')
print(f'O preço de venda do Euro é: {eur_bid} ')
print(f'O preço de venda do Bitcoin é: {btc_bid} ')
