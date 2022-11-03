from math import floor
from math import ceil


def buscabinaria(lista, n, i, f):
    global c

    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return 1
    if i <= f:
        if len(lista) % 2 == 0:
            meio = ceil((i + f) / 2)

        else:
            meio = floor((i + f) / 2)

        if n == lista[meio]:
            c += 1
            return c
        elif n > lista[meio]:
            i = meio + 1
            c += 1

            return buscabinaria(lista, n, i, f)
        elif n < lista[meio]:
            f = meio - 1
            c += 1

            return buscabinaria(lista, n, i, f)
    else:
        return c


lista = input()
lista = lista.split()
lista = list(map(int, lista))
n = lista[0]
del lista[0]
i = 0
f = len(lista) - 1
c = 0
print(f'{buscabinaria(lista, n, i, f)}')
