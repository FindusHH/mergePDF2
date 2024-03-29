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

  def swap(self,x,y):
    temp = x
    x = y
    y = temp
    return x,y

  

  def button_delete_click(self, **event_args):
    self.item.delete()
    open_form('PDF_Form')

  def button_up_click(self, **event_args):
    seqno = int(self.label_seqno.text)
    maximum, list_of_sequences = anvil.server.call('get_list_of_sequences_and_max_seqno')
    #alert('move up: ' + str(seqno) + ' index=' + str(list_of_sequences.index(seqno)))
    a = seqno
    
    # get index of next higher value which sits one position before
    b_index = (list_of_sequences.index(seqno)-1) # '-1' for moving UP
    
    b = list_of_sequences[b_index]
    #alert(str(a) + ' ' + str(b))
    row1 = app_tables.files.get(sequence=a)
    row2 = app_tables.files.get(sequence=b)
    
    a,b = self.swap(a,b)
    #alert(str(a) + ' ' + str(b))
    row1['sequence'] = a
    row2['sequence'] = b

    open_form('PDF_Form')

   



  def button_down_click(self, **event_args):
    seqno = int(self.label_seqno.text)
    maximum, list_of_sequences = anvil.server.call('get_list_of_sequences_and_max_seqno')
    if seqno == maximum:
      alert('unterste Datei')
      self.button_down.enabled = False

    else:  
      #alert('move down: ' + str(seqno) + ' index=' + str(list_of_sequences.index(seqno)))
      a = seqno
      
      # get index of next higher value which sits one position after
      b_index = (list_of_sequences.index(seqno)+1) # '+1' for moving DOWN
      
      b = list_of_sequences[b_index]
      #alert(str(a) + ' ' + str(b))
      row1 = app_tables.files.get(sequence=a)
      row2 = app_tables.files.get(sequence=b)
      
      a,b = self.swap(a,b)
      #alert(str(a) + ' ' + str(b))
      row1['sequence'] = a
      row2['sequence'] = b
  
    open_form('PDF_Form')
    
    

