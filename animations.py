from time import sleep
from sys import stdout


def loading(intervalo):
    print("Loading:")


    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    
    # Mostra a animação em tela
    for i in range(len(animation)):
        sleep(intervalo) # Função importada da lib time para que a animação não seja mostrada toda de uma vez
        stdout.write("\r" + animation[i % len(animation)])
        stdout.flush()

    print("\n")