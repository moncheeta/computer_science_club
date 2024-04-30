import os
from datetime import datetime
from config import DOMAIN, GROUP_ID
from models import Group, Event, Update, Discussion, Member
from database import database
from schoolopy import Schoology, Auth


class SchoologyAPI:
    api = None
    auth = Auth(
        os.environ["SCHOOLOGY_API_KEY"],
        os.environ["SCHOOLOGY_API_SECRET"],
        domain=DOMAIN,
    )

    def __init__(self):
        self.api = Schoology(self.auth)
        self.api.limit = 64

    def name(self):
        return self.api.get_group(GROUP_ID).title

    def description(self):
        return self.api.get_group(GROUP_ID).description

    def events(self):
        events = []
        for event in self.api.get_group_events(GROUP_ID):
            start = datetime.strptime(event.start, "%Y-%m-%d %H:%M:%S")
            end = None
            if event.has_end:
                end = datetime.strptime(event.end, "%Y-%m-%d %H:%M:%S")
            event = Event(event.id, event.title, event.description, start, end)
            events.append(event)
        return events

    def updates(self):
        updates = []
        for update in self.api.get_group_updates(GROUP_ID):
            user = self.api.get_user(update.uid)
            member = Member(user.name_display)
            # time = datetime.utcfromtimestamp(int(update.created))
            time = datetime.utcfromtimestamp(int(update.last_updated))
            updates.append(Update(member, update.body, time))
        return updates

    def discussions(self):
        discussions = []
        for discussion in self.api.get_group_discussions(GROUP_ID):
            discussions.append(
                Discussion(discussion.id, discussion.title, discussion.body)
            )
        return discussions

    def members(self):
        members = []
        for enrolled in self.api.get_group_enrollments(GROUP_ID):
            member = Member(enrolled.name_display)
            if enrolled.admin == 1:
                member.leader = True
            members.append(member)
        return members

    def group(self):
        name = self.name()
        description = self.description()
        events = self.events()
        updates = self.updates()
        discussions = self.discussions()
        projects = database.read()
        members = self.members()
        return Group(name, description, events, updates, discussions, projects, members)


api = SchoologyAPI()
group = api.group()
