from ._anvil_designer import PDF_FormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PDF_Form(PDF_FormTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.repeating_panel_1.items=app_tables.files.search()


  def file_loader_1_change(self, file, **event_args):
    for fl in self.file_loader_1.files:
      file_name = fl.name
      app_tables.files.add_row(file=fl, file_name=file_name)
    open_form('PDF_Form')

  def button_1_click(self, **event_args):
    anvil.server.call('merge_PDF_Files')

