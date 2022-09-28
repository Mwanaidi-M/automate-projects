import PyPDF2

# open a pdf file and extract some info
with open("SR-NormalPeople.pdf", "rb") as sally_pdf:
    pdf_reader = PyPDF2.PdfFileReader(sally_pdf)

    # check number of pages in the pdf file
    # print(f"Number of pages: {pdf_reader.numPages}")

    # create a page object to extract text from a page.
    # PyPDF2 uses a zero-based index for getting pages: The first page is page 0,
    # the second is page 1, and so on.
    page_12 = pdf_reader.getPage(11)

    text_pg12 = page_12.extractText()

    # check if a pdf file is encrypted
    # print(pdf_reader.isEncrypted)

# print(text_pg12)

"""
PyPDF2 doesn’t allow directly editing a PDF. Instead, you have to create a new PDF 
and then copy content over from an existing document. The steps to do this are:
1. Open one or more existing PDFs (the source PDFs) into PdfFileReader
objects.
2. Create a new PdfFileWriter object.
3. Copy pages from the PdfFileReader objects into the PdfFileWriter object.
4. Finally, use the PdfFileWriter object to write the output PDF.
"""

# opened an existing pdf file.
# with open("SR-NormalPeople.pdf", "rb") as rooney_pdf:
#
#     # created a pdfFileReader object.
#     r_pdf_reader = PyPDF2.PdfFileReader(rooney_pdf)
#
#     # created a pdfFileWriter object.
#     r_pdf_writer = PyPDF2.PdfFileWriter()
#
#     # loop through the pages in the pdfFileReader object.
#     for page_num in range(5, r_pdf_reader.numPages, 15):
#         # created a page object to get the text in that page
#         rooney_page_obj = r_pdf_reader.getPage(page_num)
#
#         # add that page object to the pdfFileWriter object.
#         r_pdf_writer.addPage(rooney_page_obj)
#
#     # create a new pdf file and open it in "wb" mode
#     with open("rooney.pdf", "wb") as copy_rooney:
#         # write to the new pdf file using the pdfFileWriter object.
#         r_pdf_writer.write(copy_rooney)

"""
The pages of a PDF can also be rotated in 90-degree increments with the 
rotateClockwise() and rotateCounterClockwise() methods.
Pass one of the integers 90, 180, or 270 to these methods. 
"""
with open("sample.pdf", "rb") as sample_pdf:
    reader_sample = PyPDF2.PdfFileReader(sample_pdf)
    page_0 = reader_sample.getPage(0)
    page_0.rotateCounterClockwise(270)

    writer_sample = PyPDF2.PdfFileWriter()
    writer_sample.addPage(page_0)

    # adding encryption to a file.
    # Before calling the write() method to save to a file, call the encrypt()
    # method and pass it a password string
    writer_sample.encrypt("sword234")

    with open("counter_sample.pdf", "wb") as new_sample:
        writer_sample.write(new_sample)