import os
from jsonpickle import decode, encode


class Data:
    projects = []

    def __init__(self, projects):
        self.projects = projects


class Database:
    def read(self):
        if not os.path.isfile("database.json"):
            return Data([])
        with open("database.json", "r") as file:
            return decode(file.read())

    def write(self, data):
        with open("database.json", "w") as file:
            file.write(encode(data))


class ProjectDatabase:
    def read(self):
        projects = []
        for project in Database().read().projects:
            projects.append(project)
        return projects

    def write(self, projects):
        Database().write(Data(projects))
