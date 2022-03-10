from domain import Produs


class MagazinController:
    def __init__(self, repo, val, filtru, undo):
        """
        :param repo: MagazinRepo
        :param val: PordusValidator
        """
        self.__repo = repo
        self.__val = val
        self.__filtru = filtru
        self.__undo = undo

    def adauga_produs(self, id, denumire, pret):
        """
        Adauga produsul in lista
        Arunca ValidatorException daca produsul nu e conform
        Arunca RepoException daca exista deja un produs cu acest id
        :param id: int
        :param denumire:string
        :param pret: int
        :return: None
        """
        produs = Produs(id, denumire, pret)
        self.__val.valideaza(produs)
        self.__repo.adauga(produs)

    def sterge_produse(self, cifra):
        """
        Sterge din fisier toate produsele care au cifra respectiva in id
        :param cifra: string
        :return: Numarul de produse sterse
        """
        contor = 0
        produse_sterse = []
        litsa_produse = self.__repo.get_all()
        for produs in litsa_produse:
            id = str(produs.get_id())
            if cifra in id:
                contor += 1
                produse_sterse.append(produs)
                self.__repo.sterge(produs.get_id())
        self.__undo.set_list(produse_sterse)
        return contor

    def verifica_filtru(self, produs):
        """
        Verifica daca produsul respecta filtrul actual
        :param produs: Produs
        :return: True / False
        """
        ok1 = False
        ok2 = False

        if self.__filtru.get_text() in produs.get_denumire():
            ok1 = True
        if self.__filtru.get_numar() > produs.get_pret():
            ok2 = True

        if self.__filtru.get_text() == "":
            ok1 = True
        if self.__filtru.get_numar() == -1:
            ok2 = True

        return ok1 and ok2

    def aplica_filtru(self):
        """
        Returneaza o lista cu produsele care respecta filtrul actual
        :return: lista cu produse
        """
        list = self.__repo.get_all()
        rez = []
        for produs in list:
            if self.verifica_filtru(produs):
                rez.append(produs)
        return rez

    def modifica_filtru(self, text, numar):
        """
        Modifica filtrul
        :param text: string
        :param numar: string
        :return: None
        """
        self.__filtru.set_text(text)
        self.__filtru.set_numar(numar)

    def get_filtru(self):
        """
        Returneaza filttrul
        :return: Filtru
        """
        return self.__filtru

    def undo_produse(self):
        """
        Adauga ultimele produse sterse din lista
        :return: None
        """
        list_produse = self.__undo.get_list()
        for produs in list_produse:
            self.__repo.adauga(produs)
        self.__undo.set_list([])
