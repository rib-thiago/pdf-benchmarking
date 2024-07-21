import timeit
import memory_profiler
import os

from scripts.extract_text_pdfplumber import extract_text_pdfplumber
from scripts.extract_text_pypdf import extract_text_pypdf
from scripts.extract_text_pymupdf import extract_text_pymupdf

from scripts.merge_interleave_pymupdf import merge_interleave_pymupdf
from scripts.merge_interleave_pypdf import merge_interleave_pypdf

from scripts.split_pages_pypdf import split_pages_pypdf
from scripts.split_pages_pymupdf import split_pages_pymupdf


def create_directory(directory):
    """Cria um diretório se não existir."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def run_benchmark(file_path, file1_path, file2_path):
    """
    Executa os testes de benchmark para as bibliotecas pdfplumber, PyPDF e PyMuPDF.

    Args:
        file_path (str): O caminho para o arquivo PDF de exemplo.
        file1_path (str): O caminho para o primeiro arquivo PDF para merge.
        file2_path (str): O caminho para o segundo arquivo PDF para merge.

    Returns:
        dict: Resultados do benchmark com tempos de execução e uso de memória.
    """
    # Número de execuções para cada teste
    num_executions = 50

    def benchmark_text_extraction(extraction_func):
        print(
            f"Benchmarking {extraction_func.__name__} - Extração de Texto...")
        time_taken = timeit.timeit(lambda: extraction_func(file_path),
                                   number=num_executions)
        mem_usage = memory_profiler.memory_usage(
            (extraction_func, (file_path, )), max_usage=True)
        return time_taken, mem_usage

    def benchmark_page_splitter(split_func, output_folder):
        print(f"Benchmarking {split_func.__name__} - Separação de Páginas...")
        create_directory(output_folder)
        time_taken = timeit.timeit(
            lambda: split_func(file_path, output_folder),
            number=num_executions)
        mem_usage = memory_profiler.memory_usage(
            (split_func, (file_path, output_folder)), max_usage=True)
        return time_taken, mem_usage

    def benchmark_merge(merge_func, file1_path, file2_path, output_path):
        print(f"Benchmarking {merge_func.__name__} - Merge Intercalado...")
        time_taken = timeit.timeit(
            lambda: merge_func(file1_path, file2_path, output_path),
            number=num_executions)
        mem_usage = memory_profiler.memory_usage(
            (merge_func, (file1_path, file2_path, output_path)),
            max_usage=True)
        return time_taken, mem_usage

    # Benchmark para pdfplumber
    print("\nIniciando benchmark para pdfplumber...")
    time_pdfplumber_extract, mem_pdfplumber = benchmark_text_extraction(
        extract_text_pdfplumber)

    # Benchmark para PyPDF
    print("\nIniciando benchmark para PyPDF...")
    time_pypdf_extract, mem_pypdf = benchmark_text_extraction(
        extract_text_pypdf)
    time_pypdf_split, mem_pypdf_split = benchmark_page_splitter(
        split_pages_pypdf, 'results/pages_pypdf')
    time_pypdf_merge, mem_pypdf_merge = benchmark_merge(
        merge_interleave_pypdf, file1_path, file2_path,
        'results/merged_interleaved_pypdf.pdf')

    # Benchmark para PyMuPDF
    print("\nIniciando benchmark para PyMuPDF...")
    time_pymupdf_extract, mem_pymupdf = benchmark_text_extraction(
        extract_text_pymupdf)
    time_pymupdf_split, mem_pymupdf_split = benchmark_page_splitter(
        split_pages_pymupdf, 'results/pages_pymupdf')
    time_pymupdf_merge, mem_pymupdf_merge = benchmark_merge(
        merge_interleave_pymupdf, file1_path, file2_path,
        'results/merged_interleaved_pymupdf.pdf')

    return {
        "pdfplumber_extract": (time_pdfplumber_extract, mem_pdfplumber),
        "PyPDF_extract": (time_pypdf_extract, mem_pypdf),
        "PyPDF_split": (time_pypdf_split, mem_pypdf_split),
        "PyPDF_merge": (time_pypdf_merge, mem_pypdf_merge),
        "PyMuPDF_extract": (time_pymupdf_extract, mem_pymupdf),
        "PyMuPDF_split": (time_pymupdf_split, mem_pymupdf_split),
        "PyMuPDF_merge": (time_pymupdf_merge, mem_pymupdf_merge)
    }


if __name__ == "__main__":
    # Caminho para o arquivo PDF de exemplo e para os arquivos de merge
    file_path = 'data/sample.pdf'
    file1_path = 'data/sample.pdf'
    file2_path = 'data/erros.pdf'

    # Executa o benchmark
    results = run_benchmark(file_path, file1_path, file2_path)

    # Exibe os resultados
    print("\nResultados do Benchmark:\n")
    for label, (time_taken, mem_usage) in results.items():
        method_name = label.replace('_', ' ').title()
        print(
            f"{method_name}:\nTempo: {time_taken:.2f} segundos\nMemória: {mem_usage:.2f} MB\n"
        )

    # Salva os resultados em um arquivo
    with open('results/benchmark_results.txt', 'w') as result_file:
        result_file.write("Resultados do Benchmark:\n")
        result_file.write('\n')
        for label, (time_taken, mem_usage) in results.items():
            method_name = label.replace('_', ' ').title()
            result_file.write(
                f"{method_name}:\nTempo: {time_taken:.2f} segundos\nMemória: {mem_usage:.2f} MB\n"
            )
            result_file.write('\n')
