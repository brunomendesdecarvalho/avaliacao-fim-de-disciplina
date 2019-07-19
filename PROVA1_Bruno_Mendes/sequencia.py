# coding: utf-8


def main():
    N = int(input('Digite N: '))
    soma_da_sequencia_dada_qtd_termos(N)


def soma_da_sequencia_dada_qtd_termos(N):
    valor_atual = 0
    valor_anterior = 1 # começa com 1, para que o resultado do 'valor_atual' seja 1 também.
    valor_anterior2 = 0
    soma = 0.0
    contador = 0

    while contador < N:
        contador += 1
        valor_atual = valor_anterior + valor_anterior2
        valor_anterior2 = valor_anterior
        valor_anterior = valor_atual

        if contador % 2 != 0:
            soma += valor_atual / (contador ** 2)

        elif contador % 2 == 0:
            soma -= valor_atual / (contador ** 2)


    print('A soma da sequência é: %.3f' % (soma))


main()