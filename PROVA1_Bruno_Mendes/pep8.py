# coding: utf-8

def main():
    frase = input('Digite uma frase, no formato PEP8: ')
    camel_case(frase)


def camel_case(frase):
    frase_nova = ''
    cont = 0
    while cont < len(frase):
        if ord(frase[cont]) == 95:
            pass
        elif ord(frase[cont-1]) == 95:
            frase_nova += chr(ord(frase[cont]) - 32)
        else:
            frase_nova += frase[cont]

        cont += 1
    print("A frase no formato Camel Case é " + frase_nova)


main()