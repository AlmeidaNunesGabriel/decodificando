from utils import binario_para_texto, normalizar
from quadgram import Pontuador
#rom collections import Counter
#from substitution import aplicar_chave
#from rotativa import quebrar_rotativa, desfazer_rotacao
#from substitution import hill_climbing, aplicar_chave
from rotativa import quebrar_rotativa2, aplicar_rotativa

#decodificar o texto do arquivo encoded-simple.txt
#texto = binario_para_texto("encoded-simple.txt")
#cifrado = normalizar(texto)

#pontuador = Pontuador("english_quadgrams.txt")

#chave, pontos = hill_climbing(cifrado, pontuador)

#print()
#print("Chave:", chave)
#print("Pontuação:", pontos)
#print()
# Aplica a chave no texto original (com espaços) para facilitar a leitura
#print(aplicar_chave(texto.upper(), chave))

#decodificar o texto do arquivo encoded-circular.txt

#print(binario_para_texto("encoded-circular.txt"))

#def ic(s):
    #n = len(s)
    #if n < 2:
        #return 0
    #c = Counter(s)
    #return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


#texto = normalizar(binario_para_texto("encoded-circular.txt"))
#print("Letras:", len(texto))

#for p in range(1, 31):
    #colunas = [texto[i::p] for i in range(p)]
    #media = sum(ic(c) for c in colunas) / p
    #print(p, round(media, 4))

#tentativa 1
#texto = binario_para_texto("encoded-circular.txt")
#cifrado = normalizar(texto)

#pontuador = Pontuador("english_quadgrams.txt")

#pontos, chave, sinal = quebrar_rotativa(cifrado, pontuador)

#print()
#print("Sinal escolhido:", sinal)
#print("Chave:", chave)
#print("Pontuação:", pontos)
#print()
#print(aplicar_chave(desfazer_rotacao(cifrado, sinal), chave))

#tentativa 2 (funcionou)

texto = binario_para_texto("encoded-circular.txt")
cifrado = normalizar(texto)

pontuador = Pontuador("english_quadgrams.txt")

pontos, chave, sinal = quebrar_rotativa2(cifrado, pontuador)

print()
print("Sinal escolhido:", sinal)
print("Chave:", chave)
print("Pontuação:", pontos)
print()
print(aplicar_rotativa(cifrado, chave, sinal))