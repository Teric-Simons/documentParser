import os
import glob
import getTables
import get_pdf
import link
import time
from convert_toPDF import *

# Folder path containing .docx files
folder_path = 'samples'

# Iterate over all .docx files in the folder
for filename in glob.glob(os.path.join(folder_path, '*.docx')):
    file_name = os.path.splitext(os.path.basename(filename))[0]  # Extract file name without extension
    file_name = os.path.join(folder_path, file_name)
    #file_name=f'word-table'
    
    if getTables.main(file_name):
        table_infile = True
    else:
        table_infile = False
    
    word_path = f'{filename}.docx'
    pdf_path = f'{filename}.pdf'
    if convert_docx_to_pdf(word_path, pdf_path):
        
        get_pdf.main(file_name)
     
   
    
    if table_infile:
        link.main(file_name)
        print(f"{file_name}: Tables found - updating file.")
    else:
        print(f"{file_name}: No tables - skip step.")
    
    print(f"{file_name}: Done processing.")

print("All files processed.")
