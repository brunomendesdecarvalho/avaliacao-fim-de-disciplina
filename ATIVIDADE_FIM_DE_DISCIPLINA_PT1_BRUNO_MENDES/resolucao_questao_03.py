from utils import *


def main():
    sequencia = []
    qtd_termos = int(input())
    sequencia_triangular(sequencia, qtd_termos)


def sequencia_triangular(sequencia, qtd_termos):
    # 1 - FOR

    for i in range(1, qtd_termos + 1):
        numero = int((i * (i+1)) / 2)
        sequencia = vetor_inserir_final(sequencia, numero)

    print(sequencia)

    # 2 - WHILE

    # cont = 1
    # while cont <= qtd_termos:
    #     numero = int((cont * (cont + 1)) / 2)
    #     sequencia = vetor_inserir_final(sequencia, numero)
    #     cont += 1
    
    # print(sequencia)

    # 3 - Recursividade

    # if qtd_termos == 0:
    #     print(sequencia)
    #     exit()
    # else:
    #     numero = int((qtd_termos * (qtd_termos + 1)) / 2)
    #     sequencia = vetor_inserir_inicio(sequencia, numero)
    #     sequencia_triangular(sequencia, qtd_termos - 1)


main()