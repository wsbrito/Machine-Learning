from veiculo import Veiculo
from carro import Carro

carro = Veiculo('Preto',1975,'Ford',50)

#print(type(carro))

print(carro.tanque)
carro.abastecer(20)
print(carro.tanque)
print(carro)

carro2 = Carro('Branco',2018,'Toyota',60)
print(carro2)
