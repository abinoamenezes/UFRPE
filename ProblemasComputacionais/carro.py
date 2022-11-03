class Carro:
    def __init__(self,consumo) :
        self.consumo=consumo
        self.nivelCombustivel=0
    def andar(self,distancia):
        self.nivelCombustivel-=distancia/self.consumo
    def getobterGasolina(self):
        return self.nivelCombustivel
    def adicionarGasolina(self,litros):
        self.nivelCombustivel+=litros
        
ferrari=Carro(20)
ferrari.adicionarGasolina(100)
ferrari.andar(2000)
print(ferrari.getobterGasolina())