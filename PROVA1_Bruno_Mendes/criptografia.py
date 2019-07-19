# coding: utf-8


def main():
    frase = input("Digite uma frase para ser criptografada: ")
    frase_criptografada = vogal_em_ascii(frase) # letra A
    frase_criptografada = mudar_letra_alfabeto(frase_criptografada) # letra B
    frase_criptografada = numerais_por_extenso(frase_criptografada) # letra C
    deslocar_p_posicoes_nome_n() # letra D
    print(frase_criptografada) # letra E
    print()
    contagem_final(frase_criptografada) # letra F


def vogal_em_ascii(frase):
    frase_nova = ''
    cont = 0
    codigo = 0
    while cont < len(frase):
        if ord(frase[cont]) == 65 or ord(frase[cont]) == 69 or ord(frase[cont]) == 73 or ord(frase[cont]) == 79 or ord(frase[cont]) == 85 or ord(frase[cont]) == 97 or ord(frase[cont]) == 101 or ord(frase[cont]) == 105 or ord(frase[cont]) == 111 or ord(frase[cont]) == 117:
            codigo = ord(frase[cont])
            frase_nova += tratar_codigo(codigo)
        else:
            frase_nova += frase[cont]
        
        cont += 1

    return frase_nova


def tratar_codigo(codigo):
    while codigo > 10:
        centenas = codigo // 100
        dezenas = codigo // 10
        unidades = codigo % 10
        codigo = centenas + dezenas + unidades
    
    return str(codigo)
    

def mudar_letra_alfabeto(frase):
    cont = 0
    frase_nova = ''
    while cont < len(frase):
        if ord(frase[cont]) == 90:
            frase_nova += 'A'
        elif ord(frase[cont]) == 122:
            frase_nova += 'a'
        elif ord(frase[cont]) < 65 or 91 <= ord(frase[cont]) < 97 or 122 < ord(frase[cont]):
            frase_nova += frase[cont]
        else:
            frase_nova += chr(ord(frase[cont]) + 1)
        cont += 1

    return frase_nova


def numerais_por_extenso(frase):
    frase_nova = ''
    cont = 0
    while cont < len(frase):
        if ord(frase[cont]) == 48:
            frase_nova += '[zero]'
        elif ord(frase[cont]) == 49:
            frase_nova += '[um]'
        elif ord(frase[cont]) == 50:
            frase_nova += '[dois]'
        elif ord(frase[cont]) == 51:
            frase_nova += '[tres]'
        elif ord(frase[cont]) == 52:
            frase_nova += '[quatro]'
        elif ord(frase[cont]) == 53:
            frase_nova += '[cinco]'
        elif ord(frase[cont]) == 54:
            frase_nova += '[seis]'
        elif ord(frase[cont]) == 55:
            frase_nova += '[sete]'
        elif ord(frase[cont]) == 56:
            frase_nova += '[oito]'
        elif ord(frase[cont]) == 57:
            frase_nova += '[nove]'
        else:
            frase_nova += frase[cont]
        
        cont += 1
    
    return frase_nova


def deslocar_p_posicoes_nome_n():
    N = input("Digite um nome: ")
    P = int(input("Digite quantas posições na tabela ASC II deseja deslocar as letras do nome (valor entre -10 e 10): "))
    cont = 0
    novo_N = ''

    while cont < len(N):
        novo_N += chr(ord(N[cont]) + P)
        cont += 1
    
    print(novo_N)
    print()


def contagem_final(frase):
    qtd_letras = 0
    qtd_numeros = 0
    qtd_caracteres_especiais = 0
    qtd_resto = 0
    cont = 0

    while cont < len(frase):
        if 65 <= ord(frase[cont]) <= 90 or 97 <= ord(frase[cont]) <= 122:
            qtd_letras += 1
        elif 48 <= ord(frase[cont]) <= 57:
            qtd_numeros += 1
        elif 32 <= ord(frase[cont]) <= 47 or 58 <= ord(frase[cont]) <= 64 or 91 <= ord(frase[cont]) <= 96 or 123 <= ord(frase[cont]) <= 126:
            qtd_caracteres_especiais += 1
        else:
            qtd_resto += 1

        cont += 1
    
    print('********** CONTAGEM FINAL **********\n' \
          'Letras: %d\n' \
          'Números: %d\n' \
          'Caracteres especiais: %d\n' \
          'Resto: %d\n' \
          'TOTAL DE CARACTERES: %d' % (qtd_letras, qtd_numeros, qtd_caracteres_especiais, qtd_resto, len(frase)))


main()