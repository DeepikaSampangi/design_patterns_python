import json

class Person:
    def __init__(self, firstname:str = None, lastName:str = None):
        self.firstName = firstname
        self.lastName = lastName

    def personName(self):
        return self.firstName + self.lastName

    def getAllNames(self):
        nameFile = open('names.txt', 'r')
        return json.loads(nameFile.read())
        