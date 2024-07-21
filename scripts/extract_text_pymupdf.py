import fitz  # PyMuPDF


def extract_text_pymupdf(file_path):
    """
    Extrai texto de um arquivo PDF usando a biblioteca PyMuPDF.

    Args:
        file_path (str): O caminho para o arquivo PDF.

    Returns:
        str: O texto extraído do PDF.
    """
    pdf_document = fitz.open(file_path)
    text = ''
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text


if __name__ == "__main__":
    # Caminho para o arquivo PDF de exemplo
    file_path = '../data/erros.pdf'
    # Extração do texto
    text = extract_text_pymupdf(file_path)
    # Exibe uma parte do texto extraído
    print(text[:1000])
