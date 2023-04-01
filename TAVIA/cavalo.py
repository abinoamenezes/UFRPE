

import random

# define o tamanho do tabuleiro
N = 8

# define a classe de um indivíduo
class Individuo:
    def __init__(self, cromossomo=None):
        if cromossomo is None:
            # gera um cromossomo sequencial
            self.cromossomo = list(range(N*N))
            #embaralhar cromossomo

            random.shuffle(self.cromossomo)
        else:
            self.cromossomo = cromossomo

    def fitness(self):
        # calcula a quantidade de movimentos necessários para visitar todas as casas
        tabuleiro = [[0] * N for _ in range(N)]
        movimentos = 0
        x, y = self.cromossomo[0] // N, self.cromossomo[0] % N
        tabuleiro[x][y] = 1
        for i in range(1, N * N):
            x1, y1 = self.cromossomo[i] // N, self.cromossomo[i] % N
            dx, dy = abs(x1 - x), abs(y1 - y)
            if dx == 1 and dy == 2 or dx == 2 and dy == 1:
                if tabuleiro[x1][y1] == 0:
                    movimentos += 1
                    x, y = x1, y1
                    tabuleiro[x][y] = i + 1
        return  movimentos + 1

    def cruzamento(self, outro):
        # realiza o cruzamento com outro indivíduo
        ponto = random.randrange(1, N * N - 1)
        return (
            Individuo(self.cromossomo[:ponto] + [gene for gene in outro.cromossomo if gene not in self.cromossomo[:ponto]]),
            Individuo(outro.cromossomo[:ponto] + [gene for gene in self.cromossomo if gene not in outro.cromossomo[:ponto]]),
        )

    def mutacao(self):
        # realiza uma mutação no cromossomo
        i, j = random.sample(range(N * N), 2)
        self.cromossomo[i], self.cromossomo[j] = self.cromossomo[j], self.cromossomo[i]

# define a função principal do algoritmo genético
def algoritmo_genetico(populacao_inicial, fitness_limite, geracoes_limite):
    # inicializa a população
    populacao = populacao_inicial

    # realiza a evolução da população
    for geracao in range(geracoes_limite):
        # calcula o fitness de cada indivíduo
        fitness = [individuo.fitness() for individuo in populacao]

        # verifica se atingimos o fitness limite
        if max(fitness) == fitness_limite:
            return max(populacao, key=lambda x: x.fitness())

        # seleciona os pais para cruzamento
        pais = [populacao[i] for i in random.sample(range(len(populacao)), len(populacao))]

        # realiza o cruzamento
        filhos = []
        for i in range(0, len(pais), 2):
            pai1 = pais[i]
            pai2 = pais[i + 1]
            filho1, filho2 = pai1.cruzamento(pai2)
            filhos.append(filho1)
            filhos.append(filho2)
        
                # realiza a mutação
        for individuo in filhos:
            if random.random() < 0.1:
                individuo.mutacao()

        # seleciona os sobreviventes
        populacao = pais + filhos
        fitness = [individuo.fitness() for individuo in populacao]
        #ordenar a população em ordem decrescente da aptidão
        #se quiser fazer elitismo, selecionar de 0 a len(pais) da populacao ordenada (ex: populacao[0:len(pais)] )
        popOrdenada = sorted(populacao, key=lambda x: x.fitness(), reverse=True)
        populacao = popOrdenada[0:len(pais)] #elitismo
        #populacao = [populacao[i] for i in sorted(range(len(fitness)), key=lambda x: fitness[x][0], reverse=True)[:len(pais)]]

    # retorna o melhor indivíduo encontrado
    return max(populacao, key=lambda x: x.fitness())



# cria a população inicial
populacao_inicial = [Individuo() for _ in range(10)]

# define os parâmetros do algoritmo genético
fitness_limite = 64
geracoes_limite = 200000

# roda o algoritmo genético
melhor_individuo = algoritmo_genetico(populacao_inicial, fitness_limite, geracoes_limite)

# imprime o resultado
print("Melhor indivíduo encontrado:")
print(melhor_individuo.cromossomo)
print("Fitness:", melhor_individuo.fitness())






