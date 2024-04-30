from models import Project
import jsonpickle as json
import sqlite3
import pickle


class Data:
    projects = []

    def __init__(self, projects=[]):
        self.projects = projects


class JSONDatabase:
    def __init__(self):
        self.projects = []
        self.read()

    def read(self):
        with open("database.json", "r") as file:
            self.projects = json.decode(file.read()).projects
        return self.projects

    def write(self):
        with open("database.json", "w") as file:
            file.write(json.encode(Data(self.projects)))

    def add(self, project):
        self.projects.append(project)
        self.write()


class SQLDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS projects (
            name text NOT NULL,
            description text,
            authors text NOT NULL,
            source text
        )"""
        )
        self.write()
        self.read()

    def __del__(self):
        self.connection.close()

    def read(self):
        self.projects = []
        self.cursor.execute("SELECT * FROM projects")
        for data in self.cursor.fetchall():
            name = data[0]
            description = data[1]
            authors = pickle.loads(data[2])
            source = data[3]
            project = Project(name, description, authors, source)
            self.projects.append(project)
        return self.projects

    def write(self):
        self.connection.commit()

    def add(self, project):
        self.projects.append(project)
        data = (
            project.name,
            project.description,
            pickle.dumps(project.authors),
            project.source,
        )
        self.cursor.execute("INSERT INTO projects VALUES (?, ?, ?, ?)", data)
        self.write()


class ProjectDatabase:
    def __init__(self):
        # self.database = JSONDatabase()
        self.database = SQLDatabase()

    def read(self):
        return self.database.read()

    def write(self):
        self.database.write()

    def add(self, project):
        self.database.add(project)


database = ProjectDatabase()
