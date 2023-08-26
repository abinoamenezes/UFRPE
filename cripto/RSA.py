#PARTE 1: Geração de chaves 

#Pesquisa 1: Geração de chaves
# Algoritmo simples para verificar se um número é primo

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Caso de uso
num = 68927
print(is_prime(num))

#Pesquisa 2: Pequeno teorema de Fermat(PTF)
# Implementação em Python:

def pequeno_teorema_fermat(p, a):
    if p <= 1 or not is_prime(p) or a % p == 0:
        return False

    return pow(a, p - 1, p) == 1

# Caso de uso
p = 7 # número primo
a = 3 # número que não é divisível por p
print(pequeno_teorema_fermat(p, a))

#Pesquisa 3: Exponencial Modular
#  Implementação em Python:

def expMod(base, exponente, primo):
    resultado = 1
    # Reduz o exponente para o intervalo [0, primo-2]
    exponente = exponente % (primo - 1)
    while exponente > 0:
        # Se o bit menos significativo do exponente for 1, multiplica o resultado pela base
        if exponente & 1:
            resultado = (resultado * base) % primo
        # Eleva a base ao quadrado e reduz o exponente pela metade
        base = (base * base) % primo
        exponente >>= 1
    return resultado

# Caso de uso
base = 14
exponencial = 5
primo = 3
print(expMod(base, exponencial, primo))


#Parte 2: Algortimo de Encriptação
# Funções necessárias:

# MDC - Recursivo
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Função de Euler
def fi(n1, n2): # Onde n1 e n2 são números primos
  result = (n1 - 1) * (n2 - 1)
  return result

# Gerador de Chave Pública
import random as rd

def generatorPublicKey(p, q):
  num = fi(p, q)
  e = num
  while mdc(e, num) != 1:
    e = rd.randint(2, p * q - 2)
  return int(e)

# Gerador de Chave Privada (MDC, Chave Privada, Y)
def euclidiano_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mdc, x, y = euclidiano_extendido(b % a, a)
        x_new = y - (b // a) * x
        y_new = x
        return mdc, x_new, y_new

# Valores pré-setados, por serem necessários.

p = 29 # VALOR PRIVADO
q = 71 # VALOR PRIVADO
f = fi(p, q) # VALOR PRIVADO
n = p * q # VALOR PRIVADO
e = generatorPublicKey(p, q) # VALOR PÚBLICO
d = euclidiano_extendido(e, f)[1] # VALOR PRIVADO

# Algoritmo de encriptação

def encript(m, e, n):
  c = expMod(m, e, n)
  return c

c = encript(1500, e, n)
print(c)

#Parte 3: Algoritmo de decriptação

def decript(c, d, n):
  m = expMod(c, d, n)
  return m

print(decript(c, d, n))