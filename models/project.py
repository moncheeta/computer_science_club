class Project:
    name = ""
    description = ""
    authors = []
    source = None

    def __init__(self, name, description, authors, source=None):
        self.name = name
        self.description = description
        self.authors = authors
        self.source = source
