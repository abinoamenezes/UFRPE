import random
from unidecode import unidecode

def cleaning(text):
    textoLimpo = []
    for c in text:
        if c.isalpha():
            textoLimpo.append(c.lower())
    textoLimpo = "".join(textoLimpo)
    textoLimpo = unidecode(textoLimpo)
    return textoLimpo

def cripto(m, k):
    textoCripto = []
    for letra in m:
        valor = (ord(letra) - ord("a") + k) % 26 + ord("a")
        textoCripto.append(chr(valor))
    textoCripto = "".join(textoCripto)
    textoCripto = textoCripto.upper()
    return textoCripto

def FrequenciaTextoCifrado(textoCifrado):
    frequencia = {}

    for letra in textoCifrado:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

    total_caracteres = len(textoCifrado)

    frequencia_decimal = {}

    for letra, ocorrencias in frequencia.items():
        frequencia_decimal[letra] = ocorrencias / total_caracteres

    return frequencia_decimal

def descobrir_chave_deslocamento(texto_cifrado, frequencias_portugues, constante_idioma):
    frequencia_texto_cifrado = FrequenciaTextoCifrado(texto_cifrado)
    chave_descoberta = None
    menor_erro = float("inf")

    for chave in range(26):
        erro_total = 0

        for letra_cifrada, frequencia_cifrada in frequencia_texto_cifrado.items():
            indice_letra_cifrada = ord(letra_cifrada) - ord("A")
            letra_portugues = chr(indice_letra_cifrada + ord("A"))
            frequencia_esperada = frequencias_portugues[letra_portugues]
            erro_letra = (frequencia_esperada * constante_idioma) - frequencia_cifrada
            erro_total += abs(erro_letra)

        if erro_total < menor_erro:
            menor_erro = erro_total
            chave_descoberta = chave

    return chave_descoberta


# Frequências das letras em português
frequencias_portugues = {
    "A": 14.634, "B": 1.043, "C": 3.882, "D": 4.992, "E": 12.570, "F": 1.023, "G": 1.303,
    "H": 1.281, "I": 6.186, "J": 0.879, "K": 0.015, "L": 2.779, "M": 4.738, "N": 4.446,
    "O": 9.735, "P": 2.523, "Q": 1.204, "R": 6.530, "S": 6.805, "T": 4.336, "U": 3.639,
    "V": 1.575, "W": 0.037, "X": 0.453, "Y": 0.006, "Z": 0.470
}

texto = """A criptografia é uma técnica de segurança amplamente utilizada na proteção de informações sensíveis. 
Ela consiste na transformação dos dados originais em um formato ilegível, conhecido como texto cifrado. A cifra de substituição é 
um exemplo simples de criptografia, em que cada caractere do texto original é substituído por outro de acordo com uma regra pré-definida. 
Outro método de criptografia é a cifra de deslocamento, também conhecida como cifra de César. Nessa cifra, cada letra do texto original é 
deslocada um número fixo de posições no alfabeto. Por exemplo, com um deslocamento de 3, a letra A se torna D, a letra B se torna E, e assim 
por diante. A criptografia desempenha um papel crucial na proteção da privacidade e na garantia da integridade das informações. 
Ela é amplamente utilizada em transações financeiras, comunicações online e armazenamento de dados sensíveis. Para garantir a segurança 
dos dados, é importante utilizar algoritmos de criptografia robustos e manter as chaves de criptografia em sigilo. Além disso, a evolução da 
tecnologia exige o desenvolvimento constante de métodos de criptografia mais avançados, capazes de resistir a ataques cada vez mais sofisticados."""
chave = random.randrange(1,26)
print(chave)
constante_idioma = 0.073
texto_cifrado = cripto(texto, chave)
frequencia_texto_cifrado = FrequenciaTextoCifrado(texto_cifrado)
chave_descoberta = descobrir_chave_deslocamento(texto_cifrado, frequencias_portugues, constante_idioma)

print("Texto cifrado:", texto_cifrado)
print("Chave de deslocamento:", chave_descoberta)