import random

def cleaning (text):
    textoLimpo=[]
    for c in text:
        if c.isalpha():
            textoLimpo.append(c.lower())
    textoLimpo="".join(textoLimpo)
    return  textoLimpo


def cripto(m,k ):
    textoCripto= []
    for letra in m:
        valor= (ord(letra) - ord("a") + k) % 26 + ord("a") 
        textoCripto.append(chr(valor))
    textoCripto="".join(textoCripto)
    textoCripto= textoCripto.upper()
    return textoCripto
    
print(cripto(cleaning("Olá, me chamo fulano da Silva, moro na rua Alfredo Alves.... 888888888 ++++++ +++++ ++++ +++"),random.randrange(1,26)))






