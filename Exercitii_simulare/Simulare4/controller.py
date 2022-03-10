from domain import Bere


class Controller_bere:
    """
    Entitae abstracta de tipul Controller bere
    """
    def __init__(self, repo_bere):
        self.__repo = repo_bere

    def update(self, nume, procent):
        """
        Majoreaza preturile berilor care au numele respectiv cu %procent
        :param nume:
        :param procent:
        :return:
        """
        list = self.__repo.get_all()
        for i in list:
            if i.get_nume() == nume:
                pret = i.get_pret()
                pret = pret + procent/100*pret
                bere_noua = Bere(nume, i.get_tip(), pret)
                self.__repo.update(i.get_id(), bere_noua)

    def discount(self, tip):
        """
        Modifica pretul berilor de acest tip cu minimul pretului berii care are numele ei
        :param tip:
        :return:
        """
        list = self.__repo.get_all()
        for i in list:
            minim = i.get_pret()
            if i.get_tip() == tip:
                for j in list:
                    if i.get_id() != j.get_id() and j.get_nume() == i.get_nume():
                        minim = min(j.get_pret(), minim)
                bere_up = Bere(i.get_nume(), tip, minim)
                self.__repo.update(i.get_id(), bere_up)


