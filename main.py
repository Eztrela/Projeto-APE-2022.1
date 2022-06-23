import os, time, tabuleiro, animations, funcionalidades


# Arquivo principal
print('Batalha Naval')

modo_jogo = 'normal'
tamanho_tabuleiro = 10

while(True):
    
    opcao = funcionalidades.imprime_menu_principal()

    if(opcao == 1):
        animations.loading(0.1)
        os.system('clear')
        print(f'Início do jogo \n')
        nome_jogador1 = input(f'nome do jogador 1: ')
        nome_jogador2 = input(f'nome do jogador 2: ')
        tabuleiro_jogador1 = tabuleiro.cria_tabuleiro()
        tabuleiro_jogador2 = tabuleiro.cria_tabuleiro()
        tam_frota = int(input(f'De quantos Navios será formada a frota de cada jogador? '))
    elif(opcao == 2):
        animations.loading(0.1)
        os.system('clear')
        print(f'Configurações:\n')
        print(f'( 1 ) Modo de jogo:       {modo_jogo}')
        print(f'( 2 )Tamanho tabuleiro:  {tamanho_tabuleiro}x{tamanho_tabuleiro}')
        config = int(input((f'O que deseja fazer: ')))

    elif(opcao == 3):
        animations.loading(0.1)
        os.system('clear')
        print(f'ESPERO QUE TENHA SE DIVERTIDO!!!!!\n ATÉ A PRÓXIMA!!!!!')
        time.sleep(4)
        break
    else:
        print(f'A opção {opcao} é invalida digite novamente')
        time.sleep(1.5)
        os.system('clear')
        continue

    

