class Project:
    name = ""
    description = ""
    authors = []
    source = None
    images = None

    def __init__(self, name, description, authors, source=None, images=None):
        self.name = name
        self.description = description
        self.authors = authors
        self.source = source
        self.images = images
