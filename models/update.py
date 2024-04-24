from datetime import datetime
from member import Member

class Update:
  member = Member()
  text = ""
  time = datetime.now()

  def __init__(self, member, text, time):
    self.member = member
    self.text = text
    self.time = time
