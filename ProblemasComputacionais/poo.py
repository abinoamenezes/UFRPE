class televisao:
    def __init__(self,min,max):
        self.ligada = False
        self.canal = 1
        self.cmin=min
        self.cmax=max

    def muda_canal_cima(self):
        if self.canal +1<=self.cmax:
            self.canal += 1

    def muda_canal_baixo(self):
        if self.canal-1>=self.cmin:
            self.canal-=1

tv=televisao(1,99)
for x in range(1,120):
    tv.muda_canal_cima()

print(tv.canal)
for x in range(0,120):
    tv.muda_canal_baixo()
print(tv.canal)
