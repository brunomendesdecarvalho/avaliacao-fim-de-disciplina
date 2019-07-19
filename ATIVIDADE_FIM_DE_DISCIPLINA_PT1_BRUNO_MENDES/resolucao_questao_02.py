def main():
    entrada = 1
    while entrada >= 0:
        entrada = int(input())
        nivel_lesma_mais_rapida(entrada)


def nivel_lesma_mais_rapida(entrada):
    velocidade_lesmas = input().split(' ')
    velocidade_lesma_mais_rapida = 0
    for i in range(len(velocidade_lesmas)):
        velocidade_lesmas[i] = int(velocidade_lesmas[i])
        if velocidade_lesmas[i] > velocidade_lesma_mais_rapida:
            velocidade_lesma_mais_rapida = velocidade_lesmas[i]
        else:
            pass
    imprimir_nivel(velocidade_lesma_mais_rapida)


def imprimir_nivel(velocidade_lesma_mais_rapida):
    if velocidade_lesma_mais_rapida < 10:
        print(1)
    elif 10 <= velocidade_lesma_mais_rapida < 20:
        print(2)
    elif 20 <= velocidade_lesma_mais_rapida:
        print(3)


main()