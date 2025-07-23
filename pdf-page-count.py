# Goal of this program: generate a spreadsheet listing all PDF files (recursively) in a directory, along with page count for each PDF
# Example usage: python3 pdf-page-count.py Books/

import PyPDF2
import fitz
from pathlib import Path
from os import sys
import xlsxwriter

source_dir = sys.argv[1]
pdf_files = []
pdf_filenames = []

for path in Path(source_dir).rglob('*.pdf'):
    pdf_files.append(path.resolve())
    pdf_filenames.append(path.name)


workbook = xlsxwriter.Workbook('pdf-pages.xlsx')
worksheet = workbook.add_worksheet()

for index, pdf in enumerate(pdf_files):
    file = fitz.open(pdf)

    totalPages = len(file)

    print("filename and page count: ", pdf_filenames[index], totalPages) # useful for debugging purposes

    toWrite1 = str(pdf_filenames[index])
    toWrite2 = totalPages

    worksheet.write(index, 0, toWrite1)
    worksheet.write(index, 1, toWrite2)


workbook.close()
file.close()
