from utils import *


def main():
    qtd_pilotos = int(input('Quantos pilotos competiram: '))
    dados_pilotos(qtd_pilotos)


def dados_pilotos(qtd_pilotos):
    nome_pilotos = vetor_novo_vetor(qtd_pilotos)
    tempo_pilotos = vetor_novo_vetor(qtd_pilotos)
    for i in range(qtd_pilotos):
        nome_pilotos[i] = input('Nome do piloto %d: ' % (i + 1))
        tempo_pilotos[i] = int(input('Tempo do piloto %d, em minutos: ' % (i + 1)))
    
    tempo_medio = tempo_medio_da_corrida(tempo_pilotos)
    qtd_pilotos_abaixo_do_tempo_medio(tempo_pilotos, tempo_medio)
    velocidade_pilotos = velocidade_media_por_piloto(qtd_pilotos, tempo_pilotos)
    print('A velocidade média da corrida foi de %.2f km/h.' % (vetor_reduce_por_media(velocidade_pilotos)))
    campeao_corrida(nome_pilotos, tempo_pilotos, velocidade_pilotos)


def tempo_medio_da_corrida(tempo_pilotos):
    tempo_medio = vetor_reduce_por_media(tempo_pilotos)
    print('\nO tempo médio de conclusão da corrida foi {} minutos'.format(tempo_medio))

    return tempo_medio


def qtd_pilotos_abaixo_do_tempo_medio(tempo_pilotos, tempo_medio):
    qtd_pilotos_abaixo_do_tempo_medio = len(vetor_filtrar_entre(tempo_pilotos, 0, tempo_medio))
    print('{} pilotos conseguiram concluir a corrida abaixo do tempo médio'.format(qtd_pilotos_abaixo_do_tempo_medio))


def velocidade_media_por_piloto(qtd_pilotos, tempo_pilotos):
    distancia = 360
    velocidade_pilotos = vetor_novo_vetor(qtd_pilotos)
    for i in range(len(tempo_pilotos)):
        velocidade_pilotos[i] = distancia / (tempo_pilotos[i] / 60)
    
    return velocidade_pilotos


def campeao_corrida(nome_pilotos, tempo_pilotos, velocidade_pilotos):
    menor_tempo = tempo_pilotos[0]
    posicao = 0
    for i in range(len(tempo_pilotos)):
        if menor_tempo > tempo_pilotos[i]:
            menor_tempo = tempo_pilotos[i]
            posicao = i
        else:
            pass

    nome_campeao = nome_pilotos[posicao]
    velocidade_campeao = velocidade_pilotos[posicao]
    print('\n********* RESULTADO FINAL *********\n' \
          'Campeão: %s\n' \
          'Tempo de conclusão, em minutos: %d\n' \
          'Velocidade média: %.2f km/h' % (nome_campeao, menor_tempo, velocidade_campeao))


main()