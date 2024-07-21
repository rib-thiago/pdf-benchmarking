# 📊 PDF Benchmarking

Bem-vindo ao repositório **PDF Benchmarking**! Este projeto tem como objetivo comparar o desempenho e a facilidade de uso de três bibliotecas populares de manipulação de PDFs em Python: pdfplumber, PyPDF e PyMuPDF.

## 🚀 Objetivo

Realizar um estudo comparativo e benchmarking das bibliotecas com base nas seguintes métricas:
- ⏱ Tempo de Execução
- 🧠 Precisão da Extração de Texto
- 🧩 Consumo de Memória
- 📄 Capacidade de Lidar com PDFs Complexos
- 🤖 Facilidade de Uso e API
- 🔄 Compatibilidade e Suporte a Formatos
- 🛠 Tratamento de Erros e Robustez

Consultar mais detalhes sobre as métricas em [Métricas](Metricas.md)

## 📋 Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `data/`: Contém os arquivos PDF utilizados para os testes.
- `scripts/`: Scripts para extração de texto, separação de páginas e merge intercalado, além do script principal de benchmark.
- `results/`: Resultado dos benchmarks realizados.
- `Metricas.md`: Arquivo com uma discussão sobre as Métricas
- `README.md`: Este arquivo com instruções sobre o projeto.
- `Resultados.md`: Arquivo que compila dos resultados obtidos até o momento.

## 🛠️ Configuração do Ambiente

Este projeto utiliza [Poetry](https://python-poetry.org/) para gerenciamento de dependências. Siga os passos abaixo para configurar seu ambiente:

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/rib-thiago/pdf-benchmarking.git
    cd pdf-benchmarking
    ```

2. **Instale o Poetry (se ainda não tiver):**

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Instale as dependências do projeto:**

    ```bash
    poetry install
    ```

4. **Ative o ambiente virtual do Poetry:**

    ```bash
    poetry shell
    ```

## 📜 Scripts de Benchmarking

| script | Descrição |
| :----- | :-------- |
| `extract_text_pdfplumber.py` | Script para extração de texto usando pdfplumber |
| `exract_text_pypdf.py` | Script para extração de texto usando PyPDF |
| `extract_text_pymupdf.py` | Script para extração de texto usando PyMuPDF |
| `split_pages_pypdf.py` | Script para divisão de páginas usando PyPDF |
| `split_pages_pymupdf.py` | Script para divisão de páginas usando PyMuPDF |
| `merge_interleave_pypdf.py` | Script para mesclagem intercalada usando PyPDF |
| `merge_interleave_pymupdf.py` | Script para mesclagem intercalada usando PyMuPDF |
| `benchmark.py` | Script principal para executar os testes de desempenho |

## 🏃‍♂️ Executando os Testes

Para executar os testes de benchmark, utilize o seguinte comando:

```bash
python scripts/benchmark.py
```

## 📝 Resultados e Análise

Os resultados dos testes, incluindo o tempo de execução e a facilidade de uso de cada biblioteca, serão documentados na pasta `results`.

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests. Qualquer feedback é bem-vindo!

## 📄 Licença

Este projeto está licenciado sob a GNU Affero General Public License v3.0. veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📚 Referências

Aqui estão alguns recursos úteis para as bibliotecas de manipulação de PDFs utilizadas neste projeto:

- 📄 **pdfplumber**: [Documentação oficial](https://github.com/jsvine/pdfplumber)
- 📑 **PyPDF**: [Documentação oficial](https://pypdf.readthedocs.io/en/latest/)
- 📜 **PyMuPDF**: [Documentação oficial](https://pymupdf.readthedocs.io/en/latest/)

Essas documentações fornecem guias detalhados, exemplos de uso e informações sobre as APIs de cada biblioteca.


---
Feito por [Thiago Ribeiro](https://github.com/rib-thiago)