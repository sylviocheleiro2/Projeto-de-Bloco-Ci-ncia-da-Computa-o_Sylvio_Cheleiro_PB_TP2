# Exercício 5 - Parte A: Mochila 0/1 com recursão

import time

ARQUIVO = "/dados/mochila.txt"

chamadas = 0


def ler_mochila(caminho):
    itens = []
    with open(caminho) as arquivo:
        # quantidade de itens e capacidade da mochila
        quantidade, capacidade = arquivo.readline().split()

        # nome, peso, valor
        for i in range(int(quantidade)):
            nome, peso, valor = arquivo.readline().split()
            itens.append((int(peso), int(valor)))
    return itens, int(capacidade)


def mochila(itens, i, capacidade):

    global chamadas
    chamadas += 1

    # Caso base: acabaram os itens ou a mochila está cheia
    if i == len(itens) or capacidade == 0:
        return 0

    peso, valor = itens[i]

    # O item não cabe: deixar de fora
    if peso > capacidade:
        return mochila(itens, i + 1, capacidade)

    # deixar o item de fora ou colocar na mochila.
    sem_item = mochila(itens, i + 1, capacidade)
    com_item = valor + mochila(itens, i + 1, capacidade - peso)

    # Fica com a escolha de maior valor
    return max(sem_item, com_item)


def main():
    itens, capacidade = ler_mochila(ARQUIVO)

    inicio = time.perf_counter()
    valor_maximo = mochila(itens, 0, capacidade)
    fim = time.perf_counter()

    print(f"Valor máximo: {valor_maximo}")
    print(f"Chamadas recursivas: {chamadas}")
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
