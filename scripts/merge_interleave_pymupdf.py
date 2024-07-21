import fitz  # PyMuPDF
import os

def merge_interleave_pymupdf(file1_path, file2_path, output_path):
    """
    Faz o merge de dois arquivos PDF intercalando as páginas usando a biblioteca PyMuPDF.

    Args:
        file1_path (str): O caminho para o primeiro arquivo PDF.
        file2_path (str): O caminho para o segundo arquivo PDF.
        output_path (str): O caminho para o arquivo PDF resultante.
    """
    # Cria o diretório de saída, se não existir
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    pdf1 = fitz.open(file1_path)
    pdf2 = fitz.open(file2_path)
    pdf_writer = fitz.open()

    max_pages = max(len(pdf1), len(pdf2))

    for i in range(max_pages):
        if i < len(pdf1):
            pdf_writer.insert_pdf(pdf1, from_page=i, to_page=i)
        if i < len(pdf2):
            pdf_writer.insert_pdf(pdf2, from_page=i, to_page=i)

    pdf_writer.save(output_path)
    pdf_writer.close()

if __name__ == "__main__":
    # Caminhos para os arquivos PDF de exemplo
    file1_path = '../data/sample.pdf'
    file2_path = '../data/erros.pdf'
    output_path = 'results/merged_interleaved_pymupdf.pdf'
    # Faz o merge intercalado
    merge_interleave_pymupdf(file1_path, file2_path, output_path)
