#cifra Vigenere- Abinoã Menezes de Paula

def cifrar_vigenere(mensagem, chave):
    mensagem = mensagem.upper()
    chave = chave.upper()
    mensagem_cifrada = ""
    chave_extendida = chave * (len(mensagem) // len(chave)) + chave[:len(mensagem) % len(chave)]

    for i in range(len(mensagem)):
        if mensagem[i].isalpha():
            letra_mensagem = ord(mensagem[i]) - ord('A')
            letra_chave = ord(chave_extendida[i]) - ord('A')
            letra_cifrada = (letra_mensagem + letra_chave) % 26
            letra_cifrada = chr(letra_cifrada + ord('A'))
            mensagem_cifrada += letra_cifrada
        else:
            mensagem_cifrada += mensagem[i]

    return mensagem_cifrada


def decifrar_vigenere(mensagem_cifrada, chave):
    mensagem_cifrada = mensagem_cifrada.upper()
    chave = chave.upper()
    mensagem_decifrada = ""
    chave_extendida = chave * (len(mensagem_cifrada) // len(chave)) + chave[:len(mensagem_cifrada) % len(chave)]

    for i in range(len(mensagem_cifrada)):
        if mensagem_cifrada[i].isalpha():
            letra_cifrada = ord(mensagem_cifrada[i]) - ord('A')
            letra_chave = ord(chave_extendida[i]) - ord('A')
            letra_decifrada = (letra_cifrada - letra_chave) % 26
            letra_decifrada = chr(letra_decifrada + ord('A'))
            mensagem_decifrada += letra_decifrada
        else:
            mensagem_decifrada += mensagem_cifrada[i]

    return mensagem_decifrada


# Exemplo de uso:
mensagem_original = "HELLO"
chave = "SECRET"

mensagem_cifrada = cifrar_vigenere(mensagem_original, chave)
print("Mensagem cifrada:", mensagem_cifrada)

mensagem_decifrada = decifrar_vigenere(mensagem_cifrada, chave)
print("Mensagem decifrada:", mensagem_decifrada)
