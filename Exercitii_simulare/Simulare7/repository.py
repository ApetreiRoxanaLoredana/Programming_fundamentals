from domain import Flight


class RepoException(Exception):
    pass


class AirportRepository:
    def __init__(self, validator_flight):
        self.__list = [Flight(1200,"ARRIVAL","Blue Air","London"),
                       Flight(1300,"DEPARTURE","Tarom","Vienna"),
                       Flight(2199,"DEPARTURE","Blue Air","Barcelona")]
        self.__val = validator_flight

    def get_by_name(self, company_name):
        self.__val.validate(Flight(12, "ARRIVAL", company_name, "Londra"))
        rez = []
        for i in self.__list:
            if i.get_company_name() == company_name:
                rez.append(i)
        if len(rez) == 0:
            raise RepoException("Nu exista nici o companie cu acest nume!\n")
        return rez

    def detele(self, flight_number):
        poz = -1
        for i in self.__list:
            if i.get_flight_number() == flight_number:
                poz = self.__list.index(i)
                break
        if poz != -1:
            del self.__list[poz]
        else:
            raise RepoException("Nu exista nici un zbor cu numarul acesta!\n")

    def get_all(self):
        return self.__list

