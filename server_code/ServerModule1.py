import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.files import data_files
import anvil.server

import anvil.media
import PyPDF2
import io


@anvil.server.callable
def merge_PDF_Files():

  # Create a PDF merger object
  pypdf2_merger = PyPDF2.PdfFileMerger()

  pdf_files = []
  # Loop over files in table
  for row in app_tables.files.search():
    print('merging files:')
    file_name  = row["file_name"]
    print(file_name)
    pdf_files.append(file_name)

    file = row["file"]
    # see https://anvil.works/forum/t/creating-and-manipulating-pdf-files-via-pypdf2-and-fpdf/901
    file_bytes = file.get_bytes()
    file_for_pdf_reader = io.BytesIO(file_bytes)
    pdfReader = PyPDF2.PdfFileReader(file_for_pdf_reader)

    pypdf2_merger.append(file_for_pdf_reader)

  
  # Output file where the merged PDF will be saved
  output_pdf = "merged.pdf"

  # Write the merged PDF to the output file
  with data_files.editing('merged.pdf') as path:
    with open(output_pdf, "wb") as output_file:
      pypdf2_merger.write(path)
    #with open(path, "wb") as f:
    #  f.write(output_file)
  
    # path is now a string path on the filesystem. We can write to it with normal Python tools.
    # For example:
    
      
  #media_obj = anvil.media.from_file(output_file)
  #media_obj = anvil.media.open(output_file)
  #output_file_bytes = io.BytesIO(output_file.get_bytes())
  #media_obj = anvil.media.open(output_file_bytes)
  
  #app_tables.files.add_row( file = media_obj, file_name = 'merged.pdf')
  
  # Close the merger object
  pypdf2_merger.close()




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
