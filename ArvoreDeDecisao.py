from NoCoisa import NoCoisa

class ArvoreDeDecisao():
    def __init__(self):
        self.__raiz = None

    def insere(self, info):
        novo_no = NoCoisa(info)
        if self.__raiz == None:
            self.__raiz = novo_no
        else:
            self.__insere(novo_no, self.__raiz)
            
    def __insere(self, novo, raiz):
        if novo.info() < raiz.info():
            if raiz.esq() == None:
                raiz.set_esq(novo)
            else:
                self.__insere(novo, raiz.esq())
        elif novo.info() < raiz.info():
            if raiz.dir() == None:
                raiz.set_dir(novo)
            else:
                self.__insere(novo, raiz.dir())

    def remove(self, info):
        pass
    
    def esvazia(self):
        self.__raiz = None

    def busca(self, info):
        pass

    def caminho_in_order(self, raiz):
        pass

    def caminho_pre_order(self, parameter_list):
        pass

    def caminho_pos_order(self, parameter_list):
        pass

