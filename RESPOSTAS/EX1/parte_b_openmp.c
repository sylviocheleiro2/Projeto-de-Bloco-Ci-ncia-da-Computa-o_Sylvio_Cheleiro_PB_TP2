// Exercício 1 - Parte B: processamento paralelo com OpenMP

#include <stdio.h>
#include <omp.h>

// Resultados de cada arquivo (são 12 arquivos em /dados/arquivos)
int linhas[12];
int palavras[12];

void processar_arquivo(int i) {
    char caminho[100];
    sprintf(caminho, "/dados/arquivos/arquivo_%02d.txt", i + 1);

    FILE *arquivo = fopen(caminho, "r");

    int total_linhas = 0;
    int total_palavras = 0;
    int dentro_da_palavra = 0;

    // Lê o arquivo um caractere por vez, até o fim (EOF)
    int c = fgetc(arquivo);
    while (c != EOF) {
        if (c == '\n') {
            total_linhas++;
        }

        if (c == ' ' || c == '\n') {
            dentro_da_palavra = 0;
        } else if (dentro_da_palavra == 0) {
            // começou uma palavra nova
            dentro_da_palavra = 1;
            total_palavras++;
        }

        c = fgetc(arquivo);
    }

    fclose(arquivo);

    linhas[i] = total_linhas;
    palavras[i] = total_palavras;
}

int main() {
    double inicio = omp_get_wtime();

    // O OpenMP divide os 12 arquivos entre as threads.
    // Cada thread grava só na posição i do seu arquivo.
    #pragma omp parallel for
    for (int i = 0; i < 12; i++) {
        processar_arquivo(i);
    }

    double fim = omp_get_wtime();

    for (int i = 0; i < 12; i++) {
        printf("arquivo_%02d.txt\n", i + 1);
        printf("Linhas: %d\n", linhas[i]);
        printf("Palavras: %d\n", palavras[i]);
    }

    printf("Threads: %d\n", omp_get_max_threads());
    printf("Tempo total: %.4f segundos\n", fim - inicio);

    return 0;
}
