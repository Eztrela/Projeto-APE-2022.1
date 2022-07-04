import os, time, tabuleiro, animations, funcionalidades, random, re


def loading_clear():
    """
        Função que limpa o terminal
        
        Recebe: nada
        Retorna: nada
        
        Desenvolvido por Pablo Eztrela, comentado por Juan Leite
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    animations.loading(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')


def imprime_menu_principal():
    """
        Função para mostrar o menu inicial em tela.
    
        Recebe do usuário os inteiros "1" ou "2"
        (1 para começar um novo jogo e 2 para encerrar o programa)
        e retorna a opção escolhida pelo usuário
        
        Desenvolvido por Matheus Pereira, comentado por Juan Leite
    """    
    loading_clear()
    
    print(f'Escolha entre as opções a seguir:\n')
    print(f'Novo Jogo       -> 1')
    print(f'Encerrar        -> 2')
    opcao = int(input(f'\nDigite opção desejada: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    return opcao


def carrega_menu():
    '''
        Exibe na tela os caracteres ASCII do jogo  
        
        Carrega o menu de opçoes do jogo e decide qual a próxima operação,
        seja de criar um novo jogo ou encerrar o jogo atual
        
        Desenvolvido por Juan Leite, comentado por Matheus Pereira
        
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
   ######              ##               ###     ###                        ##   ##                              ### 
    ##  ##             ##                ##      ##                        ###  ##                               ## 
    ##  ##   ####     #####    ####      ##      ##       ####             #### ##   ####    ##  ##    ####      ## 
    #####       ##     ##         ##     ##      #####       ##            ## ####      ##   ##  ##       ##     ## 
    ##  ##   #####     ##      #####     ##      ##  ##   #####            ##  ###   #####   ##  ##    #####     ## 
    ##  ##  ##  ##     ## ##  ##  ##     ##      ##  ##  ##  ##            ##   ##  ##  ##    ####    ##  ##     ## 
   ######    #####      ###    #####    ####    ###  ##   #####            ##   ##   #####     ##      #####    #### 

''')
    time.sleep(5)
    
    while(True):
        
        #Carrega o menu em um loop(enquanto o usuário não falar uma opção válida)
        
        opcao = funcionalidades.imprime_menu_principal()

        if(opcao == 1):
            inicia_jogo()

        elif(opcao == 2):
            encerra_jogo()
            break

        else:
            print(f'A opção {opcao} é inválida. Por favor, digite novamente.')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue


def inicia_jogo():
    '''
        Recebe o nome dos jogadores e chama a função que sorteia a ordem
        de jogadas de cada jogador
        
        Logo após, chama a função responsável por criar o tabuleiro de cada jogador
        
        No final, temos a ordem de jogadas e o tabuleiro preenchido, com base no
        valor informado
        
        Desenvolvido por Pablo Eztrela, comentado por Juan Leite
    '''

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

    while True:
        tam_frota = int(input(f'De quantos navios será formada a frota de cada jogador? '))
        if tam_frota <= 10 and tam_frota >= 1:
            break
        else:
            if tam_frota > 10:
                print('\nO tamanho da frota não pode exceder 10 navios. Por favor, digite novamente.\n')
            else:
                print('\nO tamanho da frota não pode ser nulo. Por favor, digite novamente.\n')
            continue

    tabuleiro_jogador1 = tabuleiro.preenche_tabuleiro(tabuleiro_jogador1,tam_frota)
    tabuleiro_jogador2 = tabuleiro.preenche_tabuleiro(tabuleiro_jogador2,tam_frota)
    # gabarito_jogador1 = tabuleiro_jogador1
    # gabarito_jogador2 = tabuleiro_jogador2

    loading_clear()

    jogadas(nome_jogador1,nome_jogador2,tabuleiro_jogador1,tabuleiro_jogador2)


def encerra_jogo():
    '''
    Função que encerra o Jogo
    
    Desenvolvido por Juan Leite, Comentado por Matheus Pereira
    '''
    
    loading_clear()

    print(f'ESPERO QUE TENHA SE DIVERTIDO!\n\nATÉ A PRÓXIMA!')
    time.sleep(3)


def sorteio_jogador(jog1, jog2):
    """
        Função para sortear o jogador que irá iniciar a partida

        Recebe como parâmetro os nomes dos jogadores
        
        Retorna o jogador sorteado para começar
        
        Desenvolvido por Matheus, Comentado por Juan Leite
    """

    print('\nPrimeiro, vamos sortear quem começa jogando.\n')

    
    animations.loading(0.1) # Exibe a animação em tela

    # Coloca os jogadores numa lista e sorteia um dos dois, atribuindo o resultado numa variável
    lista = [jog1,jog2]
    jogador_sorteado = random.choice(lista)

    print(f"O jogador sorteado foi '{jogador_sorteado}' e irá jogar primeiro.")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    return jogador_sorteado # Retorna o jogador sorteado


def jogada(jogador, tab_jogador, tab_oponente):
    '''
    Função que mostra a situação atual do tabuleiro, caso o usuário queira,
    como parâmetros:
        jogador da vez
        tabuleiro do jogador atual 
        tabuleiro do oponente
      
    Após, realiza a jogada do jogador e verifica se: 
        acertou a frota inimiga
        digitou uma posição já atacada 
        ou acertou a água.
  
    Desenvolvido por Pablo Eztrela, Comentado por Matheus Pereira
    '''
    while True:
        if(verifica_vitoria(tab_oponente)):
            break
        print(f'\nVez de {jogador}.\n')

        print('(Caso queira visualizar a sua frota distribuída no tabuleiro, digite a posição 0x0.)\n')

        lin = input('Escolha a linha de ataque (A-J): ').upper().strip()
        
        #col in ['0','1','2','3','4','5','6','7','8','9','10']

        
        col = input('\nEscolha a coluna de ataque (1-10): ')  

        if(verifica_entradas_jogada(col,lin)): 
            col = int(col)
        else:
            print(f'\nValores inválidos. Por favor, digite novamente.')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        

        print()
        animations.loading(0.05)
        os.system('cls' if os.name == 'nt' else 'clear')

        if(lin == '0' and col == 0):
            print(f'Frota de {jogador}:\n')
            tabuleiro.mostra_gabarito(tab_jogador)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
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


def verifica_entradas_jogada(col,lin):
    '''
    Função que verifica se a entrada dos parâmetros da jogada foi correto,
    retornando False (caso a jogada seja inválida) ou True (caso seja válida), 
    recebendo como parâmetro a coluna e linha informados pelo jogador
    
    Desenvolvido por Juan Leite, comentado por Matheus Pereira
    '''
    if((col not in ['0','1','2','3','4','5','6','7','8','9','10']) or (not re.match('[0abcdefghijABCDEFGHIJ]{1}$', lin))):
        return False
    else:
        return True


def jogadas(nome_jogador1, nome_jogador2,tabuleiro_jogador1, tabuleiro_jogador2 ):
    '''
    Função que determina se o jogo deve continuar ou ser encerrado
    Recebe os parâmetros:
        nome dos jogadores
        tabuleiro dos jogadores
    
    Desenvolvido por Pablo Eztrela, comentado por Juan Leite
    '''

    print('Hora de jogar!')

    while(True):

        funcionalidades.jogada(nome_jogador1, tabuleiro_jogador1, tabuleiro_jogador2)
        os.system('cls' if os.name == 'nt' else 'clear')

        if(verifica_vitoria(tabuleiro_jogador2)):
            
            print(f'EITA! {nome_jogador1} afundou todos os navios de {nome_jogador2}.')
            print(f'\nPARABÉNS, {nome_jogador1}! VOCÊ GANHOU O JOGO.')
            
            print(f'\nTabuleiro de {nome_jogador1} após o término do jogo:\n')
            tabuleiro.mostra_gabarito(tabuleiro_jogador1)
            
            print(f'\nTabuleiro de {nome_jogador2} após o término do jogo:\n')
            tabuleiro.mostra_gabarito(tabuleiro_jogador2)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            break


        funcionalidades.jogada(nome_jogador2, tabuleiro_jogador2, tabuleiro_jogador1)
        

        if(verifica_vitoria(tabuleiro_jogador1)):
            
            print(f'EITA! {nome_jogador2} afundou todos os navios de {nome_jogador1}.')
            print(f'\nPARABÉNS, {nome_jogador2}! VOCÊ GANHOU O JOGO.')
            
            print(f'\nTabuleiro de {nome_jogador2} após o término do jogo:\n')
            tabuleiro.mostra_gabarito(tabuleiro_jogador2)
            
            print(f'\nTabuleiro de {nome_jogador1} após o término do jogo:\n')
            tabuleiro.mostra_gabarito(tabuleiro_jogador1)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def verifica_vitoria(tabuleiro):
    """
        Verifica se ainda existem navios a serem localizados no tabuleiro

        Retorna True caso todos os navios tenham sido apontados pelo oponente
        
        Desenvolvido por Matheus Pereira, comentado por Juan Leite
    """

    # Varre o tabuleiro
    for linhas in tabuleiro:

        # Se achar "N" (ou seja, um navio não encontrado pelo adversário), o jogo deve continuar
        if ('N' in linhas):
            return False
    
    # Se o for não encontrar um navio, a função retorna true, isto é, um jogador venceu a partida
    return True
