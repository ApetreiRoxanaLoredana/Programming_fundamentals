class Controller_Coffee:
    """
    Entiate abstraca de tipul Controller_Coffee
    """
    def __init__(self, repo_coffee):
        self.__repo = repo_coffee

    def filtreaza(self, tara, pret):
        """
        :param tara:
        :param pret:
        :return: lista cafelelor care provin din tara respecctiva si au pretul mai mic
        decat parametrul pret
        """
        list = self.__repo.get_all()
        list_rez = []
        for i in list:
            if i.get_tara() == tara and i.get_pret() < pret:
                list_rez.append(i)
        return list_rez

    def sortare(self):
        """
        Sorteaza cafelele alfabeti dupa tara de origine si in candrul tarii, descrescator
        dupa pret
        :return: lista cafelelor sortata
        """
        list = self.__repo.get_all()
        list = sorted(list, key = lambda coffee: coffee.get_pret(), reverse=True)
        list = sorted(list, key = lambda coffee: coffee.get_tara())

        return list