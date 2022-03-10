class Controller_Bicicleta:
    """
    Entitate abstracta de tipul Controller_Bicicleta
    """
    def __init__(self, repo_bici):
        self.__repo = repo_bici

    def sterge_tip(self, tip):
        """
        Sterge din fisier toate bicicletele care au acest tip
        :param tip:string
        :return: None
        """
        list = self.__repo.get_all()
        for i in list:
            if i.get_tip() == tip:
                self.__repo.delete(i.get_id())

    def sterge_max(self):
        """
        Sterge din fiser toate bicicletele care au pretul maxim
        :return:
        """
        maxim = -1
        list = self.__repo.get_all()
        for i in list:
            if i.get_pret() > maxim:
                maxim = i.get_pret()

        for i in list:
            if i.get_pret() == maxim:
                self.__repo.delete(i.get_id())
