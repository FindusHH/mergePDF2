from ._anvil_designer import PDF_FormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PDF_Form(PDF_FormTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # find files which do not have a filename
    self.repeating_panel_1.items=app_tables.files.search(file_name = q.not_(None)) # __merged__.pdf
    
    # sort by sequence number ascending
    sorted_items = sorted(self.repeating_panel_1.items, key=lambda k: k['sequence'], reverse=False)
    self.repeating_panel_1.items = sorted_items

    self.link_merged.visible = False


  def file_loader_1_change(self, file, **event_args):    
    # Property MUST BE SET IN UI !!
    #self.file_loader_1.file_types = ".pdf"
    # only allow .PDF-Files
    
    for fl in self.file_loader_1.files:
      file_name = fl.name
      maximum, list_of_sequences = anvil.server.call('get_list_of_sequences_and_max_seqno')
      if maximum is None:
        # first file, assing sequence no 1
        sequence = 1
      else:
        # assign the highest sequence no
        sequence = maximum + 1
      print("sequence(UI) = " + str(sequence))
      
      # add row to table
      app_tables.files.add_row(file=fl, file_name=file_name, sequence=sequence)
      
    open_form('PDF_Form')


  
  def button_merge_pdf_click(self, **event_args):
    message = anvil.server.call('merge_PDF_Files')
    link = anvil.server.call('get_link_to_merged_PDF')
    print(link)
    self.link_merged.url= link
    #alert(message)
    self.link_merged.visible = True

  def create_link_click(self, **event_args):
    link = anvil.server.call('get_link_to_merged_PDF')
    print(link)
    self.link_merged.url= link
    #self.link_merged.visible = False
    #open_form('PDF_Form')



