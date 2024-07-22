import json

import time



# Function to extract columns
def extract_columns(table):
    return table['table']['columns']

def extract_rows(table):
    return table['table']['rows']


def search_content_for_term2(page, term):
    new_list = []
    rest_of_list = []
    num = 0
    tablegoeshere=["\nTABLE GOES HERE\n"]
    found = False
    content1 = []
    content3 = []
    already_found = []
    if "content" in page: 
            content = page["content"]
            for i in range(len(content) - 1):
                line = content[i]
                combined_line = content[i].replace('\n', '') + content[i+1].replace('\n', '')
                if found:
                    content3.append(line) 

                elif (term.lower() in line.lower() or term.lower() in combined_line.lower()) and term not in already_found:
                      return i, True
                else:
                    content1.append(line)  #
 



    return 9999, False







# Extract columns from both JSON files
def search_content_for_term(page, term, second, already_found, endlook, loop = False):
    new_list = []
    rest_of_list = []
    num = 0
    tablegoeshere=["\nTABLE GOES HERE\n"]
    found = False
    content1 = []
    combined = False
    content3 = []
    

    if "content" in page: 
            content = page["content"]
            for i in range(len(content) - 1):
                line = content[i]
                combined_line = content[i].replace('\n', '') + content[i+1].replace('\n', '')
                if found:
                    content3.append(line) 
                
                elif (term.lower() in line.lower() or combined) and term not in already_found and len(term)+5 >= len(line):
                    found = True
                    content3.append(line)
                    combined = False
                    already_found.append(term)

                elif term.lower() in combined_line.lower() and term not in already_found:
                    combined = True
                    content1.append(line)
                else:
                    content1.append(line)  #
                    combined = False
     
            if content:
                content3.append(content[-1]) 

    found2 = False
    result = []
    if loop:
         return 999
 
    for line in reversed(content3):
          
            if endlook.lower() in line.lower():
             
                break
        
            else:
                 result.append(line)
        # Reverse the collected lines to maintain original order
  
 


    return found, content1, result
 

def main(filename):
  

    file2_path = f'{filename}-tables.json'
    file1_path =f'{filename}-filedata.json'

    with open(file1_path, 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)
  

    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)

    columns_from_file2 = []
    rows_from_file2 = []
    tbl_data = []
    for table in data2:
        columns_from_file2.append(extract_columns(table))

    for table in data2:
        rows = extract_rows(table)[-1]
        last_key = list(rows.values())[-1]
        rows_from_file2.append(last_key)
 
   
        tbl_data.append(table['table'])



    test = 0

    tabledata_found = []
    # Prepare structured data with appropriate keys
    structured_data = []
    for idx2, page in enumerate(data1):
        tblindex = None
   
        already_found = []
   
        for idx, columns in enumerate(columns_from_file2[test:]):
            to_look_for = columns[0].lower()
            second =  columns[1].lower()
            
            endlook = rows_from_file2[test:][idx].lower()
            endlook = endlook.split()[-1]
         
            

            found, content1, content3 = search_content_for_term(page, to_look_for,second, already_found, endlook)
            if found:
                 print(f"FOUND ON PAGE",idx2 + 1 )
                 tblindex = idx+test
     
                 break

        page_number = page.get("page", idx2 + 1)  # Default to idx + 1 if "page" key doesn't exist
        if found :
                test+=1
                content_dict = {
                    "pagenum": page_number,
                    "content1": content1,
                    "table": tbl_data[idx],
                    "content2": content3
                    
                }
                tabledata_found.append(tbl_data[idx])
                structured_data.append(content_dict)
        elif found :
                pass
        
        else:
             content_dict = {
                    "pagenum": page_number,
                    "content1": content1,
                    "content2": content3
                }
             structured_data.append(content_dict)
        content_dict = {
                    "pagebreak": 'pagebreak'
                   
                }
        structured_data.append(content_dict)
     
  
        
    




    output_file = f"{filename}-final.json"

    with open(output_file, 'w') as outfile:
        json.dump(structured_data, outfile, indent=2)