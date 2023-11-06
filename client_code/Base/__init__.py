from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from ..MyPosts import MyPosts
from ..Feed import Feed


class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.change_sign_in_text()

    # Any code you write here will run before the form opens.

  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      email = user ["email"]
      self.sign_in.text = email
    else:
      self.sign_in.text = "Sign In"
  
  def view_posts_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(MyPosts())

  def home_page_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Base())

  def sign_in_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user:
      logout = confirm("Would you like to logout?")
      if logout:
        anvil.users.logout()
        self.content_panel.clear()
        self.content_panel.add_component(Base())
    else:
      anvil.users.login_with_form()
      self.change_sign_in_text()

  def feed_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Feed())

  def title_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass


