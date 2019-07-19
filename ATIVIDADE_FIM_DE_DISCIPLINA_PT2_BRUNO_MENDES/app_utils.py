from utils import *
import datetime
import os
from ordenacao import *


def abrir_arquivo(arquivo):
    dados = []
    log = open(arquivo)
    for linha in log.readlines():
        dado = linha.split(' ')
        dado[0] = tempo_legivel(dado[0])
        dado = vetor_remover_valor(dado, '')
        dados = vetor_inserir_final(dados, dado)

    return dados


def tempo_legivel(tempo):
    timestamp = float(tempo)
    value = datetime.datetime.fromtimestamp(timestamp)
    return value.strftime('%Y-%m-%d %H:%M:%S')


def inicio(dados):
    print('foram carregados %d dados' % (len(dados)))
    input('Pressione Enter para continuar........')
    os.system('clear')


def buscar_acessos_por_nome(dados, nome):
    for i in range(len(dados)):
        if nome in dados[i][6]:
            print(dados[i][6])
        else:
            pass


def sites_por_ip(dados):
    quer_ip = input('Deseja buscar por um IP específico? (S) ou (N)\n' \
                    '>>> ')
    if quer_ip == 'S':
        ip_desejado = input('Digite um IP para busca:\n' \
                            '>>> ')
        print('%s acessou %d sites diferentes' % (ip_desejado, qtd_sites_por_ip(dados, ip_desejado)))
    
    if quer_ip == 'N':
        for i in lista_ips(dados):
            print('%s acessou %d sites diferentes' % (i, qtd_sites_por_ip(dados, i)))


def qtd_sites_por_ip(dados, ip_desejado):
    dados_filtrados = matriz_filtra_por_atributo_valor(dados, 2, ip_desejado)
    qtd_sites = 0
    sites = []
    for i in range(len(dados_filtrados)):
        if dados[i][6] in sites:
            pass
        else:
            sites = vetor_inserir_final(sites, dados[i][6])
    
    return len(sites)


def listar_sites_e_acesso_por_ip(dados, ip_desejado):
    dados_filtrados = matriz_filtra_por_atributo_valor(dados, 2, ip_desejado)
    qtd_sites = 0
    sites = []
    acessos = []
    for i in range(len(dados_filtrados)):
        if dados[i][6] in sites:
            pass
        else:
            sites = vetor_inserir_final(sites, dados[i][6])
            acessos = vetor_inserir_final(acessos, dados[i][3])
    
    return sites, acessos


def lista_ips(dados):
    ips = []
    for i in range(len(dados)):
        if dados[i][2] in ips:
            pass
        else:
            ips = vetor_inserir_final(ips, dados[i][2])
    
    return ips


def bytes_por_ip(dados):
    quer_ip = input('Deseja buscar por um IP específico? (S) ou (N)\n' \
                    '>>> ')
    if quer_ip == 'S':
        ip_desejado = input('Digite um IP para busca:\n' \
                            '>>> ')
        print('%s transferiu %d bytes no total.' % (ip_desejado, qtd_bytes_por_ip(dados, ip_desejado)))
    
    if quer_ip == 'N':
        for i in lista_ips(dados):
            print('%s transferiu %d bytes no total' % (i, qtd_bytes_por_ip(dados, i)))


def qtd_bytes_por_ip(dados, ip_desejado):
    total_bytes = 0
    dados_filtrados = matriz_filtra_por_atributo_valor(dados, 2, ip_desejado)
    for i in range(len(dados_filtrados)):
        total_bytes += int(dados_filtrados[i][4])
    
    return total_bytes


def percentual_cache_e_internet(dados):
    sites_diferentes = []
    direct_ou_none = []
    qtd_direct = 0
    qtd_none = 0
    
    for i in range(len(dados)):
        if dados[i][6] in sites_diferentes:
            pass
        else:
            sites_diferentes = vetor_inserir_final(sites_diferentes, dados[i][6])
            direct_ou_none = vetor_inserir_final(direct_ou_none, dados[i][8])
    
    for i in direct_ou_none:
        if 'DIRECT' in i:
            qtd_direct += 1
        elif 'NONE' in i:
            qtd_none += 1
    
    porc_direct = (qtd_direct/len(direct_ou_none)) * 100
    porc_none = (qtd_none/len(direct_ou_none)) * 100

    print('\n******* ANÁLISE DA ORIGEM DOS SITES ACESSADOS *******\n' \
          'Porcentagem de sites encontrados na cache: %.2f\n' \
          'Porcentagem de sites encontrados retirados da internet: %.2f\n' \
            % (porc_none, porc_direct))


def listar_sites_com_acesso_negado(dados):
    quer_ip = input('Deseja buscar por um IP específico? (S) ou (N)\n' \
                    '>>> ')
    if quer_ip == 'S':
        ip_desejado = input('Digite um IP para busca:\n' \
                            '>>> ')
        sites_acessados, codigo_acesso = listar_sites_e_acesso_por_ip(dados, ip_desejado)
        print('\nSites digitados pelo IP %s que tiveram o acesso negado:' % (ip_desejado))
        for i in range(len(sites_acessados)):
            if 'DENIED' in codigo_acesso[i]:
                print(sites_acessados[i])
            else:
                pass
    
    elif quer_ip == 'N':
        for i in lista_ips(dados):
            sites_acessados, codigo_acesso = listar_sites_e_acesso_por_ip(dados, i)
            print('\nSites digitados pelo IP %s que tiveram o acesso negado:' % (i))
            for j in range(len(sites_acessados)):
                if 'DENIED' in codigo_acesso[j]:
                    print(sites_acessados[j])
                else:
                    pass


def sites_acessados_por_dia(dados):
    ip = input('Digite o IP do cliente:\n' \
               '>>> ')
    data = input('Digite a data desejada, no formato AAAA-MM-DD:\n' \
                 '>>> ')
    print('\n******** SITES ACESSADOS PELO CLIENTE DE IP %s NA DATA %s********\n' % (ip, data))
    for i in range(len(dados)):
        if dados[i][2] == ip and data in dados[i][0]:
            print(dados[i][6])
        else:
            pass


def media_tempo_de_resposta(dados):
    volume_dados_transferidos = []
    data = input('Digite a data desejada, no formato AAAA-MM-DD:\n' \
                 '>>> ')
    ip_destino = input('Digite o IP destino:\n' \
                 '>>> ')
    
    for i in range(len(dados)):
        if dados[i][0] == data and ip_destino in dados[i][8]:
            volume_dados_transferidos = vetor_inserir_final(volume_dados_transferidos, int(dados[i][4]))
        else:
            pass
    
    media = vetor_reduce_por_media(volume_dados_transferidos)

    print('A média de dados transferidos pelo IP %s, na data digitada, é de %.2f' % (ip_destino, media))


def volume_downloads_e_uploads(dados):
    volume_dados_transferidos_download = 0
    volume_dados_transferidos_upload = 0
    for i in range(len(dados)):
        if dados[i][5] == 'GET':
            volume_dados_transferidos_download += int(dados[i][4])
        elif dados[i][5] == 'POST':
            volume_dados_transferidos_upload += int(dados[i][4])
    
    print('Dados trafegados por meio de Download: %d bytes' % (volume_dados_transferidos_download))
    print('Dados trafegados por meio de Upload: %d bytes' % (volume_dados_transferidos_upload))


def top_acessos(dados):
    n = int(input('Digite N para que seja feito o Top N:\n' \
                  '>>> '))
    cont = 0
    ip_maquina_conectada = ''
    ip_numero = ''



def pegar_numero_de_ip(ip_maquina_conectada):
    for i in ip_maquina_conectada:
        if i not in '0123456789.':
            pass
        else:
            ip_numero += i
    
    return ip_numero


def volume_dados_por_ip(dados, ip_maquina_conectada):
    for i in range(len(dados)):
        if dados[i][8] ==