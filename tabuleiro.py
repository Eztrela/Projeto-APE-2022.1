# Importa a função randint da lib random
from random import randint

def cria_tabuleiro():
    """
    Função que cria o tabuleiro e o preenche inicialmente

    Desenvolvido por Marcela Kramer, Comentado por Juan Leite

    """

    #Cria a matriz que funcionará como tabuleiro
    tabuleiro = [[None] * 11 for i in range(11)]

    # Cria um vetor preenchido com as letras que correspodem às linhas do tabuleiro
    letras = ['A','B','C','D','E','F','G','H','I','J']

    # Preenche a posição 0x0 do tabuleiro com uma string nula
    tabuleiro[0][0] = ''

    #Preenche as bordas do tabuleiro com o as letras que correspondem às linhas e os números que indicam as colunas
    for i in range(1, 11):
        tabuleiro[i][0] = letras[i-1]
        
    for j in range(1, 11):
        tabuleiro[0][j] = j

    #Preenche o conteúdo do tabuleiro com '.', indicando seu estado inicial
    for i in range(1, 11):
        for j in range(1, 11):
            tabuleiro[i][j] = '.'           
                
    return tabuleiro # Retorna o tabuleiro


def mostra_tabuleiro(tab):
    """
    Função que exibe cada elemento do tabuleiro de maneira formatada, porém substituindo, no print, as células 'N', que indicam os navios, por '.'

    Desenvolvido por Matheus Pereira, Comentado por Juan Leite

    """

    # Cria uma variável que recebe a string '.' 
    celula_tab = '.'

    # Percorre todo o tabuleiro
    for i in range(11):
            for j in range(11):

                # Verifica se a célula do tabuleiro é a que está posição 0x0 e, caso verdadeiro, imprime essa célula com uma formatação diferente das demais
                if i == 0 and j == 0:
                    print(f'{tab[i][j]:1}', end='')

                # Verifica se a célula do tabuleiro é igual a 'N', o que indica a presença de um navio, e, caso verdadeiro, imprime um '.' 
                elif tab[i][j] == 'N':
                    print(f'{celula_tab:4}', end='')

                # Imprime a célula do tabuleiro com uma formatação padrão, a fim de manter o formato regular de matriz
                else:
                    print(f'{tab[i][j]:4}', end='')
            print()

def mostra_gabarito(tab):
    """
    Função que exibe cada elemento do tabuleiro de maneira formatada e no seu verdadeiro estado atual

    Desenvolvido por Pablo Eztrela, Comentado por Juan Leite

    """

    # Percorre todo o tabuleiro
    for i in range(11):
            for j in range(11):

                # Verifica se a célula do tabuleiro é a que está posição 0x0 e, caso verdadeiro, imprime essa célula com uma formatação diferente das demais
                if i == 0 and j == 0:
                    print(f'{tab[i][j]:1}', end='')

                # Imprime a célula do tabuleiro com uma formatação padrão, a fim de manter o formato regular de matriz
                else:
                    print(f'{tab[i][j]:4}', end='')
            print()


def preenche_tabuleiro(tab, num_navios):
    """
    Função que preenche o tabuleiro de maneira aleatória com os navios indicados pela letra 'N', sempre verificando se já existem navios ao redor da posição a ser preeenchida

    Recebe o tabuleiro a ser preenchido e a quantidade de navios que ele deve possuir

    Retorna o tabuleiro preenchido com esse determinado número de navios

    Desenvolvido por Marcela Kramer, Comentado por Matheus Pereira

    """

    # Cria uma váriavel que será utilizada como contador
    cont = 0

    # Verifica se o contador é menor que a quantidade de navios que o tabuleiro deve possuir
    while cont < num_navios:

        # Utiliza a função 'randint' da lib random para escolher uma linha e uma coluna aleatoriamente
        lin = randint(1, 10)
        col = randint(1, 10)

        # Verifica se a linha e a coluna são diferentes de 10, isto é, não estão nos limites do tabuleiro
        if lin != 10 and col != 10:

            # Verifica se não existem células 'N', isto é, navios, em alguma posição adjacente ou diagonal à posição escolhida
            if tab[lin-1][col-1] != 'N' and tab[lin-1][col] != 'N' and tab[lin-1][col+1] != 'N' and tab[lin][col-1] != 'N' and tab[lin][col+1] != 'N' and tab[lin+1][col-1] != 'N' and tab[lin+1][col] != 'N' and tab[lin+1][col+1] != 'N':

                # Caso verdadeiro, preenche a posição com 'N' para indicar a presença de um navio
                tab[lin][col] = 'N'

                # Incrementa +1 ao contador
                cont += 1

        # Verifica se a linha é diferente de 10 e a coluna é igual a 10, ou seja, se essa posição está no limite das colunas do tabuleiro
        elif lin != 10 and col == 10:

            # Verifica se não existem células 'N', isto é, navios, em alguma posição adjacente ou diagonal à posição escolhida
            if tab[lin-1][col-1] != 'N' and tab[lin-1][col] != 'N' and tab[lin][col-1] != 'N' and tab[lin+1][col-1] != 'N' and tab[lin+1][col] != 'N':

                # Caso verdadeiro, preenche a posição com 'N' para indicar a presença de um navio
                tab[lin][col] = 'N'

                # Incrementa +1 ao contador
                cont += 1

        # Verifica se a linha é igual a 10 e a coluna é diferente de 10, ou seja, se essa posição está no limite das linhas do tabuleiro
        elif lin == 10 and col != 10:

            # Verifica se não existem células 'N', isto é, navios, em alguma posição adjacente ou diagonal à posição escolhida
            if tab[lin-1][col-1] != 'N' and tab[lin-1][col] != 'N' and tab[lin-1][col+1] != 'N' and tab[lin][col-1] != 'N' and tab[lin][col+1] != 'N':

                # Caso verdadeiro, preenche a posição com 'N' para indicar a presença de um navio
                tab[lin][col] = 'N'

                # Incrementa +1 ao contador
                cont += 1


        else: # A linha e a coluna são iguais a 10, o que indica que a posição está no limite das linhas e das colunas do tabuleiro

            # Verifica se não existem células 'N', isto é, navios, em alguma posição adjacente ou diagonal à posição escolhida
            if tab[lin-1][col-1] != 'N' and tab[lin-1][col] != 'N' and tab[lin][col-1] != 'N':

                # Caso verdadeiro, preenche a posição com 'N' para indicar a presença de um navio
                tab[lin][col] = 'N'

                # Incrementa +1 ao contador
                cont += 1

    return tab # Retorna o tabuleiro devidamente preenchido com os navios


def transforma_linha(lin):
    """
    Função que transforma uma letra(str) em um inteiro que corresponderá a uma posição de linha na matriz

    Recebe uma determinada letra em formato string

    Retorna um valor inteiro que corresponde à posição dessa letra

    Desenvolvido por Matheus Pereira, Comentado por Marcela Kramer

    """
    # Cria um vetor com letras de 'A' a 'J'
    letras = ['A','B','C','D','E','F','G','H','I','J']
 
    # Percorre todas as posições desse vetor e verifica se alguma delas é igual a variável 'lin', que foi o parâmetro recebido pela função
    for i in range(10):
        if letras[i] == lin:

                # Caso True, 'lin' recebe o valor do índice da posição no vetor + 1 
                lin = i + 1

        # Caso False, é verificado ser 'lin' é igual a '0' e, se verdadeiro, 'lin' recebe o valor inteiro 0        
        elif lin == '0':
            lin = 0 
            
    return lin # Retorna o valor inteiro 