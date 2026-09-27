# Exercício 1 - Parte A: processamento assíncrono com asyncio

import asyncio
import os
import time

PASTA = "/dados/arquivos"


def ler_arquivo(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        return arquivo.read()


def contar_linhas_e_palavras(texto):
    linhas = 0
    palavras = 0
    for linha in texto.splitlines():
        linhas += 1
        palavras += len(linha.split())
    return linhas, palavras


async def processar_arquivo(nome):
    caminho = os.path.join(PASTA, nome)

    # Ler o disco bloqueia: a leitura roda numa thread auxiliar e,
    # durante o await, o loop de eventos atende as outras tarefas.
    texto = await asyncio.to_thread(ler_arquivo, caminho)

    # Contar é trabalho de CPU: roda no loop, uma tarefa por vez.
    linhas, palavras = contar_linhas_e_palavras(texto)
    return nome, linhas, palavras


async def main():
    inicio = time.perf_counter()

    # Uma tarefa assíncrona por arquivo, executadas com gather().
    # Os resultados voltam na mesma ordem das tarefas.
    tarefas = [processar_arquivo(nome) for nome in os.listdir(PASTA)]
    resultados = await asyncio.gather(*tarefas)

    fim = time.perf_counter()

    for nome, linhas, palavras in resultados:
        print(nome)
        print(f"Linhas: {linhas}")
        print(f"Palavras: {palavras}")

    print(f"Tempo total: {fim - inicio:.2f} segundos")


if __name__ == "__main__":
    asyncio.run(main())
