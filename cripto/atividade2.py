import random
from unidecode import unidecode #essa biblioteca retira os acentos das letras e o cedilha. Precisa ser instalada pelo PIP

#Questão 1 

def cleaning (text):
    textoLimpo=[]
    for c in text:
        if c.isalpha():
            textoLimpo.append(c.lower())
    textoLimpo="".join(textoLimpo)
    textoLimpo=unidecode(textoLimpo)
    return  textoLimpo


def cripto(m,k):
    print(k)
    textoCripto= []
    for letra in m:
        valor= (ord(letra) - ord("a") + k) % 26 + ord("a") 
        textoCripto.append(chr(valor))
    textoCripto="".join(textoCripto)
    textoCripto= textoCripto.upper()
    return textoCripto

#Questão 2

def FrequenciaTextoCifrado(textoCifrado):
    alfabeto= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    frequencia = {}

    for letra in textoCifrado:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

    for letra in alfabeto:
        if letra not in frequencia:
            frequencia[letra]=0

    total_caracteres = len(texto)

    frequencia_percentual = {}

    for letra, ocorrencias in frequencia.items():
        percentual = (ocorrencias / total_caracteres)
        frequencia_percentual[letra] = percentual

    
    return frequencia_percentual

texto = cripto(cleaning("""A criptografia é uma técnica de segurança amplamente utilizada na proteção de informações sensíveis. 
Ela consiste na transformação dos dados originais em um formato ilegível, conhecido como texto cifrado. A cifra de substituição 
é um exemplo simples de criptografia, em que cada caractere do texto original é substituído por outro de acordo com uma regra 
pré-definida. Outro método de criptografia é a cifra de deslocamento, também conhecida como cifra de César. Nessa cifra, cada 
letra do texto original é deslocada um número fixo de posições no alfabeto. Por exemplo, com um deslocamento de 3, a letra A 
se torna D, a letra B se torna E, e assim por diante. A criptografia desempenha um papel crucial na proteção da privacidade e 
na garantia da integridade das informações. Ela é amplamente utilizada em transações financeiras, comunicações online e armazenamento 
de dados sensíveis. Para garantir a segurança dos dados, é importante utilizar algoritmos de criptografia robustos e manter as 
chaves de criptografia em sigilo. Além disso, a evolução da tecnologia exige o desenvolvimento constante de métodos de 
criptografia mais avançados, capazes de resistir a ataques cada vez mais sofisticados."""),random.randrange(1,26))

print(texto)

frequenciaCripto=FrequenciaTextoCifrado(texto)
frequenciaCripto=dict(sorted(frequenciaCripto.items()))

def comparacaoDeFrequencia():
    const={}
  
    global frequenciaCripto
    frequeciaPT=frequeciaPT={"A":0.146, "B": 0.01, "C":0.039, "D":0.05, "E":0.126, "F":0.01, "G":0.013, "H":0.013, "I":0.062, 
                             "J":0.009, "K":0.0, "L":0.028, "M":0.047, "N":0.044, "O":0.097, "P": 0.025, "Q": 0.012, 
                             "R":0.065, "S": 0.068, "T":0.043, "U":0.036, "V":0.016, "W":0.0, "X":0.005, "Y": 0.00, "Z":0.0}

    for freqCrip in frequenciaCripto:
        for freqInd in frequeciaPT:
            for i in range(1,26):
                if freqCrip==freqInd:
                    if i in const:
                        const[i]+=frequenciaCripto[freqCrip] * frequeciaPT[freqInd] 
                    else:
                        j=ord(freqCrip) + i
                        const[i]=frequenciaCripto[chr(j)] * frequeciaPT[freqInd] 

    const_I = 0.073
    chave_mais_prox = None
    menor_diferenca = 100 #Inicializando com um valor alto

    for key, value in const.items():
        diferenca = abs(value - const_I)
        if diferenca < menor_diferenca:
            chave_mais_prox = key
            menor_diferenca = diferenca

    print("Chave com valor mais proximo de 0.073:", chave_mais_prox)
    
comparacaoDeFrequencia()