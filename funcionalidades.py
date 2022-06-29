import os, animations


def imprime_menu_principal():
    animations.loading(0.1)
    os.system('clear')
    print(f'Escolha entre as opções a seguir:\n')
    print(f'Novo Jogo       -> 1')
    print(f'Encerrar        -> 2')
    opcao = int(input(f'\nDigite opção desejada: '))
    os.system('clear')
    return opcao