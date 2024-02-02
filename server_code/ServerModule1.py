import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

import anvil.media
import PyPDF2


@anvil.server.callable
def merge_PDF_Files():

  # Create a PDF merger object
  pypdf2_merger = PyPDF2.PdfFileMerger()

  pdf_files = []
  # Loop over files in table
  for row in app_tables.files.search():
    print('merging files:')
    file = row["file"]
    file_name  = row["file_name"]
    print(file_name)
    
    pdf_files.append(file_name)


    #pdf_file_to_merge = app_tables.files.get(file_name=file_name)
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # List of PDF files to be merged
    #pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]




  
  for pdf_file in pdf_files:
    #pdf_merger.append(pdf_file)
    #pdf_merger.append(merged_file['file_name'])
    pass

  
  #app_tables.files.add_row( file=merged_file['file'], file_name=merged_file['file_name'])
  
  # Close the merger object
  pdf_merger.close()




# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
