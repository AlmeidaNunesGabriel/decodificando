import math


class Pontuador:
    def __init__(self, nome_arquivo):
        self.contagens = {}
        total = 0

        # Lê o arquivo: cada linha é "QUAD 12345"
        with open(nome_arquivo, "r") as f:
            for linha in f:
                partes = linha.split()
                if len(partes) != 2:
                    continue  # ignora linhas vazias ou estranhas
                quadgram = partes[0].upper()
                contagem = int(partes[1])
                self.contagens[quadgram] = contagem
                total += contagem

        self.total = total

        # Converte contagens em log10 da probabilidade
        self.logprobs = {}
        for quadgram, contagem in self.contagens.items():
            self.logprobs[quadgram] = math.log10(contagem / total)

        # Valor usado para quadgrams que não existem na tabela
        self.piso = math.log10(0.01 / total)

    def pontuar(self, texto):
        pontos = 0
        for i in range(len(texto) - 3):
            janela = texto[i:i + 4]
            pontos += self.logprobs.get(janela, self.piso)
        return pontos