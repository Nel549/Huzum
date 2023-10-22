import fitz  # PyMuPDF
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_document:
        num_pages = pdf_document.page_count
        for page_num in range(num_pages):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
    return text

def write_text_to_file(text, output_file):

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)



pdf_path = "7.pdf"  # Replace with your PDF file path
output_file = "7.txt"  # Replace with the desired output file name

extracted_text = extract_text_from_pdf(pdf_path)
write_text_to_file(extracted_text, output_file)









# import requests
# import json
# get_link = requests.get('https://file.notion.so/f/f/ba535503-9bce-4686-86ed-0e28252f817c/c6dbfe71-86f4-4d16-9f5c-4e74e7bd6d35/fdv_stands20230920.geojson?id=8f098f20-27e5-4aa0-bdf4-da147574c90b&table=block&spaceId=ba535503-9bce-4686-86ed-0e28252f817c&expirationTimestamp=1697983200000&signature=_eg0dtH7Dd80O0d8oEf7SAbFZzacLkIXLusImWYwb1g&downloadName=fdv_stands20230920.geojson')
# m = get_link.text
# json_data = json.loads(m)
# with open('5json.txt','w') as file:
#     file.write(str(json_data))
# import csv
# # Open the CSV file for reading
# with open('5.csv', 'r' , encoding='ISO-8859-1') as input_file:
#     csv_reader = csv.reader(input_file)
#     with open('6.txt','w') as file:
#         for row in csv_reader:
#             file.write(f'{str(row)}\n')

import PyPDF2

pdf_path = '7.pdf'  # Replace with your PDF file path
pdf_file = open(pdf_path, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Iterate through the pages and extract text
for page_number in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_number]
    text = page.extract_text()
    print(text)

# Close the PDF f3ile
pdf_file.close()