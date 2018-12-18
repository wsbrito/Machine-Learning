from veiculo import Veiculo

class Carro(Veiculo):
    
    #Construtor
    def __init__(self, cor, ano, marca, tanque):
        # Executando o construtor da classe pai
        Veiculo.__init__(self,cor, ano, marca, tanque)