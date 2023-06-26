import os
import time
begin=time.time()
os.system('cls')

rota = []
mapa = {}
lis = []
pontos_permutacao = []
#arquivo = str(input('Digite o nome do aquivo: '))
file = open('pontos_entrega.txt', 'r')  # abrindo arquivo
linhas = file.readlines()

# criando matriz
for l in linhas:
    con = l.split()  # split divide o conteudo da variável
    lis.append(con)
del lis[0]

# descobrindo posições

for c in lis:
    x = len(c)
    for j in range(x):
        if c[j] != '0': mapa[c[j]] = (lis.index(c), j)

#criando uma lista com os pontos
lista_pontos=mapa.keys()
lista_pontos=list((lista_pontos))
lista_pontos.remove('R')
 
sequencia=['R']

# calculando o vizinho mais próximo distância
def vizinho(lista):
    tamanho=len(lista)  
    inicial='R'
    distancia=0
    
    
    for c in range(tamanho):
        menor=0
        
        

        for ponto in lista:
               # print (ponto)

                calculo= abs(mapa[inicial][0] -mapa[ponto][0]) + abs(mapa[inicial][1] - mapa[ponto][1])
                #print(calculo)
                if menor > calculo or menor==0:
                    menor=calculo
                    key=ponto
        sequencia.append(key)
 
        distancia+=menor
       
        inicial=key
        lista.remove(key)
        
    sequencia.append('R')
    calculo= abs(mapa['R'][0] -mapa[ponto][0]) + abs(mapa['R'][1] - mapa[ponto][1])
    distancia+=calculo
   
    rota_final=' '.join(sequencia)
    
    print(rota_final)
    print(f'distancia: {distancia}')
      
vizinho(lista_pontos)
print(time.time()-begin)

    
    
            

