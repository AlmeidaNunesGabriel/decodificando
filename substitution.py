import random
import string

ALFABETO = string.ascii_uppercase


def aplicar_chave(texto, chave):
    # chave[i] é a letra cifrada que corresponde à letra ALFABETO[i] do texto claro
    # caminho inverso: cifrado -> claro
    tabela = {chave[i]: ALFABETO[i] for i in range(26)}
    return "".join(tabela.get(c, c) for c in texto)


def hill_climbing(cifrado, pontuador, reinicios=20, iteracoes=5000):
    melhor_chave = None
    melhor_pontos = float("-inf")

    for r in range(reinicios):
        # Chave aleatória inicial
        letras = list(ALFABETO)
        random.shuffle(letras)
        chave = letras
        pontos = pontuador.pontuar(aplicar_chave(cifrado, chave))

        for _ in range(iteracoes):
            # Troca duas posições da chave
            i, j = random.sample(range(26), 2)
            chave[i], chave[j] = chave[j], chave[i]
            novos_pontos = pontuador.pontuar(aplicar_chave(cifrado, chave))

            if novos_pontos > pontos:
                pontos = novos_pontos  # melhorou: mantém
            else:
                chave[i], chave[j] = chave[j], chave[i]  # piorou: desfaz

        print(f"Reinício {r + 1}: pontuação {pontos:.2f}")

        if pontos > melhor_pontos:
            melhor_pontos = pontos
            melhor_chave = chave[:]

    return "".join(melhor_chave), melhor_pontos