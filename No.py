class No():
    def __init__(self, info: str, ehFolha: bool = False) -> None:
        self._nao = None
        self._sim = None
        self._info = info
        self.ehFolha = ehFolha
        self.pai = None
        self.ehPositivo = None

    def set_nao(self, filho):
        self._nao = filho

    def set_sim(self, filho):
        self._sim = filho

    def get_nao(self):
        return self._nao

    def get_sim(self):
        return self._sim

    def __str__(self) -> str:
        return str(self._info)
