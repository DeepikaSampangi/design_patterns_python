from .model import Person


class personController:
    def getAllNames(self):
        return Person().getAllNames()
