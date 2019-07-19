import datetime
from app_utils import *
from utils import *
from app_utils import *
import os


def main():
    dados = abrir_arquivo('access.log')
    inicio(dados)
    texto_menu = '******* RELATÓRIO DO LOG DE ACESSOS *******\n' \
             '1 - Mostrar dados\n' \
             '2 - Buscar acessos por palavra-chave\n' \
             '3 - Sites acessados, por IP\n' \
             '4 - Total de bytes transferidos, por IP\n' \
             '5 - Percentual de sites encontrados na cache e trazidos na internet\n' \
             '6 - Lista de sites com acesso negado, por IP\n' \
             '7 - Sites acessados por um cliente, em determinada data\n' \
             '8 - Média de tempo de resposta das das requisições, por Data e IP de Destino\n' \
             '9 - Volume de dados por Download e por Upload\n' \
             '10 - Top N endereços IP por volume de dados\n' \
             '0 - Sair\n' \
             '>>> '

    opcao = -1
    while opcao != 0:
        opcao = int(input(texto_menu))
        if opcao == 1:
            for i in dados:
                print(i)
        elif opcao == 2:
            nome = input('Digite um termo para busca:\n' \
                         '>>> ')
            buscar_acessos_por_nome(dados, nome)
        elif opcao == 3:
            sites_por_ip(dados)
        elif opcao == 4:
            bytes_por_ip(dados)
        elif opcao == 5:
            percentual_cache_e_internet(dados)
        elif opcao == 6:
            listar_sites_com_acesso_negado(dados)
        elif opcao == 7:
            sites_acessados_por_dia(dados)
        elif opcao == 8:
            media_tempo_de_resposta(dados)
        elif opcao == 9:
            volume_downloads_e_uploads(dados)
        elif opcao == 10:
            top_acessos(dados)
        elif opcao == 0:
            exit()
        else:
            print('Opção inválida!')
    
        input('\nPressione Enter para continuar......')
        os.system('clear')


if __name__ == '__main__':
    main()