from pypdf import PdfReader, PdfWriter
import os

def split_pages_pypdf(file_path, output_folder):
    """
    Separa cada página de um arquivo PDF em arquivos individuais usando a biblioteca PyPDF.

    Args:
        file_path (str): O caminho para o arquivo PDF.
        output_folder (str): O diretório onde os arquivos individuais serão salvos.
    """
    reader = PdfReader(file_path)
    for page_number in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_number])
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.pdf")
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

if __name__ == "__main__":
    # Caminho para o arquivo PDF de exemplo
    file_path = '../data/sample.pdf'
    output_folder = 'results/pages_pypdf'
    os.makedirs(output_folder, exist_ok=True)
    # Separa as páginas
    split_pages_pypdf(file_path, output_folder)
