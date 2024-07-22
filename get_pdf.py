
import fitz  # PyMuPDF
import json

def extract_content_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Initialize the result list
    pages = []
    
    for page_number in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_number)
        
        # Extract text from the page, preserve newlines
        text = page.get_text("text").replace("\r", "")  # Use "text" to preserve formatting
        
        if text:
            # Split text into lines and store each line as an item in an array
            lines = text.split('\n')
            # Append each line with "\n" to preserve it in JSON
            lines_with_newlines = [line + "\n" for line in lines if line.strip()]
            pages.append({
                "page": page_number + 1,
                "content": lines_with_newlines
            })
    
    return pages

def save_to_json(data, json_path):
    # Custom JSON dump to include actual newlines
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
        print("3.file data saved from pdf")







def main(filename):
    word_path = f'{filename}.docx'
    json_path = f'{filename}-filedata.json'
    pdf_path = f'{filename}.pdf'

 
    data = extract_content_from_pdf(pdf_path)
    save_to_json(data, json_path)