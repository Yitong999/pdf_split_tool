# Description to how to use this program

## 1. Setup python required library
```bash
pip install PyPDF2
```

## 2. put the pdf waited to split into Workplace directory.

if more than one files in *Workplace -> print error message "please put a single pdf file in the *Workplace* folder"

if no pdf file is in *Workplace -> print "please put a pdf in the *Workplace* folder"

if the file in *Workplace is not pdf -> print "The file is NOT a PDF. Please try again"

## 3. Run the following command in your terminal
```bash
python main.py
```

all rendered pdfs are saved in *Output directory