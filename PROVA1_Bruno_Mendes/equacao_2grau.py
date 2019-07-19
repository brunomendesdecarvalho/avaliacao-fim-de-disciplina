# coding: utf-8


def main():

    a, b, c = adquirir_elementos_funcao_quadratica()
    avaliar_funcao_quadratica(a, b, c)

def adquirir_elementos_funcao_quadratica():
    a, b, c = map(int, input('Digite os elementos da equação do 2º grau: ').split(' '))
    
    return a
    return b
    return c


def avaliar_funcao_quadratica(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print('A função não possui raízes reais.')

    elif delta == 0:
        raiz = (-b) / (2 * a)

        print('A função possui uma raíz que vale %.2f.' % raiz)

    elif delta > 0:
        delta = (delta ** (1/2))
        raiz1 = (-b + delta) / (2 * a)
        raiz2 = (-b - delta) / (2 * a)

        print('A função possui duas raizes, que valem %.2f e %.2f.' % (raiz1, raiz2))


main()
