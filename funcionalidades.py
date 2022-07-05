# Importa as bibliotecas que são utilizadas no código
import os
import time
import tabuleiro
import animations
import funcionalidades
import random
import re


def loading_clear():
    """
        Função que limpa o terminal após uma animação de loading

        Desenvolvido por Pablo Eztrela, comentado por Juan Leite
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    animations.loading(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')


def imprime_menu_principal():
    """
        Função para mostrar o menu inicial em tela

        Recebe do jogador o valor que ele escolhe como opção do menu

        Retorna a opção escolhida pelo jogador

        Desenvolvido por Matheus Pereira, comentado por Juan Leite
    """

    # Chama a função que imprime na tela uma animação de loading e em seguida limpa o terminal
    loading_clear()

    # Cria um laço infinito
    while True:
        # Imprime o menu principa e suas opções
        print(f'Escolha entre as opções a seguir:\n')
        print(f'Novo Jogo       -> 1')
        print(f'Encerrar        -> 2')

        # Cria uma variável que recebe o valor digitado pelo jogador como a opção escolhida
        opcao = input(f'\nDigite opção desejada: ')

        # Verifica se o valor digitado pelo jogador é um número inteiro e, caso verdadeiro, converte a variável de str para int
        if opcao.isnumeric():
            opcao = int(opcao)

            # Verifica se a opção digitada pelo jogador foi diferente de 1 e 2 e, caso verdadeiro, imprime uma mensagem que indica que esse valor é inválido
            if opcao != 1 and opcao != 2:
                print('\nEssa opção não é válida. Por favor, digite novamente.\n')

                # Para a execução do programa por 3 segundos
                time.sleep(3)

                # Chama a função que limpa o terminal de execução
                os.system('cls' if os.name == 'nt' else 'clear')

                # Continua o laço, pois a opção digitada pelo jogador foi inválida
                continue

            # Como a opção digitada pelo jogador foi 1 ou 2, encerra o laço
            else:
                break

        # Como a opção digitada pelo jogador não foi um número inteiro, imprime uma mensagem que indica que esse valor é inválido
        else:
            print('\nEssa opção não é válida. Por favor, digite novamente.\n')

            # Para a execução do programa por 3 segundos
            time.sleep(3)

            # Chama a função que limpa o terminal de execução
            os.system('cls' if os.name == 'nt' else 'clear')

            # Continua o laço, pois a opção digitada pelo jogador foi inválida
            continue

    # Chama a função que limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    return opcao  # Retorna variável da opção escolhida


def titulo_jogo():
    '''
    Função que exibe na tela o título do jogo por 5 segundos

    Desenvolvido por Marcela Kramer, Comentado por Juan Leite

    '''

    # Chama a função que limpa o terminal antes de exibir o título
    os.system('cls' if os.name == 'nt' else 'clear')

    # Imprime o título em uma formatação de destaque
    print('''
   ######              ##               ###     ###                        ##   ##                              ### 
    ##  ##             ##                ##      ##                        ###  ##                               ## 
    ##  ##   ####     #####    ####      ##      ##       ####             #### ##   ####    ##  ##    ####      ## 
    #####       ##     ##         ##     ##      #####       ##            ## ####      ##   ##  ##       ##     ## 
    ##  ##   #####     ##      #####     ##      ##  ##   #####            ##  ###   #####   ##  ##    #####     ## 
    ##  ##  ##  ##     ## ##  ##  ##     ##      ##  ##  ##  ##            ##   ##  ##  ##    ####    ##  ##     ## 
   ######    #####      ###    #####    ####    ###  ##   #####            ##   ##   #####     ##      #####    #### 

''')

    # Chama a função que para o programa por 5 segundos
    time.sleep(5)


def carrega_menu():
    '''
    Função que carrega o menu de opçoes do jogo e decide qual a próxima operação,
    seja de criar um novo jogo ou encerrar o jogo atual

    Desenvolvido por Juan Leite, comentado por Matheus Pereira

    '''

    # Chama a função que exibe o título do jogo
    titulo_jogo()

    # Cria um laço infinito
    while(True):

        # Cria uma variável cujo valor é aquele retornado pela função que imprime o menu principal na tela
        opcao = imprime_menu_principal()

        # Verifica se a opção digitada foi 1 e, caso verdadeiro, chama a função que inicia o jogo
        if(opcao == 1):
            inicia_jogo()

        # Verifica se a opção digitada foi 2 e, caso verdadeiro, chama a função que encerra o jogo
        elif(opcao == 2):
            encerra_jogo()

            # Encerra o laço, pois o jogo foi encerrado
            break

        # Como a opção digitada não foi 1 ou 2, ela é inválida
        else:

            # Imprime a mensagem que indica que a opção digitada foi inválida e pede para o jogador digitar novamente
            print(f'A opção {opcao} é inválida. Por favor, digite novamente.')

            # Para o programa por 1 segundo
            time.sleep(1)

            # Chama a função que limpa o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            # Continua o laço, pois o jogador deve digitar uma opção válida
            continue


def nome_jogador(num):
    '''
    Função que lê o nome do jogador

    Recebe como parâmetro o 'número' do jogador

    Recebe como entrada o nome do jogador

    Retorna o nome do jogador

    Desenvolvido por Juan Leite, Comentado por Juan Leite

    '''

    # Cria um laço infinito
    while True:
        # Cria uma variável que recebe o nome digitado pelo jogador
        nome = input(f'Nome do jogador {num}: ').strip()

        # Verifica se a variável recebeu uma string vazia, isto é, o jogador não digitou nenhum nome
        if nome == '':

            # Imprime uma mensagem indicando que o jogador não digitou nenhum nome
            print(
                f'\nVocê não digitou nenhum nome para o jogador {num}. Por favor, informe o nome desse jogador.\n')

            # Para o programa por 2 segundos
            time.sleep(2)

            # Chama a função que limpa o terminal de execução
            os.system('cls' if os.name == 'nt' else 'clear')

            # Continua o laço, pois nenhum nome foi informado
            continue

        # Como o jogador informou o nome, encerra o laço
        else:
            break

    return nome  # Retorna a variável nome


def exibe_jogadores(jogador1, jogador2):
    '''
    Função que exibe quem são os jogadores

    Recebe o nome dos jogadores

    Desenvolvido por Juan Leite, Comentado por Marcela Kramer 

    '''

    # Imprime quem são os jogadores por 3 segundos
    print('\nVoilà! Temos nossos jogadores:')
    print(f'\nO jogador 1 é {jogador1} e o jogador 2 é {jogador2}.')
    time.sleep(3)


def tamanho_frota():
    """
    Função que define o tamanho da frota a ser utilizada no jogo

    Recebe como entrada um valor que indica a quantidade de navios da frota

    Retorna esse mesmo valor

    Desenvolvido por Pablo Eztrela, Comentado por Pablo Eztrela

    """
    # Chama a função que imprime na tela uma animação de loading e em seguida limpa o terminal
    loading_clear()

    # Cria um laço infinito
    while True:

        # Cria uma variável que recebe o valor digitado pelo jogador como a quantidade de navios da frota
        tam_frota = (
            input(f'De quantos navios será formada a frota de cada jogador? '))

        # Verifica se o valor digitado pelo jogador é um número inteiro e, caso verdadeiro, converte a variável de str para int
        if tam_frota.isnumeric():
            tam_frota = int(tam_frota)

            # Verifica se o tamanho da frota está entre 1 e 10 navios e, caso verdadeiro, encerra o laço
            if tam_frota <= 10 and tam_frota >= 1:
                break

            # Como o tamanho da frota não está entre 1 e 10 navios, executa outra estrutura condicional
            else:

                # Verifica se o tamanho da frota é maior que 10 e, caso verdadeiro, imprime uma mensagem que indica que esse valor é inválido
                if tam_frota > 10:
                    print(
                        '\nO tamanho da frota não pode exceder 10 navios. Por favor, digite novamente.\n')

                    # Para o programa por 2 segundos
                    time.sleep(2)

                    # Chama a função que limpa o terminal
                    os.system('cls' if os.name == 'nt' else 'clear')

                # Como o valor da frota não é maior que 10, ela só pode ser 0
                else:

                    # Imprime uma mensagem que indica que esse valor é inválido
                    print(
                        '\nO tamanho da frota não pode ser nulo. Por favor, digite novamente.\n')

                    # Para o programa por 2 segundos
                    time.sleep(2)

                    # Chama a função que limpa o terminal
                    os.system('cls' if os.name == 'nt' else 'clear')

                # Continua o laço, pois o jogador não digitou um valor válido
                continue

        # Como o valor digitado pelo jogador não é um número inteiro, imprime uma mensagem que indica que esse valor é inválido
        else:
            print('\nO valor digitado é inválido. Por favor, digite novamente.\n')

            # Para o programa por 2 segundos
            time.sleep(2)

            # Chama a função que limpa o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

    return tam_frota  # Retora o tamanho da frota


def inicia_jogo():
    '''   
    Função que inicia o jogo, lendo as informações necessárias para sua continuidade

    Desenvolvido por Pablo Eztrela, comentado por Juan Leite
    '''

    # Chama a função que imprime na tela uma animação de loading e em seguida limpa o terminal
    loading_clear()

    # Imprime uma mensagem que indica o início do jogo
    print(f'Início do jogo \n')

    # Cria variáveis que recebem os nomes retornados da função que os lê
    nome_jogador1 = nome_jogador(1)
    nome_jogador2 = nome_jogador(2)

    # Para o programa por 0.5 segundo
    time.sleep(0.5)

    # Chama a função que exibe quem são os jogadores
    exibe_jogadores(nome_jogador1, nome_jogador2)

    # Cria uma variável auxiliar
    aux = ''

    # Cria uma variável que recebe o nome retornado da função que sorteia um jogador para começar jogando
    jogador_sorteado = funcionalidades.sorteio_jogador(
        nome_jogador1, nome_jogador2)

    # Verifica se o jogador sorteado foi o jogador 2 e, caso verdadeiro, o transforma em jogador 1 por meio de uma variável auxiliar
    if(jogador_sorteado == nome_jogador2):
        aux = nome_jogador1
        nome_jogador1 = jogador_sorteado
        nome_jogador2 = aux

    # Cria variáveis que recebem os tabuleiros retornados da função que os cria para cada um dos jogadores
    tabuleiro_jogador1 = tabuleiro.cria_tabuleiro()
    tabuleiro_jogador2 = tabuleiro.cria_tabuleiro()

    # Cria uma variável que recebe o valor retornado da função que define o tamanho da frota
    tam_frota = tamanho_frota()

    # Preenche o tabuleiro dos jogadores com a devida quantidade de navios a partir da função que realiza essa ação
    tabuleiro_jogador1 = tabuleiro.preenche_tabuleiro(
        tabuleiro_jogador1, tam_frota)
    tabuleiro_jogador2 = tabuleiro.preenche_tabuleiro(
        tabuleiro_jogador2, tam_frota)

    ''' 
    gabarito_jogador1 = tabuleiro_jogador1
    gabarito_jogador2 = tabuleiro_jogador2

    '''

    # Chama a função que imprime na tela uma animação de loading e em seguida limpa o terminal
    loading_clear()

    # Chama a função jogo
    jogo(nome_jogador1, nome_jogador2, tabuleiro_jogador1, tabuleiro_jogador2)


def encerra_jogo():
    '''
    Função que encerra o Jogo

    Desenvolvido por Juan Leite, Comentado por Matheus Pereira
    '''

    # Chama a função que imprime na tela uma animação de loading e em seguida limpa o terminal
    loading_clear()

    # Imprime uma mensagem de despedida por 3 segundos antes de encerrar o programa
    print(f'ESPERO QUE TENHA SE DIVERTIDO!\n\nATÉ A PRÓXIMA!')
    time.sleep(3)


def sorteio_jogador(jog1, jog2):
    """
     Função para sortear o jogador que irá iniciar a partida

     Recebe como parâmetro os nomes dos jogadores

     Retorna o jogador sorteado para começar

     Desenvolvido por Matheus Pereira, Comentado por Juan Leite
    """

    # Chama a função que limpa o terminal de execução
    os.system('cls' if os.name == 'nt' else 'clear')

    # Imprime na tela uma mensagem que indica que o sorteio irá acontecer
    print('Perfeito! Agora, vamos sortear quem começa jogando.\n')

    # Para o programa por 1 segundo
    time.sleep(1)

    loading_clear()  # Exibe uma animação de loading na tela e depois chama a função que limpa o terminal

    # Coloca os jogadores numa lista e sorteia um dos dois, atribuindo o resultado numa variável
    lista = [jog1, jog2]
    jogador_sorteado = random.choice(lista)

    # Imprime na tela quem foi o jogador sorteado por 3 segundos e depois chama a função que limpa o terminal
    print(f"O jogador sorteado foi '{jogador_sorteado}' e irá jogar primeiro.")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    return jogador_sorteado  # Retorna o jogador sorteado


def verifica_entradas_jogada(col, lin):
    '''
    Função que verifica se a entrada dos valores da jogada foi correta

    Recebe a coluna e a linha informadas pelo jogador

    Retorna True(caso a jogada seja válida) ou False(caso a jogada seja inválida)

    Desenvolvido por Juan Leite, comentado por Matheus Pereira
    '''
    # Verifica se o valor da coluna não é um número de 0 a 10 ou o da linha não é uma letra de A-J ou 0
    if((col not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']) or (not re.match('[0abcdefghijABCDEFGHIJ]{1}$', lin))):

        # Caso verdadeiro, retorna False
        return False

    # Verifica se o valor da coluna é igual a 0 e o da linha é uma letra de A-J ou se o valor da coluna é um número de 1 a 10 e o da linha é 0
    elif (col == '0' and re.match('[abcdefghijABCDEFGHIJ]{1}$', lin)) or (col in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] and lin == '0'):

        # Caso verdadeiro, retorna False
        return False

    # Como nenhumas das condições anteriores foi atendida, os valores digitados são válidos
    else:
        return True  # Retorna True


def escolha_ataque(jogador, tab_oponente):
    '''
    Função que permite ao jogador escolher a posição que ele quer atacar no tabuleiro adversário

    Recebe o nome do jogador e o tabuleiro adversário

    Retorna a linha e a coluna escolhida dentro de uma tupla

    Desenvolvido por Marcela Kramer, Comentado por Matheus Pereira
    '''

    # Cria um laço infinito
    while True:

        # Imprime o jogador que deve realizar a jogada
        print(f'Vez de {jogador}.\n')

        # Imprime o tabuleiro do oponente em seu estado atual para que o jogador possa ver as posições já atacadas
        tabuleiro.mostra_tabuleiro(tab_oponente)

        # Imprime a opção do jogador visualizar seu próprio tabuleiro
        print('\n(Caso queira visualizar a sua frota distribuída no tabuleiro, digite a posição 0x0.)\n')

        # Cria uma variável que recebe o valor str digitado pelo jogador para a posição da linha do ataque
        lin = input('Escolha a linha de ataque (A-J): ').upper().strip()

        # Cria uma variável que recebe o valor str digitado pelo jogador para a posição da coluna do ataque
        col = input('\nEscolha a coluna de ataque (1-10): ').strip()

        # Verifica se as entradas digitadas pelo jogador são válidas e, caso verdadeiro, transforma o valor da coluna em um inteiro
        if(verifica_entradas_jogada(col, lin)):
            col = int(col)

            # Encerra o laço, pois o jogador digitou entradas válidas
            break

        # Como o jogador não digitou entradas válidas, imprime uma mensagem que indica que ele deve digitar novos valores
        else:
            print(f'\nValores inválidos. Por favor, digite novamente.')

            # Para o programa por 3 segundos
            time.sleep(3)

            # Chama a função que limpa o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            # Continua o laço, pois o jogador deve digitar novas entradas
            continue

    return lin, col  # Retorna os valores da linha e da coluna


def jogada_ataque(jogador, tab_jogador, tab_oponente):
    '''
    Função que executa o comando de ataque de fato

    Recebe o nome do jogador que realiza o ataque, seu próprio tabuleiro e o tabuleiro adversário

    Desenvolvido por Pablo Eztrela, Comentado por Marcela Kramer

    '''

    # Cria um laço infinito
    while True:

        # Verifica se o jogador derrubou todos os navios adversários
        if verifica_vitoria(tab_oponente):
            return True
        else:

            # Chama a função de escolha de ataque para definir a linha e a coluna que devem ser atacadas
            posicao = escolha_ataque(jogador, tab_oponente)

            # Cria as variáveis de linha e coluna a partir dos valores retornados na função de escolha
            lin = posicao[0]
            col = posicao[1]

            # Imprime uma linha em branco
            print()

            # Chama a função que limpa o terminal de execução após uma animação de loading
            animations.loading(0.05)
            os.system('cls' if os.name == 'nt' else 'clear')

            # Verifica se os valores da linha e da coluna são iguais a 0 e, caso verdadeiro, exibe a frota do jogador por 3 segundos
            if(lin == '0' and col == 0):
                print(f'Frota de {jogador}:\n')
                tabuleiro.mostra_gabarito(tab_jogador)
                time.sleep(3)

                # Chama a função que limpa o terminal de execução
                os.system('cls' if os.name == 'nt' else 'clear')
            else:

                # Imprime na tela a posição que o jogador atacou
                print(f'\n{jogador} atacou a posição {lin}{col}.\n')

                # Chama a função que transforma a variável da linha em um valor inteiro
                lin = tabuleiro.transforma_linha(lin)

                # Verifica se o jogador atingiu um navio e, caso verdadeiro, substitui o 'N', de navio, pelo 'F', de fogo
                if tab_oponente[lin][col] == 'N':
                    tab_oponente[lin][col] = 'F'

                    # Imprime na tela o tabuleiro do oponente por 3 segundos, indicando que o jogador acertou o ataque
                    print('FOGO!\nUm navio foi atingido.\n')
                    tabuleiro.mostra_tabuleiro(tab_oponente)
                    time.sleep(3)

                    # Chama a função que limpa o terminal de execução
                    os.system('cls' if os.name == 'nt' else 'clear')

                    # Continua o laço, pois o jogador acertou a jogada
                    continue

                # Verifica se a posição escolhida pelo jogador está preenchida por 'F' ou 'A' e, caso verdadeiro, imprime uma mensagem, por 3 segundos, indicando que o jogador deve escolher outra posição
                elif(tab_oponente[lin][col] == 'F' or tab_oponente[lin][col] == 'A'):
                    print('Essa posição já foi atacada. Por favor, escolha outra.')
                    time.sleep(3)

                    # Chama a função que limpa o terminal de execução
                    os.system('cls' if os.name == 'nt' else 'clear')

                    # Continua o laço, pois o jogador não realizou a jogada
                    continue

                # Como nenhuma das outras condições é verdadeira, substitui o '.', que indica uma posição vazia, pelo 'A', que indica que o jogador acertou a água
                else:
                    tab_oponente[lin][col] = 'A'

                    # Imprime na tela o tabuleiro do oponente por 3 segundos, indicando que o jogador errou o ataque
                    print('ÁGUA!\nNenhum navio foi atingido.\n')
                    tabuleiro.mostra_tabuleiro(tab_oponente)
                    time.sleep(3)

                    # Chama a função que limpa o terminal de execução
                    os.system('cls' if os.name == 'nt' else 'clear')

                    # Encerra o laço, pois o jogador errou a jogada
                    return False


def mensagem_final(vencedor, perdedor, tab_vencedor, tab_perdedor):
    '''
    Função que exibe na tela a mensagem final do jogo, declarando o vencedor e imprimindo os tabuleiros em seu estado final

    Recebe os nomes do vencedor e do perdedor do jogo, bem como seus tabuleiros

    Desenvolvido por Marcela Kramer, Comentado por Pablo Eztrela

    '''
    # Imprime uma mensagem que indica o jogador vencedor e outra que o parabeniza
    print(f'EITA! {vencedor} afundou todos os navios de {perdedor}.')
    print(f'\nPARABÉNS, {vencedor}! VOCÊ GANHOU O JOGO.')

    # Imprime o tabuleiro do jogador vencedor após o término do jogo
    print(f'\nTabuleiro de {vencedor} após o término do jogo:\n')

    # Chama a função que imprime o gabarito do tabuleiro vencedor
    tabuleiro.mostra_gabarito(tab_vencedor)

    # Imprime o tabuleiro do jogador perdedor após o término do jogo
    print(f'\nTabuleiro de {perdedor} após o término do jogo:\n')

    # Chama a função que imprime o gabarito do tabuleiro perdedor
    tabuleiro.mostra_gabarito(tab_perdedor)

    # Para o programa por 5 segundos para garantir mais tempo de visualização da mensagem e depois chama a função que limpa o terminal de execução
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')


def jogo(nome_jogador1, nome_jogador2, tabuleiro_jogador1, tabuleiro_jogador2):
    '''
    Função que executa as jogadas de ataque dos dois jogadores em série

    Recebe o nome dos jogadores e seus tabuleiros

    Desenvolvido por Pablo Eztrela, comentado por Juan Leite
    '''

    # Imprime uma mensagem que indica o início da série de ataques
    print('Hora de jogar!')

    # Cria um laço infinito
    while(True):

        # Chama a função que executa o comando de ataque do jogador 1
        dizimado = jogada_ataque(
            nome_jogador1, tabuleiro_jogador1, tabuleiro_jogador2)

        # Chama a função que limpa o terminal de execução
        os.system('cls' if os.name == 'nt' else 'clear')

        # Chama a função que verifica se há vitória do jogador 1
        if(dizimado):

            # Chama a função que imprime a mensagem final do jogo
            mensagem_final(nome_jogador1, nome_jogador2,
                           tabuleiro_jogador1, tabuleiro_jogador2)

            # Encerra o laço, pois o jogador 1 venceu o jogo
            break

        # Chama a função que executa o comando de ataque do jogador 2
        dizimado = jogada_ataque(
            nome_jogador2, tabuleiro_jogador2, tabuleiro_jogador1)

        # Chama a função que limpa o terminal de execução
        os.system('cls' if os.name == 'nt' else 'clear')

        # Chama a função que verifica se há vitória do jogador 2
        if(dizimado):

            # Chama a função que imprime a mensagem final do jogo
            mensagem_final(nome_jogador2, nome_jogador1,
                           tabuleiro_jogador2, tabuleiro_jogador1)

            # Encerra o laço, pois o jogador 2 venceu o jogo
            break


def verifica_vitoria(tabuleiro):
    """
     Verifica se ainda existem navios a serem localizados no tabuleiro

     Recebe o tabuleiro a ser verificado

     Retorna True(caso todos os navios tenham sido apontados pelo oponente) ou False(caso ainda existam navios a serem atacados)

     Desenvolvido por Matheus Pereira, comentado por Juan Leite
    """

    # Varre o tabuleiro
    for linhas in tabuleiro:

        # Se achar "N" (ou seja, um navio não encontrado pelo adversário), o jogo deve continuar
        if ('N' in linhas):
            return False

    # Se o for não encontrar um navio, a função retorna True, isto é, um jogador venceu a partida
    return True
