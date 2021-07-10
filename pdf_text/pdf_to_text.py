import textract
from pdf2docx import Converter
import PyPDF2


def use_textract(file):
    text = textract.process(file).decode()

    return text


def use_pdf2docx(file):
    cv = Converter(file)
    tables = cv.extract_tables()
    cv.close()

    # print(cv)
    # print(f"TOTAL TABLES: {len(tables)}")
    # print(tables[2])
    for row in tables[2]:
        print(row[0], row[1], sep="\t\t\t")


def pypdf_extract_text(pdf_file):
    # creating a pdf file object
    pdf_file_obj = open(pdf_file, 'rb')
    # creating a PdfFileReader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    num_pages = pdf_reader.numPages  # get number of pages
    pdf_info = pdf_reader.getDocumentInfo()  # get pdf information

    # print(num_pages)
    # print(pdf_info)

    page_obj = pdf_reader.getPage(2)
    text = page_obj.extractText()
    print(text)
    # closing pdf file object
    pdf_file_obj.close()


def rotate_pdf(original_pdf, rotated_pdf_name):
    pdf_file_obj = open(original_pdf, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # creating pdf writer object
    pdf_writer = PyPDF2.PdfFileWriter()

    # rotate all pages
    for page in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page)
        # rotate each page 90 degree clockwise
        page_obj.rotateClockwise(90)

        # adding rotated page to pdf writer object
        pdf_writer.addPage(page_obj)

    # new pdf file obj
    new_file = open(rotated_pdf_name, 'wb')
    pdf_writer.write(new_file)
    print('Successfully roated')

    new_file.close()
    pdf_file_obj.close()


if __name__ == "__main__":
    file_path = 'files/example.pdf'

    # output = use_textract(file_path)
    # output = use_pdf2docx(file_path)
    # print(output)

    # pypdf_extract_text(file_path)

    rotate_pdf(file_path, 'files/rotated_file.pdf')
