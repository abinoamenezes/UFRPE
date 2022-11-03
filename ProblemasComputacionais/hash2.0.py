#extraindo dados
lista_entrada=list(map(int,input().split()))
qtd_conteiner=lista_entrada[0]
tamanho_conteiner=lista_entrada[1]
qtd_insercoes=lista_entrada[2]
tabela_hash=[None]*(qtd_conteiner*tamanho_conteiner)

#inserindo valores na tabela
def inserir(tabela, elemento,qtdConteiner,tamConteiner):
    conteiner=elemento % qtdConteiner
    posi_conteiner=conteiner*tamConteiner
    for c in range(tamConteiner):
        if tabela[posi_conteiner+ c]==None:
            tabela[posi_conteiner + c]=elemento
            break  
#buscando valores na tabela
def busca(tabela,elemento,qtdConteiner,tamConteiner):
    conteiner=elemento % qtdConteiner
    posi_conteiner=conteiner*tamConteiner
    contagem=0
    for c in range(tamConteiner):
        contagem+=1
        if tabela[posi_conteiner + c]==elemento:
            break
        elif tabela[posi_conteiner + c]==None:
            break
    return contagem
    
    
for c in range(3,qtd_insercoes + 3):
    inserir(tabela_hash,lista_entrada[c],qtd_conteiner,tamanho_conteiner)

for c in range((qtd_insercoes + 3), len(lista_entrada)):
    x=busca(tabela_hash,lista_entrada[c],qtd_conteiner,tamanho_conteiner)
    print(x,end=' ')



   


       
            
        


    

