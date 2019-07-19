def obter_texto(mensagem):
    texto = input(mensagem)
    
    return texto


def obter_inteiro(mensagem):
    while True:
        num_inteiro = ''
        digitado = input(mensagem)
        for i in digitado:
            if i in '-0123456789':
                num_inteiro += i
            else:
                pass

        if num_inteiro != digitado:
            print('Valor inválido!')
        else:
            return int(num_inteiro)


def obter_inteiro_no_minimo(mensagem, minimo):
    while True:
        num_inteiro = ''
        digitado = input(mensagem)
        for i in digitado:
            if i in '-0123456789':
                num_inteiro += i
            else:
                pass

        if num_inteiro != digitado or int(num_inteiro) < minimo or (int(num_inteiro) == minimo and minimo == 0):
            print('Valor inválido!')
        else:
            return int(num_inteiro)


def obter_inteiro_no_maximo(mensagem, maximo):
    while True:
        num_inteiro = ''
        digitado = input(mensagem)
        for i in digitado:
            if i in '-0123456789':
                num_inteiro += i
            else:
                pass

        if num_inteiro != digitado or int(num_inteiro) > maximo or (int(num_inteiro) == maximo and maximo == 0):
            print('Valor inválido!')
        else:
            return int(num_inteiro)


def obter_inteiro_entre(mensagem, minimo, maximo):
    while True:
        num_inteiro = ''
        digitado = input(mensagem)
        for i in digitado:
            if i in '-0123456789':
                num_inteiro += i
            else:
                pass

        if num_inteiro != digitado or minimo > int(num_inteiro) or int(num_inteiro) > maximo:
            print('Valor inválido!')
        else:
            return int(num_inteiro)


def obter_inteiro_positivo(mensagem):
    num_inteiro = obter_inteiro_no_minimo(mensagem, 0)
    return num_inteiro


def obter_inteiro_negativo(mensagem):
    num_inteiro = obter_inteiro_no_maximo(mensagem, 0)
    return num_inteiro


def eh_par(valor):
    if valor % 2 == 0:
        return True
    else:
        return False


def eh_impar(valor):
    if valor % 2 != 0:
        return True
    else:
        return False


def eh_positivo(valor):
    if abs(valor) == valor:
        return True
    else:
        return False


def eh_negativo(valor):
    if abs(valor) != valor:
        return True
    else:
        return False


def eh_multiplo(valor, de):
    if valor % de == 0:
        return True
    else:
        return False


def vetor_novo_vetor(tamanho):
    return [0] * tamanho


def vetor_inserir_final(vetor, valor):
    return vetor_inserir_posicao(vetor, valor, len(vetor))


def vetor_inserir_inicio(vetor, valor):
    return vetor_inserir_posicao(vetor, valor, 0)


def vetor_inserir_posicao(vetor, valor, posicao):
    novo_vetor = [0] * (len(vetor) + 1)
    for i in range(len(vetor) + 1):
        if i < posicao:
            novo_vetor[i] = vetor[i]
        elif i == posicao:
            novo_vetor[i] = valor
        elif i > posicao:
            novo_vetor[i] = vetor[i-1]
    
    return novo_vetor


def vetor_contem_valor(vetor, valor):
    for i in vetor:
        if i == valor:
            return True
        else:
            continue
    
    return False


def vetor_contar_valor(vetor, valor):
    ocorrencias = 0
    for i in vetor:
        if i == valor:
            ocorrencias += 1
        else:
            pass
    
    return ocorrencias


def vetor_remover_valor(vetor, valor):
    ocorrencias = vetor_contar_valor(vetor, valor)
    qtd_termos_novo_vetor = len(vetor) - ocorrencias
    novo_vetor = [0] * qtd_termos_novo_vetor
    cont = 0
    while cont < (len(novo_vetor) - 1):
        for i in vetor:
            if i == valor:
                pass
            else:
                novo_vetor[cont] = i
                cont += 1
    
    return novo_vetor


def vetor_inserir_posicao(vetor, valor, posicao):
    novo_vetor = [0] * (len(vetor) + 1)
    for i in range(len(vetor) + 1):
        if i < posicao:
            novo_vetor[i] = vetor[i]
        elif i == posicao:
            novo_vetor[i] = valor
        elif i > posicao:
            novo_vetor[i] = vetor[i-1]
    
    return novo_vetor


def vetor_remover_posicao(vetor, posicao):
    novo_vetor = [0] * (len(vetor) - 1)
    for i in range(len(vetor)):
        if i < posicao:
            novo_vetor[i] = vetor[i]
        elif i == posicao:
            continue
        elif i > posicao:
            novo_vetor[i-1] = vetor[i]
    
    return novo_vetor


def vetor_reduce_por_somatorio(vetor):
    soma = 0
    for i in vetor:
        soma += i
    
    return soma


def vetor_reduce_por_media(vetor):
    if len(vetor) == 0:
        return 0
    else:
        return (vetor_reduce_por_somatorio(vetor) / len(vetor))


def vetor_filtrar_impares(vetor):
    impares = 0
    for i in vetor:
        if eh_impar(i) == True:
            impares += 1
        else:
            pass
    
    cont = 0
    novo_vetor = vetor_novo_vetor(impares)
    
    while cont < impares:
        for i in vetor:
            if eh_impar(i) == True:
                novo_vetor[cont] = i
                cont += 1
            else:
                pass
    
    return novo_vetor


def vetor_filtrar_pares(vetor):
    pares = 0
    for i in vetor:
        if eh_par(i) == True:
            pares += 1
        else:
            pass
    
    cont = 0
    novo_vetor = vetor_novo_vetor(pares)
    
    while cont < pares:
        for i in vetor:
            if eh_par(i) == True:
                novo_vetor[cont] = i
                cont += 1
            else:
                pass
    
    return novo_vetor


def vetor_filtrar_positivos(vetor):
    positivos = 0
    for i in vetor:
        if eh_positivo(i) == True:
            positivos += 1
        else:
            pass
    
    cont = 0
    novo_vetor = vetor_novo_vetor(positivos)
    
    while cont < positivos:
        for i in vetor:
            if eh_positivo(i) == True:
                novo_vetor[cont] = i
                cont += 1
            else:
                pass
    
    return novo_vetor


def vetor_filtrar_negativos(vetor):
    negativos = 0
    for i in vetor:
        if eh_negativo(i) == True:
            negativos += 1
        else:
            pass
    
    cont = 0
    novo_vetor = vetor_novo_vetor(negativos)
    
    while cont < negativos:
        for i in vetor:
            if eh_negativo(i) == True:
                novo_vetor[cont] = i
                cont += 1
            else:
                pass
    
    return novo_vetor


def vetor_filtrar_entre(vetor, min, max):
    entre_numeros = 0
    for i in vetor:
        if min < i < max:
            entre_numeros += 1
        else:
            pass
    
    cont = 0
    novo_vetor = vetor_novo_vetor(entre_numeros)
    
    while cont < entre_numeros:
        for i in vetor:
            if min < i < max:
                novo_vetor[cont] = i
                cont += 1
            else:
                pass
    
    return novo_vetor


def criar_matriz(linhas, colunas):
    nova_matriz = vetor_novo_vetor(linhas)
    for linha in range(len(nova_matriz)):
        nova_matriz[linha] = vetor_novo_vetor(colunas)
    
    return nova_matriz


def matriz_inserir_linha_registro_final(matriz, linha_registro):
    nova_matriz = vetor_novo_vetor(len(matriz) + 1)
    for i in range(len(matriz)):
        nova_matriz[i] = matriz[i]
    nova_matriz[len(matriz)] = linha_registro

    return nova_matriz


def matriz_remover_linhas_registro(matriz, posicao_linhas_registro):
    return vetor_remover_posicao(matriz, posicao_linhas_registro)


def matriz_reduce_por_somatorio(matriz, atributo):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == atributo:
                soma += matriz[i][j]
            else:
                pass
    
    return soma


def matriz_reduce_por_media(matriz, atributo):
    if len(matriz) == 0:
        return 0
    else:
        return (matriz_reduce_por_somatorio(matriz, atributo) / len(matriz))


def matriz_contar_registro_por_atributo_valor(matriz, atributo, valor):
    quantidade_ocorrencias = 0
    for i in range(len(matriz)):
        if matriz[i][atributo] == valor:
            quantidade_ocorrencias += 1
        else:
            continue
    
    return quantidade_ocorrencias


def matriz_filtra_por_atributo_valor(matriz, atributo, valor):
    quantidade_ocorrencias = matriz_contar_registro_por_atributo_valor(matriz, atributo, valor)
    nova_matriz = criar_matriz(quantidade_ocorrencias, len(matriz[0]))
    cont = 0
    while cont < len(nova_matriz):
        for i in range(len(matriz)):
            if matriz[i][atributo] == valor:
                nova_matriz[cont] = matriz[i]
                cont += 1
            else:
                pass

    return nova_matriz
