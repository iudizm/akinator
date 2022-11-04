
class NoPergunta():
    def __init__(self, pergunta:  str) -> None:
        self.__pergunta = pergunta
        self.__resposta_sim = None
        self.__resposta_nao = None

    def pergunta(self):
        return self.__peprgunta

    def resposta_sim(self):
        return self.__resposta_sim

    def resposta_nao(self):
        return self.__resposta_nao
