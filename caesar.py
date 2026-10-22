def deslocar(texto, deslocamento):
    resultado = []
    for letra in texto:
        if letra.isalpha():
            posicao = ord(letra) - 65
            nova_posicao = (posicao - deslocamento) % 26
            resultado.append(chr(nova_posicao + 65))
        else:
            resultado.append(letra)
    return "".join(resultado)


def forca_bruta(texto):
    for d in range(1, 26):
        print(d, deslocar(texto, d))