import requests
import json

40e54a6c4dc68cfcacd8575aed619e63

dolar_request = requests.get('http://economia.awesomeapi.com.br/USD-BRL/1')
#dolar_request = requests.get('http://api.promasters.net.br/cotacao/v1/valores')

#print(dolar_request.text)

dolar_dict = json.loads(dolar_request.text)

print('dolar_dict = \n',dolar_dict)