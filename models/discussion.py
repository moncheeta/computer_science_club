from config import DOMAIN


class Discussion:
    name = ""
    description = ""
    link = f"{DOMAIN}/discussion/"

    def __init__(self, id, name, description):
        self.link += str(id)
        self.name = name
        self.description = description


from datetime import datetime
from config import DOMAIN


class Event:
    name = ""
    description = ""
    start = datetime.now()
    end = None
    differentDay = False
    link = f"{DOMAIN}/event/"

    def __init__(self, id, name, description, start, end):
        self.link += str(id)
        self.name = name
        self.description = description
        self.start = start
        self.end = end
        if (
            end
            and self.end.year >= self.start.year
            and self.end.month >= self.start.month
            and self.end.day > start.day
        ):
            differentDay = True
