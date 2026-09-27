# Exercício 2 - Parte A: QuickSort

import time

ARQUIVO = "/dados/numeros.txt"

comparacoes = 0
chamadas = 0


def ler_numeros(caminho):
    numeros = []
    with open(caminho) as arquivo:
        for linha in arquivo:
            numeros.append(int(linha))
    return numeros


def partition(lista, esq, dir):
    global comparacoes

    # O pivô é o último elemento. Os menores ou iguais a ele
    # vão para a esquerda, e i marca o fim dessa região.
    pivo = lista[dir]
    i = esq - 1
    for j in range(esq, dir):
        comparacoes += 1
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    # Coloca o pivô na posição final dele, entre as duas partes
    lista[i + 1], lista[dir] = lista[dir], lista[i + 1]
    return i + 1


def quicksort(lista, esq, dir):
    global chamadas
    chamadas += 1

    # Caso base: trecho com 0 ou 1 elemento já está ordenado
    if esq >= dir:
        return

    pos_pivo = partition(lista, esq, dir)

    # Chamadas recursivas: ordena os menores e os maiores que o pivô
    quicksort(lista, esq, pos_pivo - 1)
    quicksort(lista, pos_pivo + 1, dir)


def esta_ordenada(lista):
    for i in range(1, len(lista)):
        if lista[i - 1] > lista[i]:
            return False
    return True


def main():
    numeros = ler_numeros(ARQUIVO)

    inicio = time.perf_counter()
    quicksort(numeros, 0, len(numeros) - 1)
    fim = time.perf_counter()

    ordenada = "Sim" if esta_ordenada(numeros) else "Não"

    print(f"Quantidade de números: {len(numeros)}")
    print(f"Lista ordenada: {ordenada}")
    print(f"Primeiros 10: {numeros[:10]}")
    print(f"Últimos 10: {numeros[-10:]}")
    print(f"Comparações: {comparacoes}")
    print(f"Chamadas recursivas: {chamadas}")
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")


if __name__ == "__main__":
    main()
