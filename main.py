import pickle
import os
from Akinator import Akinator


pickle_file_name = "arvoreAkinator.pkl"

def menu(jogo):
    r = input(
        "O QUE DESEJAS FAZER AGORA?\n"
        + "(1)-Jogar Novamente\n"
        + "(2)-Salvar estado da árvore\n"
        + "(3)-Descartar aprendizado\n"
        + "(4)-Sair\n\n>>"
    )
    if r == "1":
        main()
    elif r == "2":
        with open(pickle_file_name, "wb") as arquivo:
            pickle.dump(jogo, arquivo)
        print("Salvo com sucesso.\n")
        menu(jogo)
    elif r == "3":
        if os.path.exists(pickle_file_name):
            os.remove(pickle_file_name)
        menu(jogo)
    elif r == "4":
        exit
    else:
        print("\nEscolha uma opção digitando o número\n")
        menu(jogo)


def main():
    if os.path.exists(pickle_file_name):
        with open(pickle_file_name, "rb") as arquivo:
            jogo = pickle.load(arquivo)
    else:
        jogo = Akinator()
    jogo.main()
    menu(jogo)

main()