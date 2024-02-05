from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    # show filename
    pic_name = self.item['file'].name
    self.label_filename.text = pic_name
    
    # show sequence number
    seqno = self.item['sequence']
    self.label_seqno.text = seqno

  def button_delete_click(self, **event_args):
    self.item.delete()
    open_form('PDF_Form')

  def button_up_click(self, **event_args):
    """This method is called when the button is clicked"""
    seqno = self.label_seqno.text
    alert(seqno)
    

