from pypdf import PdfReader, PdfWriter
import os

def merge_interleave_pypdf(file1_path, file2_path, output_path):
    """
    Faz o merge de dois arquivos PDF intercalando as páginas usando a biblioteca PyPDF.

    Args:
        file1_path (str): O caminho para o primeiro arquivo PDF.
        file2_path (str): O caminho para o segundo arquivo PDF.
        output_path (str): O caminho para o arquivo PDF resultante.
    """
    # Cria o diretório de saída, se não existir
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    reader1 = PdfReader(file1_path)
    reader2 = PdfReader(file2_path)
    writer = PdfWriter()

    max_pages = max(len(reader1.pages), len(reader2.pages))

    for i in range(max_pages):
        if i < len(reader1.pages):
            writer.add_page(reader1.pages[i])
        if i < len(reader2.pages):
            writer.add_page(reader2.pages[i])

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

if __name__ == "__main__":
    # Caminhos para os arquivos PDF de exemplo
    file1_path = '../data/sample.pdf'
    file2_path = '../data/erros.pdf'
    output_path = 'results/merged_interleaved_pypdf.pdf'
    # Faz o merge intercalado
    merge_interleave_pypdf(file1_path, file2_path, output_path)
