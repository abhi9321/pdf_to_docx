from pdf2docx import Converter

pdf_file = 'input/sample_pdf.pdf'
docx_file = 'output/resume.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
