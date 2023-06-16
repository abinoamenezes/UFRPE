import random

def cripto(m,k ):
    textoCripto= []
    for letra in m:
        valor= (ord(letra) - ord("a") + k) % 26 + ord("a") 
        textoCripto.append(chr(valor))
    textoCripto="".join(textoCripto)
    return textoCripto
    
print(cripto("",random.randrange(1,26)))






