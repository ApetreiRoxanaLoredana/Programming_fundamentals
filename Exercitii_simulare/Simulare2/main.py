from validator_bucycle import Validator_bike
from repository_bicycle import Repository_bike
from controller_bicycle import Controller_bike
from ui import UI

val_bike = Validator_bike()
repo_bike = Repository_bike()
contr_bike = Controller_bike(repo_bike, val_bike)
consola = UI(contr_bike)
consola.run()