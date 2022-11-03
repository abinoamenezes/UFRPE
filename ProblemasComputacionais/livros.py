class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
        

        
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1
    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)
        
    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)
    
    

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)

    def livrosOrdenadosPeloNome (self):
        

#ordenando os livros alugados
        for i in range(1,len(self.alugados)):
            chave=self.alugados[i]
            j=i
            while j>0 and self.alugados[j-1].nome > chave.nome:
                self.alugados[j]=self.alugados[j-1]
                j-=1
            self.alugados[j]=chave
        
#ordernando livros disponiveis
        for i in range(1,len(self.disponiveis)):
            chave=self.disponiveis[i]
            j=i
            while j>0 and self.disponiveis[j-1].nome > chave.nome:
                self.disponiveis[j]=self.disponiveis[j-1]
                j-=1
            self.disponiveis[j]=chave

#mesclnado com o mergerSort
        lista_definitiva=[]
        i,j=0,0
        while i<len(self.alugados) and j<len(self.disponiveis):
            if self.alugados[i].nome<=self.disponiveis[j].nome:
                lista_definitiva.append(self.alugados[i])
                i+=1
           
            else:
                lista_definitiva.append(self.disponiveis[j])
                j+=1
        lista_definitiva+=self.alugados[i:]
        lista_definitiva+=self.disponiveis[j:]
        return lista_definitiva
       
        
        
        
       


lista_entrada=list(map(str,input().split(',')))
c=1

bibli=Biblioteca()
c=1
for d in range(int(lista_entrada[0])):
  li=Livro(int(lista_entrada[c]),lista_entrada[c+1],lista_entrada[c+2])
  bibli.inserir(li)
  c+=3
bibli.alugar(li)
for c in bibli.livrosOrdenadosPeloNome():
    print(c.codigo,end=' ')



 