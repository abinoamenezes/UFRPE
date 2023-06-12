def cleaning (text):
    textoLimpo=[]
    for c in text:
        if c.isalpha():
            textoLimpo.append(c.lower())
    textoLimpo="".join(textoLimpo)
    print("texto limpo: " + textoLimpo)
   
cleaning(input("Digite aqui o texto que será limpado: "))



