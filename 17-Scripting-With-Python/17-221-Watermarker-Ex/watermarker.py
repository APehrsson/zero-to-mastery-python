import PyPDF2
import sys

wtr = sys.argv[1]
pdf = sys.argv[2]
watermarked_pdf = sys.argv[3]

def watermarker(mark, to_be_marked, marked):
    with open(mark, 'rb') as watermark_file, open(to_be_marked, 'rb') as input_file:
        reader = PyPDF2.PdfFileReader(input_file)
        watermark_reader = PyPDF2.PdfFileReader(watermark_file)
        watermark_page = watermark_reader.pages[0]

        writer = PyPDF2.PdfFileWriter()

        for page in reader.pages:
            page.mergePage(watermark_page)
            writer.addPage(page)

        with open(marked, 'wb') as output_file:
            writer.write(output_file)

watermarker(wtr, pdf, watermarked_pdf)



