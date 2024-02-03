from ._anvil_designer import PDF_FormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PDF_Form(PDF_FormTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    #self.repeating_panel_1.items=app_tables.files.search()
    self.repeating_panel_1.items=app_tables.files.search(file_name = q.not_(None)) # __merged__.pdf

    sorted_items = sorted(self.repeating_panel_1.items, key=lambda k: k['sequence'], reverse=False)
    self.repeating_panel_1.items = sorted_items


  def file_loader_1_change(self, file, **event_args):
    for fl in self.file_loader_1.files:
      file_name = fl.name
      # TO DO
      # retrieve highest sequence number
      # assigne highest sequence number to new uploaded file
      app_tables.files.add_row(file=fl, file_name=file_name)
    open_form('PDF_Form')

  def button_1_click(self, **event_args):
    anvil.server.call('merge_PDF_Files')

  def create_link_click(self, **event_args):
    link = anvil.server.call('get_link_to_merged_PDF')
    print(link)
    self.link_merged.url= link



