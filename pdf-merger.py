import sys
import PyPDF2


def pdf_merge(inputs):
    # create a pdf merger
    merger = PyPDF2.PdfFileMerger()
    # loop through the pdfs and concate together
    for file in inputs:
        merger.append(PyPDF2.PdfFileReader(file, 'rb'))
    # complete writing to a merged pdf
    merger.write("merged-file.pdf")


if __name__ == '__main__':
    inputs = sys.argv[1:]
    pdf_merge(inputs)
