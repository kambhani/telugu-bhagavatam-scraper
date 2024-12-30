from pypdf import PdfWriter

# The pdf files to merge
pdfs = [
    'pdf/chapter1.pdf',
    'pdf/chapter2.pdf',
    'pdf/chapter3.pdf',
    'pdf/chapter4.pdf',
    'pdf/chapter5-1.pdf',
    'pdf/chapter5-2.pdf',
    'pdf/chapter6.pdf',
    'pdf/chapter7.pdf',
    'pdf/chapter8.pdf',
    'pdf/chapter9.pdf',
    'pdf/chapter10-1.pdf',
    'pdf/chapter10-2.pdf',
    'pdf/chapter11.pdf',
    'pdf/chapter12.pdf'
]

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("bhagavatam.pdf")
merger.close()