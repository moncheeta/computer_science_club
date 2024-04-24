class Group:
	name = ""
	description = ""
	picture = "https://www.shutterstock.com/image-vector/computer-science-icon-outline-thin-600nw-1613513884.jpg"
	leaders = []
	members = []
	events = []
	updates = []
	discussions = []
	projects = []

	def __init__(self, name, description, events, updates, discussions, projects, members):
		self.name = name
		self.description = description
		self.events = events
		self.updates = updates
		self.discussions = discussions
		self.projects = projects
		for member in members:
			if member.leader:
				self.leaders.append(member)
				continue
			self.members.append(member)
			