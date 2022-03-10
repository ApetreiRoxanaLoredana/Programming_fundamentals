from console import AgendaUI
from controller import AgendaController
from repository import ContactRepository
from validator import ContactValidator

repo_agenda = ContactRepository("Contacte.txt")
val_agenda = ContactValidator()
contr_agenda = AgendaController(repo_agenda, val_agenda)
consola = AgendaUI(contr_agenda)
consola.run()