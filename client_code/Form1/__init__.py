from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.repeating_panel_1.items=app_tables.images.search()

  def file_loader_1_change(self, file, **event_args):
    for fl in self.file_loader_1.files:
      app_tables.images.add_row(image=fl)
    open_form('Form1')

