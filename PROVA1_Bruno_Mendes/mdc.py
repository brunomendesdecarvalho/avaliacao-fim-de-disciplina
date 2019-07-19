# coding: utf-8


def main():    
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    calcular_mdc(num1, num2)


def calcular_mdc(num1, num2):    
    quociente = 0
    resto = 1

    while resto != 0:
        quociente = num1 // num2
        resto = num1 % num2
        num1 = num2
        num2 = resto

    print('O MDC é %d' % num1)


main()
