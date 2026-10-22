def binario_para_texto(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        conteudo = f.read()

    grupos = conteudo.split()

    caracteres = []
    for grupo in grupos:
        numero = int(grupo, 2)
        caracteres.append(chr(numero))

    return "".join(caracteres)

def normalizar(texto):
    # Mantém só letras e deixa em maiúsculo (tira espaços e pontuação)
    return "".join(c for c in texto.upper() if c.isalpha())