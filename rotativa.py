from substitution import hill_climbing, aplicar_chave
import random
import string
A = 65


def desfazer_rotacao(texto, sinal):
    # texto: só letras maiúsculas, sem espaços
    # sinal: +1 ou -1
    saida = []
    for i, c in enumerate(texto):
        n = (ord(c) - A + sinal * i) % 26
        saida.append(chr(n + A))
    return "".join(saida)


def quebrar_rotativa(cifrado, pontuador, reinicios=20, iteracoes=5000):
    melhor = None
    for sinal in (+1, -1):
        intermediario = desfazer_rotacao(cifrado, sinal)
        chave, pontos = hill_climbing(intermediario, pontuador, reinicios, iteracoes)
        print(f"Sinal {sinal:+d}: melhor pontuação {pontos:.2f}")
        if melhor is None or pontos > melhor[0]:
            melhor = (pontos, chave, sinal)
    return melhor

ALFABETO = string.ascii_uppercase


def aplicar_rotativa(cifrado, chave, sinal):
    # posição de cada letra cifrada dentro da chave
    tabela = {chave[k]: k for k in range(26)}
    saida = []
    for i, c in enumerate(cifrado):
        n = (tabela[c] + sinal * i) % 26
        saida.append(chr(n + 65))
    return "".join(saida)


def hill_climbing_rotativa(cifrado, pontuador, sinal, reinicios=20, iteracoes=5000):
    melhor_chave = None
    melhor_pontos = float("-inf")

    for r in range(reinicios):
        chave = list(ALFABETO)
        random.shuffle(chave)
        pontos = pontuador.pontuar(aplicar_rotativa(cifrado, chave, sinal))

        for _ in range(iteracoes):
            i, j = random.sample(range(26), 2)
            chave[i], chave[j] = chave[j], chave[i]
            novos = pontuador.pontuar(aplicar_rotativa(cifrado, chave, sinal))
            if novos > pontos:
                pontos = novos
            else:
                chave[i], chave[j] = chave[j], chave[i]

        print(f"Sinal {sinal:+d} | reinício {r + 1}: {pontos:.2f}")
        if pontos > melhor_pontos:
            melhor_pontos = pontos
            melhor_chave = chave[:]

    return "".join(melhor_chave), melhor_pontos


def quebrar_rotativa2(cifrado, pontuador):
    melhor = None
    for sinal in (+1, -1):
        chave, pontos = hill_climbing_rotativa(cifrado, pontuador, sinal)
        if melhor is None or pontos > melhor[0]:
            melhor = (pontos, chave, sinal)
    return melhor