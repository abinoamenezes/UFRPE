class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.esquerdo=None
        self.direito=None

class ArvoreBinaria:
    def __init__(self) :
        self.raiz=None

    def inserir(self, valor):
        if self.raiz==None:
            self.raiz=Nodo(valor)
        else:
           self.inserirRecursivamente(valor,self.raiz)
    

    def inserirRecursivamente(self,valor,nodo_atual):
        if valor<nodo_atual.valor:
            if nodo_atual.esquerda is None:
                nodo_atual.esquerda= Nodo(valor)
            else:
                self.inserirRecursivamente(valor,nodo_atual.esquerda)
        else:
            if valor>nodo_atual.valor:
                if nodo_atual.direito is None:
                    nodo_atual.direito= Nodo(valor)
                else:
                    self.inserirRecursivamente(valor,nodo_atual.direito)
    def Buscar(self, valor) :
             
        return self.BuscarRecursiva(valor,self.raiz)
        


    def BuscarRecursiva(self, valor, nodo_atual):
        if valor==nodo_atual.valor:
            return nodo_atual.valor
        else: 
            if valor<nodo_atual.valor:
                self.Buscar(valor, nodo_atual.esquerdo)
            else:
                self.Buscar(valor, nodo_atual.direito)


myTree= ArvoreBinaria()
myTree.inserir(10)
valorBuscado= myTree.Buscar(10)
print(valorBuscado)