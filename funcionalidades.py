import os, time, tabuleiro, animations, funcionalidades, random


def imprime_menu_principal():
    
    loading_clear()
    
    print(f'Escolha entre as opções a seguir:\n')
    print(f'Novo Jogo       -> 1')
    print(f'Encerrar        -> 2')
    opcao = int(input(f'\nDigite opção desejada: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    return opcao


def jogada(jogador, tab_oponente):
    
    while True:
        if(verifica_vitoria(tab_oponente)):
            break
        print(f'\nVez de {jogador}.\n')

        lin = input('Escolha a linha de ataque (A-J): ').upper().strip()
        col = int(input('\nEscolha a coluna de ataque (1-10): '))
        
        if(lin not in 'ABCDEFGHIJ' or col not in [1,2,3,4,5,6,7,8,9,10]):
            print(f'\nValores Invalidos por favor digite novamente!!!')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
            
        
        print(f'\n{jogador} atacou a posição {lin}{col}.\n')
        lin = tabuleiro.transforma_linha(lin)
        if tab_oponente[lin][col] == 'N':
            tab_oponente[lin][col] = 'F'
            print('FOGO!\n')
            tabuleiro.mostra_tabuleiro(tab_oponente)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif(tab_oponente[lin][col] == 'F' or tab_oponente[lin][col] == 'A'):
            print('Essa posição já foi atacada. Por favor, escolha outra.')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            tab_oponente[lin][col] = 'A'
            print('ÁGUA!\n')
            tabuleiro.mostra_tabuleiro(tab_oponente)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def carrega_menu():

    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
   ######              ##               ###     ###                        ##   ##                              ### #
    ##  ##             ##                ##      ##                        ###  ##                               ## #
    ##  ##   ####     #####    ####      ##      ##       ####             #### ##   ####    ##  ##    ####      ## #
    #####       ##     ##         ##     ##      #####       ##            ## ####      ##   ##  ##       ##     ## #
    ##  ##   #####     ##      #####     ##      ##  ##   #####            ##  ###   #####   ##  ##    #####     ## #
    ##  ##  ##  ##     ## ##  ##  ##     ##      ##  ##  ##  ##            ##   ##  ##  ##    ####    ##  ##     ## #
   ######    #####      ###    #####    ####    ###  ##   #####            ##   ##   #####     ##      #####    #### #

''')
    time.sleep(5)

    while(True):

        opcao = funcionalidades.imprime_menu_principal()

        if(opcao == 1):
            inicia_jogo()

        elif(opcao == 2):
            encerra_jogo()
            break

        else:
            print(f'A opção {opcao} é invalida digite novamente')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue


def inicia_jogo():

    loading_clear()

    print(f'Início do jogo \n')

    nome_jogador1 = input(f'Nome do jogador 1: ')
    nome_jogador2 = input(f'Nome do jogador 2: ')
    aux = ''
    
    jogador_sorteado = funcionalidades.sorteio_jogador(nome_jogador1, nome_jogador2)
    if(jogador_sorteado == nome_jogador2):
        aux = nome_jogador1
        nome_jogador1 = jogador_sorteado
        nome_jogador2 = aux
    


    tabuleiro_jogador1 = tabuleiro.cria_tabuleiro()
    tabuleiro_jogador2 = tabuleiro.cria_tabuleiro()

    tam_frota = int(input(f'De quantos Navios será formada a frota de cada jogador? '))

    tabuleiro_jogador1 = tabuleiro.preenche_tabuleiro(tabuleiro_jogador1,tam_frota)
    tabuleiro_jogador2 = tabuleiro.preenche_tabuleiro(tabuleiro_jogador2,tam_frota)
    gabarito_jogador1 = tabuleiro_jogador1
    gabarito_jogador2 = tabuleiro_jogador2

    loading_clear()

    jogadas(nome_jogador1,nome_jogador2,tabuleiro_jogador1,tabuleiro_jogador2)

def encerra_jogo():
    
    loading_clear()

    print(f'ESPERO QUE TENHA SE DIVERTIDO!!!!!\n ATÉ A PRÓXIMA!!!!!')
    time.sleep(3)

def loading_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    animations.loading(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')

def jogadas(nome_jogador1, nome_jogador2,tabuleiro_jogador1, tabuleiro_jogador2 ):

    while(True):

        print('Hora de jogar!')


        funcionalidades.jogada(nome_jogador1, tabuleiro_jogador2)
        os.system('cls' if os.name == 'nt' else 'clear')

        if(verifica_vitoria(tabuleiro_jogador2)):
            
            print(f'{nome_jogador1} Afundou todos os Navios de {nome_jogador2}')
            print(f'{nome_jogador1} GANHOU O JOGO')
            
            print(f'Tabuleiro {nome_jogador1} após termino do jogo:\n')
            tabuleiro.mostra_tabuleiro(tabuleiro_jogador1)
            
            print(f'Tabuleiro {nome_jogador2} após termino do jogo:\n')
            tabuleiro.mostra_tabuleiro(tabuleiro_jogador2)
            time.sleep(5)
            loading_clear()
            break

        

        funcionalidades.jogada(nome_jogador2, tabuleiro_jogador1)
        

        if(verifica_vitoria(tabuleiro_jogador1)):
            
            print(f'{nome_jogador2} Afundou todos os Navios de {nome_jogador1}')
            print(f'{nome_jogador2} GANHOU O JOGO')
            
            print(f'Tabuleiro {nome_jogador2} após termino do jogo:\n')
            tabuleiro.mostra_tabuleiro(tabuleiro_jogador2)
            
            print(f'Tabuleiro {nome_jogador1} após termino do jogo:\n')
            tabuleiro.mostra_tabuleiro(tabuleiro_jogador1)
            time.sleep(5)
            loading_clear()
            break



def verifica_vitoria(tabuleiro):
    for linhas in tabuleiro:
        if ('N' in linhas):
            return False
    return True


def sorteio_jogador(jog1, jog2):
    print('\nPrimeiro, vamos sortear quem começa jogando.\n')
    animations.loading(0.1)
    lista = [jog1,jog2]
    jogador_sorteado = random.choice(lista)
    print(f'O jogador sorteado foi {jogador_sorteado} e irá jogar primeiro.')
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    return jogador_sorteado
