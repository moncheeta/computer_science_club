from models import Project
from database import Database, Data


class ProjectDatabase:
    def read(self):
        projects = []
        for project in Database().read()["projects"]:
            name = project.get("name")
            description = project.get("description")
            authors = project.get("authors")
            source = project.get("source")
            images = project.get("images")
            projects.append(Project(name, description, authors, source, images))
        return projects

    def write(self, projects):
        with open("database.json", "w") as file:
            file.write(encode(Data(projects)))
