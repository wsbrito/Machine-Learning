import requests
import json

dolar_request = requests.get('http://economia.awesomeapi.com.br/USD-BRL/1')
#dolar_request = requests.get('http://api.promasters.net.br/cotacao/v1/valores')

#print(dolar_request.text)

dolar_dict = json.loads(dolar_request.text)

print('dolar_dict = \n',dolar_dict)