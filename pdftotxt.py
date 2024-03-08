import pytesseract
from pytesseract import image_to_string
from pdf2image import convert_from_path
import PyPDF2
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path, output_file_path):
    extracted_text = []  # This list will store the extracted text

    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            # Convert PDF page to image
            images = convert_from_path(pdf_path, first_page=page_num+1, last_page=page_num+1)

            # Perform OCR on the image
            page_text = image_to_string(images[0])

            # Append the text for this page to the list
            extracted_text.append(page_text)

    # Combine the text from all pages and write to a file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("\n".join(extracted_text))

# Specify  directory containing the PDF files
pdf_dir = r"path_to_directory"

# Iterate over all PDF files in the directory
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, pdf_file)
        # Construct the output file path by replacing the PDF extension with "_TXT.txt"
        output_file_path = os.path.join(pdf_dir, pdf_file[:-4] + "_TXT.txt")
        
        # Extract text from the PDF and write to the file
        extract_text_from_pdf(pdf_path, output_file_path)
        
        print(f"Text extraction completed for {pdf_file}. The text has been saved to: {output_file_path}")
