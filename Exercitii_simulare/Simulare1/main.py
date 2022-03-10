from validator_trip  import Validator_trip
from repository_trip import Repository_trip
from cotroller_trip import Controller_trip
from ui_trip import UI


val_trip = Validator_trip
repo_trip = Repository_trip()
contr_trip = Controller_trip(repo_trip, val_trip)
consola = UI(contr_trip)
consola.run()
