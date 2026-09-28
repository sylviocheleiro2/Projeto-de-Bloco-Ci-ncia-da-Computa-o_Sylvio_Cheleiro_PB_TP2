# Exercício 5 - Parte B: Mochila 0/1 com programação dinâmica (memorização)

import time

ARQUIVO = "/dados/mochila.txt"

# Guarda o resultado de cada estado (item, capacidade) já calculado
memo = {}


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
    # Caso base: acabaram os itens ou a mochila está cheia
    if i == len(itens) or capacidade == 0:
        return 0

    # Estado já calculado: reaproveita o resultado guardado
    if (i, capacidade) in memo:
        return memo[(i, capacidade)]

    peso, valor = itens[i]

    # O item não cabe: deixar de fora
    if peso > capacidade:
        resultado = mochila(itens, i + 1, capacidade)
    else:
        # deixar o item de fora ou colocar na mochila.
        sem_item = mochila(itens, i + 1, capacidade)
        com_item = valor + mochila(itens, i + 1, capacidade - peso)

        # Fica com a escolha de maior valor
        resultado = max(sem_item, com_item)

    # Guarda o resultado deste estado para não calcular de novo
    memo[(i, capacidade)] = resultado
    return resultado


def main():
    itens, capacidade = ler_mochila(ARQUIVO)

    inicio = time.perf_counter()
    valor_maximo = mochila(itens, 0, capacidade)
    fim = time.perf_counter()

    print(f"Valor máximo: {valor_maximo}")
    print(f"Estados calculados: {len(memo)}")
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
