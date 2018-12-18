class Veiculo:
    
    # Método construtor
    def __init__(self, cor, ano, marca, tanque):
        self.cor = cor
        self.ano = ano
        self.marca = marca
        self.tanque = tanque
    
    def abastecer(self,litros):
        self.tanque += litros
    
    def __str__(self):
        return "O veiculo é " + self.cor +  " da marca " + self.marca + " e o ano é " + str(self.ano)