import json
import random
import string
import time
from collections import Counter

import matplotlib # type: ignore
matplotlib.use("Agg")  # gera arquivos PNG sem abrir janela
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]

from utils import binario_para_texto, normalizar
from quadgram import Pontuador
from substitution import aplicar_chave
from rotativa import aplicar_rotativa

ALFABETO = string.ascii_uppercase


def hill_climbing_registrado(cifrado, pontuador, aplicar, reinicios=20, iteracoes=5000):
    """Mesmo algoritmo de antes, mas guardando os dados para os gráficos."""
    finais = []   # pontuação final de cada reinício
    curva = []    # pontuação a cada iteração do primeiro reinício
    melhor_chave = None
    melhor_pontos = float("-inf")

    for r in range(reinicios):
        chave = list(ALFABETO)
        random.shuffle(chave)
        pontos = pontuador.pontuar(aplicar(cifrado, chave))
        historico = [pontos]

        for _ in range(iteracoes):
            i, j = random.sample(range(26), 2)
            chave[i], chave[j] = chave[j], chave[i]
            novos = pontuador.pontuar(aplicar(cifrado, chave))
            if novos > pontos:
                pontos = novos
            else:
                chave[i], chave[j] = chave[j], chave[i]
            historico.append(pontos)

        finais.append(pontos)
        if r == 0:
            curva = historico
        if pontos > melhor_pontos:
            melhor_pontos = pontos
            melhor_chave = chave[:]
        print(f"  reinício {r + 1}/{reinicios}: {pontos:.2f}")

    return finais, curva, "".join(melhor_chave), melhor_pontos


def indice_coincidencia(s):
    n = len(s)
    if n < 2:
        return 0
    c = Counter(s)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


# ---------- Dados ----------
pontuador = Pontuador("english_quadgrams.txt")

cifrado_simples = normalizar(binario_para_texto("encoded-simple.txt"))
cifrado_rot = normalizar(binario_para_texto("encoded-circular.txt"))
print("Letras (simples):", len(cifrado_simples))
print("Letras (rotativa):", len(cifrado_rot))

# ---------- 1. IC por período (cifra rotativa) ----------
periodos = list(range(1, 31))
ic_medio = []
for p in periodos:
    colunas = [cifrado_rot[i::p] for i in range(p)]
    ic_medio.append(sum(indice_coincidencia(c) for c in colunas) / p)

# ---------- 2. Substituição simples ----------
print("\nSubstituição simples:")
t0 = time.time()
fin_s, curva_s, chave_s, pts_s = hill_climbing_registrado(
    cifrado_simples, pontuador, aplicar_chave
)
tempo_s = time.time() - t0

# ---------- 3. Substituição rotativa (sinal -1) ----------
print("\nSubstituição rotativa (sinal -1):")
t0 = time.time()
fin_r, curva_r, chave_r, pts_r = hill_climbing_registrado(
    cifrado_rot, pontuador, lambda c, k: aplicar_rotativa(c, k, -1)
)
tempo_r = time.time() - t0

# ---------- Salva os números ----------
resultados = {
    "simples": {
        "letras": len(cifrado_simples),
        "chave": chave_s,
        "melhor_pontuacao": pts_s,
        "pontuacao_por_quadgram": pts_s / (len(cifrado_simples) - 3),
        "reinicios": fin_s,
        "tempo_s": tempo_s,
    },
    "rotativa": {
        "letras": len(cifrado_rot),
        "chave": chave_r,
        "sinal": -1,
        "melhor_pontuacao": pts_r,
        "pontuacao_por_quadgram": pts_r / (len(cifrado_rot) - 3),
        "reinicios": fin_r,
        "tempo_s": tempo_r,
    },
    "ic_por_periodo": dict(zip(periodos, ic_medio)),
}
with open("resultados.json", "w") as f:
    json.dump(resultados, f, indent=2)

# ---------- Figura 1: IC x período ----------
plt.figure(figsize=(6, 3))
cores = ["tab:red" if p in (13, 26) else "tab:gray" for p in periodos]
plt.bar(periodos, ic_medio, color=cores)
plt.axhline(0.066, linestyle="--", color="k", linewidth=0.8, label="Inglês (≈0,066)")
plt.axhline(0.038, linestyle=":", color="k", linewidth=0.8, label="Aleatório (≈0,038)")
plt.xlabel("Período testado")
plt.ylabel("IC médio das colunas")
plt.legend(fontsize=7)
plt.tight_layout()
plt.savefig("fig_ic.png", dpi=300)
plt.close()

# ---------- Figura 2: pontuação final por reinício ----------
fig, eixos = plt.subplots(1, 2, figsize=(7, 3))
for eixo, dados, titulo in (
    (eixos[0], fin_s, "Substituição simples"),
    (eixos[1], fin_r, "Substituição rotativa"),
):
    eixo.bar(range(1, len(dados) + 1), dados)
    eixo.set_title(titulo, fontsize=9)
    eixo.set_xlabel("Reinício")
    eixo.set_ylabel("Log-pontuação final")
    eixo.set_ylim(min(dados) * 1.02, max(dados) * 0.9)
plt.tight_layout()
plt.savefig("fig_reinicios.png", dpi=300)
plt.close()

# ---------- Figura 3: convergência (reinício 1) ----------
fig, eixos = plt.subplots(1, 2, figsize=(7, 3))
for eixo, curva, titulo in (
    (eixos[0], curva_s, "Substituição simples"),
    (eixos[1], curva_r, "Substituição rotativa"),
):
    eixo.plot(curva)
    eixo.set_title(titulo, fontsize=9)
    eixo.set_xlabel("Iteração")
    eixo.set_ylabel("Log-pontuação")
plt.tight_layout()
plt.savefig("fig_convergencia.png", dpi=300)
plt.close()

# ---------- Resumo no terminal ----------
print("\n=== RESUMO ===")
print(f"Simples:  {pts_s:.2f} | {pts_s / (len(cifrado_simples) - 3):.3f} por quadgram | {tempo_s:.0f} s")
print(f"Rotativa: {pts_r:.2f} | {pts_r / (len(cifrado_rot) - 3):.3f} por quadgram | {tempo_r:.0f} s")
print("Chave simples: ", chave_s)
print("Chave rotativa:", chave_r)
print("\nArquivos gerados: resultados.json, fig_ic.png, fig_reinicios.png, fig_convergencia.png")