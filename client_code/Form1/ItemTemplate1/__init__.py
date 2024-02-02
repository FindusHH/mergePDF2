from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    pic_name = self.item['image'].name
    self.label_1.text = pic_name

  def button_1_click(self, **event_args):
    self.item.delete()
    open_form('Form1')

