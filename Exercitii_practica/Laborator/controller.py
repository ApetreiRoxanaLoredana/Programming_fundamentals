from domain import Laborator
from errors import ContrException, RepoException


class Controller:
    def __init__(self, repo_st, repo_lab):
        """
        :param repo_st: StudentRepo
        :param repo_lab: LaboratorRepo
        """
        self.__repo_st = repo_st
        self.__repo_lab = repo_lab

    def get_all_st(self):
        """
        :return: returneaza lista cu toti studentii
        """
        return self.__repo_st.get_all()

    def cauta_student(self, id):
        """
        Cauta studentul cu id-ul respectiv
        Arunca RepoException daca nu il gaseste
        :param id: int
        :return: Student
        """
        return self.__repo_st.cauta(id)

    def adauga_laborator(self, id_st, lab_nr, nr_problemei):
        """
        Adauga in lista de laboratoare un laborator nou
        Arunca RepoException daca exista deja un laborator cu id_st si lab_nr
        :param id_st: int
        :param lab_nr: int
        :param nr_problemei: string
        :return: None
        """
        self.__repo_lab.add(Laborator(id_st, lab_nr, nr_problemei))

    def get_laboratoare_st(self, id):
        """
        Arunca ContrException daca studentul cu id respectiv
        nu are nici un laborator
        :param id: int
        :return: lista cu toate laboratoarele studentului cu id ul respectiv
        """
        rez = []
        list_lab = self.__repo_lab.get_all()
        for lab in list_lab:
            if lab.get_id_st() == id:
                rez.append(lab)
        if len(rez) == 0:
            raise ContrException("Acest student nu are nici un laborator\n")
        return rez

    def get_studenti_nr_lab(self, lab_nr):
        """
        Arunca ContrException daca nici un student nu are o problema la
        laboratorul cu nr_lab
        :param lab_nr: int
        :return: O lista cu toti studentii care au cate o problema la
        laboratorul cu nr_lab
        """
        rez = []
        list_lab = self.__repo_lab.get_all()
        for lab in list_lab:
            if lab.get_lab_nr() == lab_nr:
                try:
                    st = self.__repo_st.cauta(lab.get_id_st())
                    for student in rez:
                        if student.get_id() == st.get_id():
                            raise RepoException
                    rez.append(st)
                except RepoException:
                    continue
        if len(rez) == 0:
            raise ContrException("Nici un student nu are o problema la acest laborator\n")
        return rez