from Ui import JucatoriUi
from controller import JucatoriController
from domain import JucatorValidator
from repository import JucatoriRepo

val = JucatorValidator()
repo = JucatoriRepo("jucatori.txt")
contr = JucatoriController(repo, val)
consola = JucatoriUi(contr)
consola.run()