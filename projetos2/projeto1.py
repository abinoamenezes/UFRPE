from itertools import permutations
import time
begin=time.time()

rota = []
mapa = {}
lis = []
pontos_permutacao = []
#arquivo = str(input('Digite o nome do aquivo: '))
file = open('matriz1', 'r')  # abrindo arquivo
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
        if c[j] != '0':
            mapa[c[j]] = (lis.index(c), j)
            if c[j] != 'R':
                pontos_permutacao.append(c[j])
# permutações
combinacao = list(permutations(pontos_permutacao))

# calculando a menor distância
def distancia(lss):
    menor = 0

    for tupla in lss:
        g = len(tupla)
        c = 0
        total = abs(mapa['R'][0] - mapa[tupla[c]][0]) + abs(mapa['R'][1] - mapa[tupla[c]][1])
        while c < g - 1:
            total = total + abs(mapa[tupla[c]][0] - mapa[tupla[c + 1]][0]) + abs(
                mapa[tupla[c]][1] - mapa[tupla[c + 1]][1])
            c = c + 1
        total = total + abs(mapa['R'][0] - mapa[tupla[c]][0]) + abs(mapa['R'][1] - mapa[tupla[c]][1])
        if total < menor or menor == 0:
            menor = total
            rota = tupla
    print(f'Menor distância: {menor} dronômetros')
    rota = ' '.join(rota)  # transformando tupla em string
    print(f'Rota com a menor distância: {rota}')

# chamando função

distancia(combinacao)
print(time.time()-begin)