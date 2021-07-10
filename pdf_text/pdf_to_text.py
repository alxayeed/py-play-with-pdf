import textract
from pdf2docx import Converter


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


def use_pypdf(file):
    pass


if __name__ == "__main__":
    file_path = 'files/test.pdf'
    # output = use_textract(file_path)
    output = use_pdf2docx(file_path)
    # print(output)
