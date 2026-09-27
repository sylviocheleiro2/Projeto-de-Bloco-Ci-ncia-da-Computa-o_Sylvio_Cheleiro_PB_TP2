# Exercício 3: Lista Duplamente Encadeada

import time

N = 100000


class No:
    def __init__(self, valor):
        self.anterior = None
        self.valor = valor
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        if self.inicio is None:  # lista vazia
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def inserir_final(self, valor):
        novo = No(valor)
        if self.fim is None:  # lista vazia
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

    def buscar(self, valor):
        # Percorre a lista a partir do início até achar o valor: O(n)
        atual = self.inicio
        while atual is not None:
            if atual.valor == valor:
                return atual
            atual = atual.proximo
        return None

    def remover_no(self, no):
        # Liga o vizinho da esquerda direto no da direita
        if no.anterior is None:  # era o primeiro
            self.inicio = no.proximo
        else:
            no.anterior.proximo = no.proximo

        if no.proximo is None:  # era o último
            self.fim = no.anterior
        else:
            no.proximo.anterior = no.anterior

        no.anterior = None
        no.proximo = None

    def remover(self, valor):
        no = self.buscar(valor)
        if no is None:
            return False
        self.remover_no(no)
        return True

    def listar_inicio_fim(self):
        valores = []
        atual = self.inicio
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(valores)

    def listar_fim_inicio(self):
        valores = []
        atual = self.fim
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.anterior
        return " -> ".join(valores)


def sequencia_obrigatoria():
    lista = ListaDuplamenteEncadeada()
    lista.inserir_final(10)
    lista.inserir_final(20)
    lista.inserir_final(30)
    lista.inserir_final(40)
    lista.inserir_final(50)
    lista.remover(30)

    print("Sequência obrigatória")
    print(lista.listar_inicio_fim())
    print(lista.listar_fim_inicio())


def medir_busca(lista, valor):
    inicio = time.perf_counter()
    lista.buscar(valor)
    fim = time.perf_counter()
    return fim - inicio


def teste_adicional():
    lista = ListaDuplamenteEncadeada()
    for valor in range(1, N + 1):
        lista.inserir_final(valor)

    # Os valores entraram em ordem (1 a N): o valor é a posição na lista
    print(f"Teste adicional ({N} elementos)")
    print(f"Buscar 10 (perto do início): {medir_busca(lista, 10):.4f} s")
    print(f"Buscar 50000 (perto do meio): {medir_busca(lista, 50000):.4f} s")
    print(f"Buscar 99990 (perto do final): {medir_busca(lista, 99990):.4f} s")


def main():
    sequencia_obrigatoria()
    print()
    teste_adicional()


if __name__ == "__main__":
    main()
