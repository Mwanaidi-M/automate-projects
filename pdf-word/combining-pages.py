"""
Say you have the boring job of merging several dozen PDF documents into
a single PDF file. Each of them has a cover sheet as the first page, but you
don’t want the cover sheet repeated in the final result. Even though there
are lots of free programs for combining PDFs, many of them simply merge
entire files together. This Python program is supposed to customize which pages
you want in the combined PDF.

At a high level, here’s what the program will do:
• Find all PDF files in the current working directory.
• Sort the filenames so the PDFs are added in order.
• Write each page, excluding the first page, of each PDF to the
output file.

In terms of implementation, your code will need to do the following:
• Call os.listdir() to find all the files in the working directory and
remove any non-PDF files.
• Call Python’s sort() list method to alphabetize the filenames.
• Create a PdfFileWriter object for the output PDF.
• Loop over each PDF file, creating a PdfFileReader object for it.
• Loop over each page (except the first) in each PDF file.
• Add the pages to the output PDF.
• Write the output PDF to a file named medley.pdf.
"""

import os, PyPDF2


# get a list of all files with the .pdf extension in the current working directory
# and sort them.

pdf_files = []

for file_name in os.listdir("."):
    if file_name.endswith(".pdf"):
        pdf_files.append(file_name)

pdf_files.sort()

# create a pdf file writer object
writer_pdf = PyPDF2.PdfFileWriter()

# loop through all pdf files
for file in pdf_files:
    with open(file, "rb") as f_pdf:
        reader_pdf = PyPDF2.PdfFileReader(f_pdf)

        # Loop through the pages (except the first) and add them to the writer obj.
        for num_pages in range(2, reader_pdf.numPages, 10):
            page_obj = reader_pdf.getPage(num_pages)

            writer_pdf.addPage(page_obj)

        # writing the output to the new created pdf file.
        with open("medley.pdf", "wb") as medley:
            writer_pdf.write(medley)
