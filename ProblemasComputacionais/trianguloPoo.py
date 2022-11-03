import os
os.system('cls')
class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA=ladoA
        self.ladoB=ladoB
        self.ladoC=ladoC
    def calcularPerimetro(self):
        perimetro=self.ladoA + self.ladoB + self.ladoC
        return perimetro
    def getMaiorLado(self):
        if (self.ladoA> self.ladoB) and (self.ladoA > self.ladoC):
            return self.ladoA
        elif ( self.ladoB>self.ladoA) and (self.ladoB > self.ladoC):
            return self.ladoB
        elif (self.ladoC>self.ladoB) and (self.ladoC>self.ladoA):
            return self.ladoC

ladoA=int(input("digite o lado a do triangulo"))
ladoB=int(input('digite o lado B do do triangulo'))
ladoC=int(input("digite o lado c do triangulo"))

triangulo1=Triangulo(ladoA,ladoB,ladoC)
perimetro=triangulo1.calcularPerimetro()
maiorLado= triangulo1.getMaiorLado()
print(f'perimetro: {perimetro}')
print(f'menor lado: {maiorLado}')
