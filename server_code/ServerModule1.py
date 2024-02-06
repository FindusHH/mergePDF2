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



# merge PDF-Files which are uploaded
@anvil.server.callable
def merge_PDF_Files():

  #----- Step 1: clear previous merged PDF file -----
  # Output PDF file where the cleared PDF will be saved
  output_pdf = "cleared.pdf"

  # Create an empty PDF object
  pdf_cleared = PyPDF2.PdfFileWriter()

  # Create a PDF merger object
  pypdf2_merger = PyPDF2.PdfFileMerger()
  
  # remove all pages from existing target-PDF-File "merged.pdf"
  # Loop over files in table
  for row in app_tables.files.search( tables.order_by("sequence",ascending=True),file_name = q.not_(None)):
    print('clearing previous merged file...')
    file = row["file"]

    # Read file byte by byte
    # see https://anvil.works/forum/t/creating-and-manipulating-pdf-files-via-pypdf2-and-fpdf/901
    file_bytes = file.get_bytes()
    file_for_pdf_reader = io.BytesIO(file_bytes)
    pdfReader = PyPDF2.PdfFileReader(file_for_pdf_reader)

    # Iterate through the existing pages of the previous merge and add none of them to the cleared PDF object
    for page_num in range(pdfReader.getNumPages()):
      print("Page " + str(page_num))
      pass  # This effectively skips adding any pages

    # Write the cleared PDF to the output file
    with open(output_pdf, "wb") as output_file:
        pdf_cleared.write(output_file)

    # save output file to filesystem
    with data_files.editing('merged.pdf') as path:
      with open(output_pdf, "wb") as output_file:
        pypdf2_merger.write(path)

  # Close the merger object
  pypdf2_merger.close()
  
  print("Pages removed from the PDF successfully!")

  #----- Step 2: merge PDF files -----  
  # Create a PDF merger object
  pypdf2_merger = PyPDF2.PdfFileMerger()

  pdf_files = []
  # Loop over files in table, exclude files without filenames, sort by sequence number
  for row in app_tables.files.search( tables.order_by("sequence",ascending=True),file_name = q.not_(None)):
    print('merging files:')
    file_name  = row["file_name"]
    print(" - " + file_name)
    pdf_files.append(file_name)

    file = row["file"]
    # Read file byte by byte
    # see https://anvil.works/forum/t/creating-and-manipulating-pdf-files-via-pypdf2-and-fpdf/901
    file_bytes = file.get_bytes()
    file_for_pdf_reader = io.BytesIO(file_bytes)
    pdfReader = PyPDF2.PdfFileReader(file_for_pdf_reader)

    # Error handling, not every PDF-File can be merged/processed
    try:
      pypdf2_merger.append(file_for_pdf_reader)
      
    except Exception as error:
      ret_message = "Datei kann nicht verarbeitet werden: " + file_name + "\n\n" 
      error_message = "Fehlermeldung: " + str(error)
      #print(ret_message + error_message)

      return (ret_message + error_message)

  
  # Set output file for the merged PDF - file
  output_pdf = "merged.pdf"

  # Write the merged PDF to the output file
  with data_files.editing('merged.pdf') as path:
    with open(output_pdf, "wb") as output_file:
      pypdf2_merger.write(path)

  # Close the merger object
  pypdf2_merger.close()
  ret_message = "Dateien wurden zusammengeführt." 

  return ret_message




# create a link for downloading the merged PDF File
@anvil.server.callable
def get_link_to_merged_PDF():
  # Loop over files in table
  for row in app_tables.files.search(sequence = q.greater_than_or_equal_to(99)):
    print('providing link to merged file...')
    file = row["file"]
    url = file.get_url()
    print(url)
  return(url)



@anvil.server.callable
def get_list_of_sequences_and_max_seqno():
  list_of_sequence_values =[]
  maximum = 1
  
  # select max sequence value where filename is not none
  for row in app_tables.files.search(file_name = q.not_(None)):
    sequence = row["sequence"]
    list_of_sequence_values.append(sequence)
    maximum = max(list_of_sequence_values)

    # MUST sort the the list by sequence numbers
    list_of_sequence_values.sort()
    
  return maximum, list_of_sequence_values
    


  





