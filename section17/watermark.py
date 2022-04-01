import PyPDF2

super_pdf = PyPDF2.PdfFileReader(open("section17/super.pdf", "rb"))
watermark_pdf = PyPDF2.PdfFileReader(open("section17/wtr.pdf", "rb"))
output = PyPDF2.PdfFileWriter()


# getting the pages, for any number of pages
for i in range(super_pdf.getNumPages()):
    page = super_pdf.getPage(i)
    page.mergePage(watermark_pdf.getPage(0))
    output.addPage(page)


with open("section17/watermarked.pdf", mode="wb") as merged_file:
    output.write(merged_file)
