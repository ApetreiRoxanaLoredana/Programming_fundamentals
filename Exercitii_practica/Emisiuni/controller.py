import random

from domain import Emisiune
from errors import ControllerException


class EmisiuneController:
    """
    Entitate abstracat de tipul EmisiuneController
    """
    def __init__(self, repo, repo_blocate):
        self.__repo = repo
        self.__repo_bloc  = repo_blocate

    def genereaza_program(self, ora_inceput, ora_final):
        """
        Genereaza random un program Tv
        :param ora_inceput: int
        :param ora_final: int
        :return: o lista cu programul generat
        """
        lista_emisiuni = self.__repo.loadFromFile()
        lista_program = []

        while ora_inceput <= ora_final:
            durata = random.randint(ora_inceput, ora_final)
            durata = durata - ora_inceput

            for i in lista_emisiuni:
                if i.get_durata() == durata:
                    print(durata)
                    lista_program.append(i)
                    lista_program[-1].set_durata(ora_inceput)
                    ora_inceput += durata
        return lista_program

    def sterge_emisiune(self, nume, tip):
        """
        Sterge emisiunea care are numele si tipul respectiv
        Daca nu exista arunca RepoException
        :param nume: string
        :param tip: string
        :return: None
        """
        lista_emisiuni_blocate = self.__repo_bloc.get_all()
        if tip in lista_emisiuni_blocate:
            raise ControllerException("Aceasta emisiune e blocata\n")
        self.__repo.sterge(nume, tip)

    def modifica_emisiune(self, nume, tip, durata, descriere):
        """
        Modifica descrierea si durata emisiunii cu numele si tipul rspectiv
        Arunca RepoException daca nu exista emisiunea
        :param nume: string
        :param tip: string
        :param durata: int
        :param descriere: string
        :return: None
        """
        lista_emisiuni_blocate = self.__repo_bloc.get_all()
        if tip in lista_emisiuni_blocate:
            raise ControllerException("Aceasta emisiune e blocata\n")
        emisiune = Emisiune(nume, tip, durata, descriere)
        self.__repo.modifica(emisiune)

    def adauga_bloc(self, tip):
        """
        Adauga un tip de emisiune in lista de blocate
        :param tip: string
        :return: None
        """
        self.__repo_bloc.adauga(tip)

    def sterge_bloc(self, tip):
        """
        Sterge un tip de emisiune de lista de blocate
        :param tip: string
        :return: None
        """
        self.__repo_bloc.sterge(tip)

    def reseteaza_bloc(self):
        """
        Reseteaza lista de tipuri de emisiuni blocate
        :return: None
        """
        self.__repo_bloc.reseteaza()

