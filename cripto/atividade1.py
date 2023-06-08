def cleaning (text):
    textoLimpo=[]
    for c in text:
        if c.isalpha():
            textoLimpo.append(c.lower())
    textoLimpo="".join(textoLimpo)
    print(textoLimpo)
   
cleaning("123456 Abinoa ddd asasa ****8 !11111122 3 4 ")




