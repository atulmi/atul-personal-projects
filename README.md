# Atul Murali's personal projects
This repo contains various Python side projects I've developed to make my life easier.

## pdf-page-count.py
- Goal of this program: generate a spreadsheet listing all PDF files (recursively) in a directory, along with page count for each PDF
- Example usage: python3 pdf-page-count.py Books/
- Result: a spreadsheet containing all PDF titles in Books and its subdirectories (like "Fiction", "Nonfiction", etc) along with the page count of those PDFs

## generate-book-notes-chapter-template.py
- Goal of this program: generate a docx note-taking template for a set of books
- For each book, a docx will be generated with "Intro, Chapter 1, Chapter 2... Conclusion" all on separate lines
- As a command-line argument, we pass a spreadsheet, where each row has 2 items: book title & its number of chapters
- Usage: "python3 generate-book-notes-chapter-template.py test-spreadsheet.xlsx"
- Result: 1 note-taking template for each book listed in above spreadsheet will be created in CURRENT directory, unless a docx with that book already exists (we don't want to overwrite existing book note documents!)

## generate-book-notes-page-blocks.py
- Goal of this program: generate a docx note-taking template for a set of PDF books in the given directory (passed as 1st argument on command-line)
- Each docx will be populated with entries/headings for each block of "n" pages until final page count of book is reached (number of pages per block is provided as 2nd argument)

- Ex: if n=20 and the PDF has 567 pages, the docx will have page block entries like "Pages 1-20", "Pages 21-40", "Pages 41-60"... "Pages 560-567", etc, all on separate lines. The page block entry/heading will be bolded
- Ex: if n=1, the docx will have headings like "Page 1, Page 2, Page 3", etc, all on separate lines. The page entry/heading will be bolded

- Example usage: "python3 generate-book-notes-page-blocks.py Example-PDF-Directory/ 20"
- The docx templates will be created in CURRENT directory (not the one provided as an argument). Thus, the directory containing PDF books (given as argument) doesn't get cluttered with the note-taking templates
- Not all PDFs have a clear concept of chapters (they might have "sections" or "parts"), so this script (unlike the above script "generate-book-notes-chapter-template.py" creates entries for each set of "n" pages, rather than 1 entry for each chapter
- This program only supports PDF files. If there are books in EPUB or other book formats, use Calibre or some other program to convert to PDF before running this program

## generate-spreadsheet-from-tsv.py
- Goal of this program: generate a spreadsheet from a set of TSV (tab separated values) files
- The spreadsheet will have separate tabs containing each file's content (with the tab name being same as filename)
- Example usage: python3 generate-spreadsheet-from-tsv.py Book-List.tsv Articles-List.tsv Games-List.tsv
- Result: a spreadsheet with tabs "Book-List", "Articles-List", and "Games-List", each containing the full content of the respective file

## parse-country-studies.py
- Goal of this program: parse a Country Study page for a given country (published by Library of Congress) into a text file
- As a command-line argument, provide the name of the country as given in the URL for that country, on the website http://countrystudies.us
- Example usage for https://countrystudies.us/germany:
- python3 parse-country-studies.py germany
- Result: a file "germany.txt" containing the full content of the Library of Congress country study on Germany
