from ArvoreDeDecisao import ArvoreDeDecisao

class Jogo():
    def __init__(self) -> None:
        self.arvore = ArvoreDeDecisao()
        self.inicializa()

    def inicializa(self):
        self.arvore.insere("baleia")

    def interage(self, tipo: str):
        print("\npense em um " + tipo)
        resposta = self.chuta(self.decide_um_chute())

    def decide_um_chute(self):
        return "baleia"

    def chuta(self, chute: str):
        resposta = input("voce pensou em " + chute + "?\n>>")
        if resposta.lower() == "s":
            self.recomeca()
        elif resposta.lower() == "n":
            pass
        else:
            self.chuta(chute)

    def recomeca(self):
        print("\nAKINATOR!\n------------\n")
        self.comeca()

    def comeca(self):
        self.interage("animal")

j = Jogo()
j.comeca()