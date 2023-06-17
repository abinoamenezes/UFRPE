from unidecode import unidecode #essa biblioteca retira os acentos das letras e o cedilha. Precisa ser instalada pelo PIP

def cleaning (text):
    textoLimpo=[]
    for c in text:
        if c.isalpha():
            textoLimpo.append(c.lower())
    textoLimpo="".join(textoLimpo)
    textoLimpo=unidecode(textoLimpo)
    return "texto limpo: " + textoLimpo
   
print(cleaning(input("Digite aqui o texto que será limpado: ")))



