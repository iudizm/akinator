from No import No

class Akinator():
    def __init__(self, tipo: str = "animal") -> None:
        self.__raiz = No("baleia", True)
        self.tipo = tipo

    def percorre(self):
        self._percorre(self.__raiz)

    def _percorre(self, raiz):
        if raiz.ehFolha:
            if not self.chuta(raiz):
                self.aprende_com_erro(raiz)
            self.menu()
        else:
            if self.pergunta(raiz):
                self._percorre(raiz.get_sim())
            else:
                self._percorre(raiz.get_nao())

    def chuta(self, no):
        resposta = input("\nVocê pensou em " + str(no) + "?\n(S/N)>>")
        if resposta.lower() == "s":
            print("\nAKINATOR!\n------------\n\n")
            return True
        elif resposta.lower() == "n":
            return False
        else:
            self.chuta(no)

    def pergunta(self, no):
        resposta = input(
            "O " + self.tipo + " que você pensou possui a característica '" +
            str(no) + "'? \n(S/N)>>"
        )
        if resposta.lower() == "s":
            return True
        elif resposta.lower() == "n":
            return False
        else:
            self.pergunta(no)

    def aprende_com_erro(self, no_chutado):
        print("\n😢Poxa que pena, me ajude a melhorar:\n")
        resposta_certa = input(
            "Em que " + self.tipo + " voce tinha pensado?\n>>")
        diferenca = input(
            "\nEntendi, e qual a principal característica de um(a) " + resposta_certa +
            " que o(a) diferencia de um(a) " + str(no_chutado) + "?\n>>"
        )
        self.registra_aprendizado(no_chutado, resposta_certa, diferenca)
        print("\nObrigado!\n")

    def registra_aprendizado(self, no_chutado, resposta_certa, diferenca):
        nova_caracteristica = No(diferenca)
        nova_folha = No(resposta_certa, True)
        
        nova_folha.pai = nova_caracteristica
        nova_folha.ehPositivo = True
        
        nova_caracteristica.pai = no_chutado.pai
        nova_caracteristica.set_sim(nova_folha)
        nova_caracteristica.set_nao(no_chutado)
        
        if self.__raiz == no_chutado:
            self.__raiz = nova_caracteristica
        elif no_chutado.ehPositivo:
            no_chutado.pai.set_sim(nova_caracteristica)
        else:
            no_chutado.pai.set_nao(nova_caracteristica)
        no_chutado.pai = nova_caracteristica
        no_chutado.ehPositivo = False

    def menu(self):
        r = input(
            "O QUE DESEJAS FAZER AGORA?\n(1)-Jogar Novamente\n(2)-Sair\n\n>>"
        )
        if r == "1":
            self.main()
        elif r == "2":
            exit
        else:
            self.menu()

    def main(self):
        print("\npense em um " + self.tipo)
        self.percorre()

a = Akinator()
a.main()
