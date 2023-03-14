import random

def gerar_individuo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

def gerar_populacao(tamanho_populacao, tamanho_individuo):
    return [gerar_individuo(tamanho_individuo) for _ in range(tamanho_populacao)]

def fitness(individuo):
    return sum(individuo)

def selecao_roleta(populacao, numero_pais):
    total_fitness = sum([fitness(individuo) for individuo in populacao])
    pais = []
    for i in range(numero_pais):
        pai = None
        while pai is None or pai in pais:
            valor_sorteado = random.uniform(0, total_fitness)
            soma = 0
            for individuo in populacao:
                soma += fitness(individuo)
                if soma >= valor_sorteado:
                    pai = individuo
                    break
        pais.append(pai)
    return pais

def cruzamento(pais):
    ponto_corte = random.randint(1, len(pais[0])-1)
    filho1 = pais[0][:ponto_corte] + pais[1][ponto_corte:]
    filho2 = pais[1][:ponto_corte] + pais[0][ponto_corte:]
    return filho1, filho2

def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.uniform(0, 1) < taxa_mutacao:
            individuo[i] = 1 - individuo[i]
    return individuo

def algoritmo_genetico(tamanho_populacao, tamanho_individuo, taxa_mutacao, numero_geracoes):
    populacao = gerar_populacao(tamanho_populacao, tamanho_individuo)
    for geracao in range(numero_geracoes):
        pais = selecao_roleta(populacao, 2)
        filhos = cruzamento(pais)
        filhos_mutados = [mutacao(filho, taxa_mutacao) for filho in filhos]
        pior_individuo = min(populacao, key=fitness)
        populacao.remove(pior_individuo)
        populacao.extend(filhos_mutados)
    melhor_individuo = max(populacao, key=fitness)
    return melhor_individuo

# Exemplo de uso:
tamanho_populacao = 100
tamanho_individuo = 20
taxa_mutacao = 0.1
numero_geracoes = 100
resultado = algoritmo_genetico(tamanho_populacao, tamanho_individuo, taxa_mutacao, numero_geracoes)
print(resultado)
