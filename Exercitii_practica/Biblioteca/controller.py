from domain import Carte, Undo


class BiblioController:
    """
    Entitate abstracta de tipul BiblioController
    """
    def __init__(self, repo, repo_undo, val, filtru):
        """
        :param repo: BiblioRepo
        :param val: ValidatorCarte
        """
        self.__repo = repo
        self.__repo_undo = repo_undo
        self.__val = val
        self.__filtru = filtru

    def adauga_carte(self, id, titlu, autor, an_aparitie):
        """
        Adauga o carte noua in biblioteca
        Arunca ValidatorException daca cartea nu e conforma
        :param id: int
        :param titlu: string
        :param autor: string
        :param an_aparitie: int
        :return: None
        """
        carte = Carte(id, titlu, autor, an_aparitie)
        self.__val.valideaza(carte)
        self.__repo.add(carte)
        self.__repo_undo.add(Undo("adaugare", [carte]))

    def modifica_carte(self, cifra, autor):
        """
        Modifica autorii cartilor care au in id cifra respectiva
        :param cifra: string
        :param autor: string
        :return: None
        """
        lista_carti_modificate = []
        list = self.__repo.load_from_file()
        for carte in list:
            id = str(carte.get_id())
            if cifra in id:
                carte_mod = Carte(carte.get_id(), carte.get_titlu(), autor, carte.get_an_aparitie())
                self.__repo.modifica(carte_mod)
                lista_carti_modificate.append(carte)
        self.__repo_undo.add(Undo("modificare", lista_carti_modificate))

    def undo(self):
        """
        Reface ultima operatie
        :return: None
        """
        element = self.__repo_undo.pop()
        lista_carti = self.__repo.load_from_file()
        if element.get_status() == "adaugare":
            list = element.get_lista_carti()
            for i in list:
                self.__repo.sterge(i)
        if element.get_status() == "modificare":
            list = element.get_lista_carti()
            for i in list:
                self.__repo.modifica(i)

    def modifica_filtru(self, text, numar):
        """
        Modifica filtrul
        :param text: string
        :param numar: int
        :return: None
        """
        self.__filtru.set_text(text)
        self.__filtru.set_numar(numar)

    def aplica_filtru(self):
        """
        :return: Returneaza lista cu cartile dupa filtru
        """
        list = self.__repo.load_from_file()
        if self.__filtru.get_text() == "" and self.__filtru.get_numar() == -1:
            return list
        new_list = []
        for carte in list:
            if self.__filtru.get_text() in carte.get_titlu():
                if carte.get_an_aparitie() < self.__filtru.get_numar():
                    new_list.append(carte)
        return new_list
