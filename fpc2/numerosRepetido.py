nr=[]

def descobrindoNumerosRepetidos(listaNumeros):
    n=1
    for i in listaNumeros:
        for c in range(n,len(listaNumeros)):
            if i==listaNumeros[c]:
                nr.append(listaNumeros[c])
        n=n+1
    return nr

print(descobrindoNumerosRepetidos([14,15,4,9,15,9,4,14]))
