import os, time, tabuleiro, animations, funcionalidades


def imprime_menu_principal():
    
    loading()
    
    print(f'Escolha entre as opções a seguir:\n')
    print(f'Novo Jogo       -> 1')
    print(f'Encerrar        -> 2')
    opcao = int(input(f'\nDigite opção desejada: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    return opcao


def jogada(jogador, tab_oponente):
    print(f'\nVez de {jogador}.\n')
    while True:
        if(verifica_vitoria(tab_oponente)):
            break
        lin = input('Escolha a linha de ataque (A-J): ').upper().strip()
        col = int(input('\nEscolha a coluna de ataque (1-10): '))

        print(f'\n{jogador} atacou a posição {lin}{col}.\n')
        lin = tabuleiro.transforma_linha(lin)
        if tab_oponente[lin][col] == 'N':
            tab_oponente[lin][col] = 'F'
            print('FOGO!\n')
            tabuleiro.mostra_tabuleiro(tab_oponente)
            continue
        else:
            tab_oponente[lin][col] = 'A'
            print('ÁGUA!\n')
            tabuleiro.mostra_tabuleiro(tab_oponente)
            break


def carrega_menu():

    while(True):

        opcao = funcionalidades.imprime_menu_principal()

        if(opcao == 1):
            inicia_jogo()

        elif(opcao == 2):
            encerra_jogo()
            break

        else:
            print(f'A opção {opcao} é invalida digite novamente')
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue


def inicia_jogo():

    loading()

    print(f'Início do jogo \n')

    nome_jogador1 = input(f'Nome do jogador 1: ')
    nome_jogador2 = input(f'Nome do jogador 2: ')
    tabuleiro_jogador1 = tabuleiro.cria_tabuleiro()
    tabuleiro_jogador2 = tabuleiro.cria_tabuleiro()

    tam_frota = int(input(f'De quantos Navios será formada a frota de cada jogador? '))

    tabuleiro_jogador1 = tabuleiro.preenche_tabuleiro(tabuleiro_jogador1,tam_frota)
    tabuleiro_jogador2 = tabuleiro.preenche_tabuleiro(tabuleiro_jogador2,tam_frota)

    loading()

    jogadas(nome_jogador1,nome_jogador2,tabuleiro_jogador1,tabuleiro_jogador2)

def encerra_jogo():
    
    loading()

    print(f'ESPERO QUE TENHA SE DIVERTIDO!!!!!\n ATÉ A PRÓXIMA!!!!!')
    time.sleep(4)

def loading():
    os.system('cls' if os.name == 'nt' else 'clear')
    animations.loading(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')

def jogadas(nome_jogador1, nome_jogador2,tabuleiro_jogador1, tabuleiro_jogador2 ):

    while(True):

        print('Hora de jogar!')

        funcionalidades.jogada(nome_jogador1, tabuleiro_jogador2)

        if(verifica_vitoria(tabuleiro_jogador2)):
            
            print(f'{nome_jogador1} Afundou todos os Navios de {nome_jogador2}')
            print(f'{nome_jogador1} GANHOU O JOGO')
            
            print(f'Tabuleiro {nome_jogador1} após termino do jogo:\n')
            tabuleiro.mostra_tabuleiro(tabuleiro_jogador1)
            
            print(f'Tabuleiro {nome_jogador2} após termino do jogo:\n')
            tabuleiro.mostra_tabuleiro(tabuleiro_jogador2)
            time.sleep(8)
            break

        time.sleep(4)

        funcionalidades.jogada(nome_jogador2, tabuleiro_jogador1)

        if(verifica_vitoria(tabuleiro_jogador1)):
            
            print(f'{nome_jogador2} Afundou todos os Navios de {nome_jogador1}')
            print(f'{nome_jogador2} GANHOU O JOGO')
            
            print(f'Tabuleiro {nome_jogador2} após termino do jogo:\n')
            tabuleiro.mostra_tabuleiro(tabuleiro_jogador2)
            
            print(f'Tabuleiro {nome_jogador1} após termino do jogo:\n')
            tabuleiro.mostra_tabuleiro(tabuleiro_jogador1)
            time.sleep(8)
            break

def verifica_vitoria(tabuleiro):
    for linhas in tabuleiro:
        if ('N' in linhas):
            return False
    return True