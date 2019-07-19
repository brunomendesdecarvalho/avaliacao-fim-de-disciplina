# coding: utf-8


def main():
    n = int(input('Digite um número: '))
    m = int(input('Digite outro número: '))
    n, m = ordenar_numeros(n, m)
    eh_perfeito(n, m)


def ordenar_numeros(n, m):
    maior = ((n + m) + abs(n - m)) / 2
    if maior == n:
        return m, n
    elif maior == m:
        return n, m


def eh_perfeito(menor, maior):
    numero = 0
    while numero < (maior + 1):
        soma_divisores = 0
        if numero < menor:
            pass
        else:
            divisor = 1
            while divisor < numero:
                if numero % divisor == 0:
                    soma_divisores += divisor
                else:
                    pass
                
                divisor += 1
            
            if soma_divisores == numero:
                print("%d é perfeito" % numero)
            
            else:
                print("%d não é perfeito" % numero)
        
        numero += 1


main()