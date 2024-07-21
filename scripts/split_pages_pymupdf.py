import fitz  # PyMuPDF
import os

def split_pages_pymupdf(file_path, output_folder):
    """
    Separa cada página de um arquivo PDF em arquivos individuais usando a biblioteca PyMuPDF.

    Args:
        file_path (str): O caminho para o arquivo PDF.
        output_folder (str): O diretório onde os arquivos individuais serão salvos.
    """
    pdf_document = fitz.open(file_path)
    for page_number in range(len(pdf_document)):
        pdf_writer = fitz.open()
        pdf_writer.insert_pdf(pdf_document, from_page=page_number, to_page=page_number)
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.pdf")
        pdf_writer.save(output_path)
        pdf_writer.close()

if __name__ == "__main__":
    # Caminho para o arquivo PDF de exemplo
    file_path = '../data/sample.pdf'
    output_folder = 'results/pages_pymupdf'
    os.makedirs(output_folder, exist_ok=True)
    # Separa as páginas
    split_pages_pymupdf(file_path, output_folder)
