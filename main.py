import os, time, tabuleiro, animations, funcionalidades


# Arquivo principal
print('Batalha Naval')

while(True):
    
    opcao = funcionalidades.imprime_menu_principal()

    if(opcao == 1):
        animations.loading(0.1)
        os.system('clear')
        print(f'Início do jogo \n')
        nome_jogador1 = input(f'Nome do jogador 1: ')
        nome_jogador2 = input(f'Nome do jogador 2: ')
        tabuleiro_jogador1 = tabuleiro.cria_tabuleiro()
        tabuleiro_jogador2 = tabuleiro.cria_tabuleiro()
        tam_frota = int(input(f'De quantos Navios será formada a frota de cada jogador? '))
    elif(opcao == 2):
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

    

