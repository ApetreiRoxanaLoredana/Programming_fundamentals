from controller import AirportController
from domain import Flight_Validator
from repository import AirportRepository
from ui import Console

validator_flight = Flight_Validator()
repo_airport = AirportRepository(validator_flight)
contr_airport = AirportController(repo_airport)
consola = Console(contr_airport)
consola.run()