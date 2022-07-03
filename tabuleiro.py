from random import randint

def cria_tabuleiro():

    #Criando a matriz que funcionará como tabuleiro

    tabuleiro = [[None] * 11 for i in range(11)]

    letras = ['A','B','C','D','E','F','G','H','I','J']

    tabuleiro[0][0] = ''

    #Preenchendo as bordas do tabuleiro com o as letras que correspondem às linhas e os números que indicam as colunas

    for i in range(1, 11):
        tabuleiro[i][0] = letras[i-1]
        
    for j in range(1, 11):
        tabuleiro[0][j] = j

    #Preenchendo o conteúdo do tabuleiro com '.', indicando seu estado inicial

    for i in range(1, 11):
        for j in range(1, 11):
            tabuleiro[i][j] = '.'           
                
    return tabuleiro


def mostra_tabuleiro(tab):
    celula_tab = '.'
    for i in range(11):
            for j in range(11):
                if i == 0 and j == 0:
                    print(f'{tab[i][j]:1}', end='')
                elif tab[i][j] == 'N':
                    print(f'{celula_tab:4}', end='')
                else:
                    print(f'{tab[i][j]:4}', end='')
            print()

def mostra_gabarito(tab):

    #Exibindo cada elemento do tabuleiro de maneira formatada

    for i in range(11):
            for j in range(11):
                if i == 0 and j == 0:
                    print(f'{tab[i][j]:1}', end='')
                else:
                    print(f'{tab[i][j]:4}', end='')
            print()


def preenche_tabuleiro(tab, num_navios):

   #Preenchendo o tabuleiro de maneira aleatória com os navios indicados pela letra 'N', sempre verificando se já existem navios ao redor da posição a ser preeenchida

    cont = 0
    while cont < num_navios:
        lin = randint(1, 10)
        col = randint(1, 10)
        if lin != 10 and col != 10:
            if tab[lin-1][col-1] != 'N' and tab[lin-1][col] != 'N' and tab[lin-1][col+1] != 'N' and tab[lin][col-1] != 'N' and tab[lin][col+1] != 'N' and tab[lin+1][col-1] != 'N' and tab[lin+1][col] != 'N' and tab[lin+1][col+1] != 'N':
                tab[lin][col] = 'N'
                cont += 1
        elif lin != 10 and col == 10:
            if tab[lin-1][col-1] != 'N' and tab[lin-1][col] != 'N' and tab[lin][col-1] != 'N' and tab[lin+1][col-1] != 'N' and tab[lin+1][col] != 'N':
                tab[lin][col] = 'N'
                cont += 1
        elif lin == 10 and col != 10:
            if tab[lin-1][col-1] != 'N' and tab[lin-1][col] != 'N' and tab[lin-1][col+1] != 'N' and tab[lin][col-1] != 'N' and tab[lin][col+1] != 'N':
                tab[lin][col] = 'N'
                cont += 1
        else:
            if tab[lin-1][col-1] != 'N' and tab[lin-1][col] != 'N' and tab[lin][col-1] != 'N':
                tab[lin][col] = 'N'
                cont += 1
    return tab


def transforma_linha(lin):
    letras = ['A','B','C','D','E','F','G','H','I','J']
    for i in range(10):
        if letras[i] == lin:
                lin = i + 1
    if lin == '0':
        lin = 0 
    return lin