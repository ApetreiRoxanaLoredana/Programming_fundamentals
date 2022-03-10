class Contact:
    """
    Entitate abstracta de tipul Contact
    """
    def __init__(self, id, name, phoneNr, group):
        self.__id = id
        self.__name = name
        self.__phoneNr = phoneNr
        self.__group = group

    def get_id(self):
        """
        :return: id - int
        """
        return self.__id

    def get_name(self):
        """
        :return: name - string
        """
        return self.__name

    def get_phoneNr(self):
        """
        :return: phoneNr - string
        """
        return self.__phoneNr

    def get_group(self):
        """
        :return: group - string
        """
        return self.__group

    def __str__(self):
        """
        :return: un string ce contine informatiile despre un contact
        """
        return str(self.__id)+" "+self.__name+" "+self.__phoneNr+" "+self.__group

    def __eq__(self, other):
        return self.__id == other.__id
