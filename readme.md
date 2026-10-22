# Decifragem de Textos com Cifras Clássicas

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de decifrar dois textos fornecidos em formato binário: `encoded-simple.txt` e `encoded-circular.txt`.

A atividade consistiu em investigar os métodos de codificação utilizados, testar diferentes estratégias de decifragem e implementar soluções em Python para recuperar as mensagens originais.

## Metodologia

A resolução foi realizada de forma experimental, por meio de tentativas com diferentes métodos de decifragem.

### 1. Decifragem do texto `encoded-simple.txt`

Inicialmente, foi testada a cifra de César, baseada no deslocamento das letras do alfabeto. Essa abordagem não produziu o resultado esperado.

Em seguida, foi utilizada a cifra de substituição simples, na qual cada letra do texto original é substituída por outra letra de acordo com uma chave. Para encontrar uma chave adequada, foi implementada uma busca heurística baseada no algoritmo *hill climbing*, com avaliação dos textos candidatos por meio de frequências de quadgramas da língua inglesa.

Essa abordagem permitiu encontrar uma solução para o primeiro texto.

### 2. Decifragem do texto `encoded-circular.txt`

O segundo texto exigiu uma abordagem diferente. Após tentativas iniciais que não produziram o resultado esperado, foi investigada uma cifra rotativa, na qual o deslocamento aplicado às letras varia conforme suas posições no texto.

A solução foi desenvolvida combinando a busca por uma chave de substituição com a avaliação de diferentes sentidos de rotação. A segunda implementação dessa estratégia apresentou o resultado esperado.

## Tecnologias e técnicas utilizadas

- **Python:** implementação dos algoritmos de decifragem.
- **Cifra de César:** primeira estratégia testada para o texto simples.
- **Cifra de substituição simples:** método utilizado para recuperar o primeiro texto.
- **Cifra rotativa:** método utilizado para recuperar o segundo texto.
- **Hill climbing:** busca heurística por chaves candidatas.
- **Análise de quadgramas:** avaliação estatística de textos candidatos com base em sequências de quatro letras.
- **Visualização de dados:** gráficos utilizados para analisar os experimentos.

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `main.py` | Executa a estratégia de decifragem selecionada. |
| `caesar.py` | Implementa o deslocamento utilizado na cifra de César e uma tentativa por força bruta. |
| `substitution.py` | Implementa a aplicação de chaves de substituição e a busca heurística por hill climbing. |
| `rotativa.py` | Implementa operações de rotação e estratégias para decifrar o texto circular. |
| `quadgram.py` | Contém a implementação da pontuação baseada em quadgramas. |
| `utils.py` | Contém funções auxiliares para converter os dados binários em texto e normalizar as mensagens. |
| `experimentos.py` | Reúne experimentos relacionados à investigação das cifras. |
| `english_quadgrams.txt` | Arquivo de dados utilizado na avaliação estatística dos textos candidatos. |
| `encoded-simple.txt` | Primeiro texto fornecido para decifragem. |
| `encoded-circular.txt` | Segundo texto fornecido para decifragem. |
| `resultados.json` | Arquivo com resultados dos experimentos. |
| `fig_convergencia.png` | Gráfico relacionado à convergência dos experimentos. |
| `fig_ic.png` | Gráfico relacionado ao índice de coincidência. |
| `fig_reinicios.png` | Gráfico relacionado aos reinícios da busca heurística. |

## Execução

Com o Python 3 instalado, clone o repositório e acesse o diretório do projeto:

```bash
git clone https://github.com/AlmeidaNunesGabriel/decodificando
cd decodificando
```

Recomenda-se utilizar um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências externas necessárias ao projeto, caso existam, e execute:

```bash
python3 main.py
```

O programa utiliza os arquivos de entrada e de pontuação presentes no diretório do projeto. Portanto, execute o comando a partir da raiz do repositório.


### Fonte dos dados de quadgramas

O arquivo `english_quadgrams.txt` contém estatísticas de quadgramas da língua inglesa utilizadas para avaliar a qualidade das tentativas de decifragem. Essas estatísticas são empregadas pelo algoritmo de busca para comparar possíveis textos decifrados e favorecer aqueles que apresentam padrões mais compatíveis com o inglês.

**Fonte:** [Practical Cryptography — Quadgrams](http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams//quadgrams/)

O material foi utilizado como referência para implementar a avaliação estatística dos textos durante o processo de criptoanálise.

