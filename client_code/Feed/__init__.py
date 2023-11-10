from ._anvil_designer import FeedTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Feed(FeedTemplate):

  feed_pic = {}
  
  def __init__(self, **properties):
    self.load_feed()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def load_feed(self):
    user = anvil.users.get_user()
    if user:
      email = user ["email"]
    else:
      email = "default"
    self.feed_pic['image_1'] = anvil.server.call('get_feed', email)
