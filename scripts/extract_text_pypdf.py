import pypdf

def extract_text_pypdf(file_path):
    """
    Extrai texto de um arquivo PDF usando a biblioteca pypdf.

    Args:
        file_path (str): O caminho para o arquivo PDF.

    Returns:
        str: O texto extraído do PDF.
    """
    pdf_reader = pypdf.PdfReader(file_path)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text() or ''
    return text

if __name__ == "__main__":
    # Caminho para o arquivo PDF de exemplo
    file_path = '../data/sample.pdf'
    # Extração do texto
    text = extract_text_pypdf(file_path)
    # Exibe uma parte do texto extraído
    print(text[:1000])

