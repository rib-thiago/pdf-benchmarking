import pdfplumber

def extract_text_pdfplumber(file_path):
    """
    Extrai texto de um arquivo PDF usando a biblioteca pdfplumber.

    Args:
        file_path (str): O caminho para o arquivo PDF.

    Returns:
        str: O texto extraído do PDF.
    """
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

if __name__ == "__main__":
    # Caminho para o arquivo PDF de exemplo
    file_path = '../data/sample.pdf'
    # Extração do texto
    text = extract_text_pdfplumber(file_path)
    # Exibe uma parte do texto extraído
    print(text[:1000])
