# Importa as funções das bibliotecas que são utilizadas no código
from time import sleep
from sys import stdout
import os


def loading(intervalo):
    """
    Função que cria a animação de loading e a imprime na tela

    Recebe o tempo de execução da animação

    Desenvolvido por Pablo Eztrela, Comentado por Matheus Pereira

    """
    print("Loading:")

    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                 "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    # Mostra a animação em tela
    for i in range(len(animation)):
        # Função importada da lib time para que a animação não seja mostrada toda de uma vez
        sleep(intervalo)
        stdout.write("\r" + animation[i % len(animation)])
        stdout.flush()

    print("\n")