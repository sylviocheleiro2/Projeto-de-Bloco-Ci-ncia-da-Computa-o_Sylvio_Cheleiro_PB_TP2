# Exercício 4: Labirinto (recursão com backtracking)

import sys

sys.setrecursionlimit(5000)

ARQUIVO = "/dados/labirinto.txt"

def ler_labirinto(caminho):
    labirinto = []
    with open(caminho) as arquivo:
        for linha in arquivo:
            linha = linha.rstrip("\n")
            # Cada linha vira uma lista de caracteres, para podermos marcar o caminho
            labirinto.append(list(linha))
    return labirinto


def criar_visitados(labirinto):
    # Tabela do mesmo tamanho do labirinto, começando tudo como False
    visitado = []
    for linha in range(len(labirinto)):
        visitado.append([False] * len(labirinto[linha]))
    return visitado


def encontrar_inicio(labirinto):
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            if labirinto[linha][coluna] == "S":
                return linha, coluna


def procurar_caminho(labirinto, visitado, linha, coluna):
    # Caso base: saiu dos limites do labirinto
    if linha < 0 or linha >= len(labirinto):
        return False
    if coluna < 0 or coluna >= len(labirinto[linha]):
        return False

    # Caso base: parede, não dá para passar
    if labirinto[linha][coluna] == "#":
        return False

    # Caso base: já passamos por aqui, não entra de novo
    if visitado[linha][coluna]:
        return False

    # Caso base: saída
    if labirinto[linha][coluna] == "E":
        return True

    # Marca a posição como visitada e como parte do caminho
    visitado[linha][coluna] = True
    if labirinto[linha][coluna] != "S":
        labirinto[linha][coluna] = "*"

    # Chamadas recursivas: tenta cima, baixo, esquerda e direita.
    if procurar_caminho(labirinto, visitado, linha - 1, coluna):  # cima
        return True
    if procurar_caminho(labirinto, visitado, linha + 1, coluna):  # baixo
        return True
    if procurar_caminho(labirinto, visitado, linha, coluna - 1):  # esquerda
        return True
    if procurar_caminho(labirinto, visitado, linha, coluna + 1):  # direita
        return True

    #(backtracking): nenhuma direção chegou na saída. Tira o *
    # desta posição e volta para a decisão anterior, continua marcada
    # como visitada, para não ser explorada de novo.
    if labirinto[linha][coluna] != "S":
        labirinto[linha][coluna] = " "
    return False


def mostrar_labirinto(labirinto):
    for linha in labirinto:
        print("".join(linha))


def main():
    labirinto = ler_labirinto(ARQUIVO)
    visitado = criar_visitados(labirinto)
    linha_inicio, coluna_inicio = encontrar_inicio(labirinto)

    achou = procurar_caminho(labirinto, visitado, linha_inicio, coluna_inicio)

    if achou:
        print("Caminho encontrado (marcado com *):")
        mostrar_labirinto(labirinto)
    else:
        print("Não existe caminho entre S e E.")


if __name__ == "__main__":
    main()
