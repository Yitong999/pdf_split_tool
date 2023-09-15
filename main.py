# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import PyPDF2
import os 
import re

def main():
    if valid_check() == False:
        return
    
    output_folder = 'Output'

    # Check if the folder exists
    if not os.path.exists(output_folder):
        # If it doesn't exist, create the folder
        os.makedirs(output_folder)
 

    work_path = "Workplace"
    files_in_folder = os.listdir(work_path)
    file_path = "Workplace/" + files_in_folder[0]

    pdf = PyPDF2.PdfReader(open(file_path, 'rb'))

    for page_number in range(len(pdf.pages)):
        # Create a new PDF writer object for each page
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf.pages[page_number])

        name = read_name(file_path, page_number)
        # Generate a filename for the current page (e.g., page_1.pdf, page_2.pdf, etc.)
        output_filename = f'Output/{name}_page_{page_number}.pdf'

        # Save the page as a separate PDF file
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        # if page_number > 10:
        #     break


    print(f'Saved {len(pdf.pages)} pages as separate PDF files.')



def valid_check():
    work_path = "Workplace"

    files_in_folder = os.listdir(work_path)

    if len(files_in_folder) == 0:
        print("please put a pdf in the *Workplace* folder")
        return False
    elif len(files_in_folder) > 1:
        print("please put a single pdf file in the *Workplace* folder")
        return False
    
    file_path = files_in_folder[0]
        # Get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # Check if the file extension is ".pdf"
    if file_extension != '.pdf':
        print("The file is NOT a PDF. Please try again")
        return False
   
    return True

def read_name(pdf_file_path, page_num, line_number = 1):
        # Open the PDF file
    pdf = PyPDF2.PdfReader(open(pdf_file_path, 'rb'))

    # Extract the text from the chosen page
    page = pdf.pages[page_num]
    page_text = page.extract_text()

    # Split the extracted text into lines
    lines = page_text.split('\n')

    line_num = line_number
    # Read the selected line
    selected_line = lines[line_num]

    words = selected_line.split()
    name = words[0]

    # Define a regular expression pattern for a number
    pattern = r'\d+'
    match = re.search(pattern, name)

    print(name)
    if match:
        name = read_name(pdf_file_path, page_num, line_number = line_num + 1)
    if ',' in name:
        name = words[0].replace(',', '')
    elif '/' in name:
        name = words[0].replace('/', '')
    elif name.endswith('.'):
        name = words[0].replace('.', '')
    elif name == 'Rodriguez':
        name = name
    elif name == 'Schulte':
        name = name
    else:
        name = read_name(pdf_file_path, page_num, line_number = line_num + 1)
    # print(name)
    
    return name

def clean():
    # Specify the path to the "Output" folder
    output_folder = 'Output'  # Replace with the actual path to your folder

    # Check if the folder exists
    if os.path.exists(output_folder) and os.path.isdir(output_folder):
        # Get a list of files in the folder
        files_in_folder = os.listdir(output_folder)
        
        # Loop through the files and remove each one
        for file_name in files_in_folder:
            file_path = os.path.join(output_folder, file_name)
            os.remove(file_path)
        
        print(f"All previous files in the '{output_folder}' folder have been removed.")










if __name__ == '__main__':
    clean()
    main()