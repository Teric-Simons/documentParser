import json
from docx import Document


def extract_content_from_docx(docx_path):
    # Load the Word document
    doc = Document(docx_path)
    
    # Initialize result list
    pages = []
    current_page = {"page": 1, "content": ""}
    
    for element in doc.element.body:
        if element.tag.endswith('tbl'):
            # If there's existing content in current_page, save it
            if current_page["content"].strip():
                pages.append(current_page)
                current_page = {"page": current_page["page"] + 1, "content": ""}

            # Process table
            table = doc.tables[len(pages)]  # Assuming tables and text are processed in order

            # Extract columns
            columns = [cell.text.strip() for cell in table.rows[0].cells if cell.text.strip()]

            # Check if both columns and rows_data are empty or only contain empty strings
            if not columns and all(all(cell.text.strip() == '' for cell in row.cells) for row in table.rows[1:]):
                continue  # Skip processing this table if both are empty or only whitespace

            # Process rows
            rows_data = []
            for row in table.rows[1:]:
                row_data = {}
                for idx, cell in enumerate(row.cells):
                    cell_text = cell.text.strip()
                    if cell_text:  # Add to row_data only if cell text is not empty
                        row_data[columns[idx]] = cell_text
                rows_data.append(row_data)

            # Append table data to pages if it contains meaningful data
            if columns or rows_data:
                pages.append({
                    "page": len(pages) + 1,
                    "table": {
                        "columns": columns,
                        "rows": rows_data
                    }
                })

    
    # Append the last page if it has content
    if current_page["content"].strip():
        pages.append(current_page)
    
    return pages

def save_to_json(data, json_path):
 
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
        print("1.All tables extracted")





def main(filename):
    docx_path = f'{filename}.docx'
 
    json_path = f'{filename}-tables.json'



    data = extract_content_from_docx(docx_path)
    if data:
        save_to_json(data, json_path)
        return True
    else:
        print("1.No tables in file")
        return False
