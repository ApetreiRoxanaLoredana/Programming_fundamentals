from domain import Jucator


class JucatoriController:
    def __init__(self, repo, val):
        """
        :param repo: JucatoriRepo
        :param val: JucatorValidator
        """
        self.__repo = repo
        self.__val = val

    def adauga_jucator(self, nume, prenume, inaltime, post):
        """
        Adauga un jucator nou
        Arunca ValidatorException daca jucatorul nu e conform
        :param nume:string
        :param prenume:string
        :param inaltime:int
        :param post:string
        :return:None
        """
        jucator = Jucator(nume, prenume, inaltime, post)
        self.__val.valideaza(jucator)
        self.__repo.add(jucator)

    def modifica_jucator(self, nume, prenume, inaltime):
        """
        Modifica inaltimea jucatorului cu numele si prenumele respectiv
        Arunca ValidatorException daca jucatorul nu e conform
        Arunca RepoException daca nu exista jucatorul
        :param nume: string
        :param prenume: string
        :param inaltime: int
        :return: None
        """
        jucator = Jucator(nume, prenume, inaltime, "Pivot")
        self.__val.valideaza(jucator)
        self.__repo.modifica(jucator)

    def get_echipa(self):
        """
        Formeaza o echipa formata din 2 Fundasi, 2 Extreme si un Pivot
        Cu cele mai mari inaltimi
        :return:
        """
        list = self.__repo.get_all()
        max1_fundas = max2_fundas = max1_extrema = max2_extrema = pivot = -1
        poz1_fundas = poz2_fundas = poz1_extrema = poz_pivot = 0
        for i in range(len(list)):
            if list[i].get_post == "Fundas":
                if list[i].get_inaltime() > max1_extrema:
                    max1_fundas = list[i].get_inaltime()
                    poz_fundas1 = i
                    max2_fundas = max1_fundas
                else:
                    if list[i].get_inaltime() > max2_fundas:

            if list[i].get_post == "Extrema":
                if list[i].get_inaltime() > max1_extrema:
                    max1_extrema = list[i].get_inaltime()
                    poz_extrema = i
            if list[i].get_post == "Pivot":
                if list[i].get_inaltime() > max1_extrema:
                    max1_pivot = list[i].get_inaltime()
                    poz_pivot = i