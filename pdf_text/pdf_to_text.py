import textract


def use_textract(file):
    text = textract.process(file).decode()

    return text


def use_pdf2docx(file):
    pass


def use_pypdf(file):
    pass


if __name__ == "__main__":
    file_path = 'files/test.pdf'
    output = use_textract(file_path)
    print(output)
