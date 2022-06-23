def cria_tabuleiro():
    tabuleiro = [[None] * 11 for i in range(11)]

    letras = ['A','B','C','D','E','F','G','H','I','J']

    tabuleiro[0][0] = ''

    for i in range(1, 11):
        tabuleiro[i][0] = letras[i-1]
        
    for j in range(1, 11):
        tabuleiro[0][j] = j

    for i in range(1, 11):
        for j in range(1, 11):
            tabuleiro[i][j] = '.'           
                
    return tabuleiro


def mostra_tabuleiro(tab):
    for i in range(11):
            for j in range(11):
                if i == 0 and j == 0:
                    print(f'{tab[i][j]:1}', end='')
                else:
                    print(f'{tab[i][j]:4}', end='')
            print()
