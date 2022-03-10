class Flight:
    def __init__(self, flight_number, type, company_name, city):
        self.__flight_number = flight_number
        self.__type = type
        self.__company_name = company_name
        self.__city = city

    def get_flight_number(self):
        return self.__flight_number

    def get_type(self):
        return self.__type

    def get_company_name(self):
        return self.__company_name

    def get_city(self):
        return self.__city

    def __str__(self):
        return str(self.__flight_number)+" // "+self.__type+" // "+self.__company_name+"" \
                " // "+self.__city


class ValidatorException(Exception):
    pass


class Flight_Validator:
    def validate(self, flight):
        errors = ""

        if flight.get_flight_number() == "":
            errors += "Numarul zborului nu poate fi valid!\n"
        if flight.get_type() != "ARRIVAL" and flight.get_type() != "DEPARTURE":
            errors += "Tipul zborului poate fii doar ARRIVAL sau DEPARTURE!\n"
        if flight.get_company_name() == "":
            errors += "Numele companiei nu poate fi vid!\n"
        if flight.get_city() == "":
            errors += "Numele orasului nu poate fi vid!\n"

        if len(errors) > 0:
            raise ValidatorException(errors)


