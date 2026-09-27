# Exercício 2 - Parte B: QuickSelect

import time
import parte_a_quicksort as qs

K = 1000  # queremos o 1000º menor número


def quickselect(lista, esq, dir, alvo):
    qs.chamadas += 1  # usa o mesmo contador da Parte A

    # Caso base: sobrou um elemento só, e ele é a resposta
    if esq == dir:
        return lista[esq]

    # Mesma partição do QuickSort: o pivô vai para a posição final dele
    pos_pivo = qs.partition(lista, esq, dir)

    # Se o pivô parou na posição procurada, ele é a resposta
    if pos_pivo == alvo:
        return lista[pos_pivo]

    # Chamada recursiva só no lado onde está o alvo;
    # o outro lado é descartado sem ser ordenado
    if alvo < pos_pivo:
        return quickselect(lista, esq, pos_pivo - 1, alvo)
    else:
        return quickselect(lista, pos_pivo + 1, dir, alvo)


def testar_quicksort(numeros):
    lista = numeros.copy()  # não mexe na lista original
    qs.comparacoes = 0
    qs.chamadas = 0

    inicio = time.perf_counter()
    qs.quicksort(lista, 0, len(lista) - 1)
    valor = lista[K - 1]  # acesso direto à posição desejada
    tempo = time.perf_counter() - inicio

    print("QuickSort + acesso à posição desejada")
    print(f"  {K}º menor número: {valor}")
    print(f"  Tempo: {tempo:.4f} segundos")
    print(f"  Comparações: {qs.comparacoes}")
    print(f"  Chamadas recursivas: {qs.chamadas}")
    return valor, tempo


def testar_quickselect(numeros):
    lista = numeros.copy()  # não mexe na lista original
    qs.comparacoes = 0
    qs.chamadas = 0

    # O 1000º menor fica na posição 999 da lista ordenada
    inicio = time.perf_counter()
    valor = quickselect(lista, 0, len(lista) - 1, K - 1)
    tempo = time.perf_counter() - inicio

    print("QuickSelect")
    print(f"  {K}º menor número: {valor}")
    print(f"  Tempo: {tempo:.4f} segundos")
    print(f"  Comparações: {qs.comparacoes}")
    print(f"  Chamadas recursivas: {qs.chamadas}")
    return valor, tempo


def main():
    numeros = qs.ler_numeros(qs.ARQUIVO)

    valor_sort, tempo_sort = testar_quicksort(numeros)
    valor_select, tempo_select = testar_quickselect(numeros)

    iguais = "Sim" if valor_sort == valor_select else "Não"
    print(f"Mesmo resultado nos dois: {iguais}")
    print(f"QuickSelect foi {tempo_sort / tempo_select:.1f} vezes mais rápido")


if __name__ == "__main__":
    main()
