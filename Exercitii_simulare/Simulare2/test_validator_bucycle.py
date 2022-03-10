from unittest import TestCase
from domain_bicycle import Bicycle
from errors import ValidatorException, RepoException
from validator_bucycle import Validator_bike

class TestValidator_bike(TestCase):
    def setUp(self):
        self.__val = Validator_bike()

    def test_valideaza(self):
        bike = Bicycle("", "", "")
        self.assertRaisesRegex(ValidatorException, "Codul nu poate fi vid!\n"
                                               "Tipul nu poate fi vid!\n"
                                               "Pretul nu poate fi vid!\n", self.__val.valideaza, bike)