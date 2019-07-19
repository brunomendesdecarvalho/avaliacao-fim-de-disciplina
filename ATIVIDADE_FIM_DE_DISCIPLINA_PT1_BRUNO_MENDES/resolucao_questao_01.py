def main():
    n = int(input())
    experimento(n)


def experimento(quantidade_testes):
    total_ratos = 0
    total_sapos = 0
    total_coelhos = 0
    for i in range(quantidade_testes):
        qtd_cobaias, tipo_cobaias = input().split(' ')
        qtd_cobaias = int(qtd_cobaias)
        if tipo_cobaias == 'C':
            total_coelhos += qtd_cobaias
        elif tipo_cobaias == 'R':
            total_ratos += qtd_cobaias
        elif tipo_cobaias == 'S':
            total_sapos += qtd_cobaias

    estatisticas_cobaias(total_coelhos, total_ratos, total_sapos)


def estatisticas_cobaias(total_coelhos, total_ratos, total_sapos):
    total_cobaias = total_coelhos + total_ratos + total_sapos
    percentual_coelhos = (total_coelhos / total_cobaias) * 100
    percentual_ratos = (total_ratos / total_cobaias) * 100
    percentual_sapos = (total_sapos / total_cobaias) * 100
    imprimir_resultados(total_cobaias, total_coelhos, total_ratos, total_sapos, percentual_coelhos, percentual_ratos, percentual_sapos)


def imprimir_resultados(total_cobaias, total_coelhos, total_ratos, total_sapos, percentual_coelhos, percentual_ratos, percentual_sapos):
    porcentagem = chr(37)
    print('Total: %d cobaias\n' \
          'Total de coelhos: %d\n' \
          'Total de ratos: %d\n' \
          'Total de sapos: %d\n' \
          'Percentual de coelhos: %.2f %s\n' \
          'Percentual de ratos: %.2f %s\n' \
          'Percentual de sapos: %.2f %s\n' \
          % (total_cobaias, total_coelhos, total_ratos, total_sapos,
          percentual_coelhos, porcentagem, percentual_ratos, porcentagem,
          percentual_sapos, porcentagem))


main()