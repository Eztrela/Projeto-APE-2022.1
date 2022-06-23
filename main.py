import os
import tabuleiro
import animations


# Arquivo principal
print('Batalha Naval')



while(True):
    print(f'Escolha entre as opções a seguir: ')
    print(f'Novo Jogo       -> 1')
    print(f'Configurações   -> 2')
    print(f'Encerrar        -> 3')
    opcao = int(input(f'\nDigite opção desejada: '))
    animations.loading()
    os.system('clear')

    if(opcao == 1):
        print(f'Começo do jogo \n')
        tabuleiro_jogador1 = tabuleiro.cria_tabuleiro()
        tabuleiro_jogador2 = tabuleiro.cria_tabuleiro()
        tam_frota = int(input(f'De quantos Navios será formada a frota de cada jogador? '))
    elif(opcao == 2):
        print(f'opcao 2')
    elif(opcao == 3):
        print(f'opcao 3')
    else:
        print(f'A opção {opcao} é invalida digite novamente')
        continue


    print(f'Começo do jogo \n')
    

