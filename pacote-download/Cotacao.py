import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL'] ['bid']
cotacao_euro = cotacoes['EURBRL'] ['bid']
cotacao_bitcoin = cotacoes['BTCBRL'] ['bid']
print (f'A cotação do dólar no momento é R${cotacao_dolar}')
print (f'A cotação do euro no momento é R${cotacao_euro}')
print (f'A cotação do bitcoin no momento é R${cotacao_bitcoin}')
