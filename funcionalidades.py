import os, animations, tabuleiro


def imprime_menu_principal():
    animations.loading(0.1)
    os.system('clear')
    print(f'Escolha entre as opções a seguir:\n')
    print(f'Novo Jogo       -> 1')
    print(f'Encerrar        -> 2')
    opcao = int(input(f'\nDigite opção desejada: '))
    os.system('clear')
    return opcao

def jogada(jogador, tab_oponente):
    print(f'\nVez de {jogador}.\n')
    while True:
        lin = input('Escolha a linha de ataque (A-J): ').upper().strip()
        col = int(input('\nEscolha a coluna de ataque (1-10): '))
        animations.loading(0.1)
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
