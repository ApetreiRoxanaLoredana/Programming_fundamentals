class AirportController:
    def __init__(self, repo_airport):
        self.__repo = repo_airport

    def remove_flights(self, company_name):
        list = self.__repo.get_by_name(company_name)
        for i in list:
            self.__repo.detele(i.get_flight_number())

    def get_all_flights(self):
        return self.__repo.get_all()