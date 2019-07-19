# coding: utf-8


def main():
    lim_inferior = 10
    lim_superior = 1000
    imprimir_primos_entre(10, 1000)


def imprimir_primos_entre(menor, maior):
    while menor < maior:
        if eh_primo(menor):
            print(menor)
        else:
            pass

        menor += 1


def eh_primo(numero):
    from math import sqrt
    
    raiz_quadrada = int(sqrt(numero))
    divisor = 2
    while divisor < (raiz_quadrada + 1):
        if numero % divisor == 0:
            return False
        else:
            pass

        divisor += 1
    
    return True


main()