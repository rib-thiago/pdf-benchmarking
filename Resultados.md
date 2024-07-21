# 🧪 Análise Detalhada dos Resultados do Benchmark das Bibliotecas para manipulação de PDF

## 📊 Introdução
Este documento fornece uma análise detalhada dos resultados do benchmark realizado para comparar as bibliotecas `pdfplumber`, `PyPDF` e `PyMuPDF` nas funcionalidades de extração de texto, separação de páginas e merge intercalado. O foco é avaliar o desempenho em termos de tempo e uso de memória.

---

## 🚀 Resultados do Benchmark

### 1. Extração de Texto

| Biblioteca   | Tempo Total (50 Execuções) | Memória Máxima (MB) |
|--------------|----------------------------|---------------------|
| Pdfplumber   | 0.38 segundos              | 72.95 MB            |
| PyPDF        | 0.18 segundos              | 78.45 MB            |
| PyMuPDF      | 0.04 segundos              | 93.92 MB            |

#### Análise:
- **Pdfplumber**: A extração de texto com `pdfplumber` levou mais tempo comparado ao `PyPDF` e `PyMuPDF`, com um total de 0.38 segundos. No entanto, a memória usada foi a menor entre os três, 72.95 MB.
- **PyPDF**: Com um tempo de 0.18 segundos, o `PyPDF` foi significativamente mais rápido que o `pdfplumber`, mas utilizou mais memória, 78.45 MB.
- **PyMuPDF**: O `PyMuPDF` apresentou o melhor desempenho em termos de tempo, completando a extração em apenas 0.04 segundos, porém, consumiu a maior quantidade de memória, 93.92 MB.

### 2. Separação de Páginas

| Biblioteca   | Tempo Total (50 Execuções) | Memória Máxima (MB) |
|--------------|-----------------------------|---------------------|
| PyPDF         | 0.53 segundos               | 80.70 MB            |
| PyMuPDF       | 0.46 segundos               | 94.04 MB            |

#### Análise:
- **PyPDF**: A separação de páginas com `PyPDF` levou 0.53 segundos, usando 80.70 MB de memória.
- **PyMuPDF**: O `PyMuPDF` foi ligeiramente mais rápido, com 0.46 segundos, mas utilizou 94.04 MB, indicando que pode ser menos eficiente em termos de memória comparado ao `PyPDF`.

### 3. Merge Intercalado

| Biblioteca   | Tempo Total (50 Execuções)  | Memória Máxima (MB) |
|--------------|-----------------------------|---------------------|
| PyPDF        | 2.16 segundos               | 90.79 MB            |
| PyMuPDF      | 0.66 segundos               | 94.04 MB            |

#### Análise:
- **PyPDF**: O `PyPDF` teve um desempenho mais lento no merge intercalado, com 2.16 segundos, com uso de memória em 90.79 MB.
- **PyMuPDF**: Embora o `PyMuPDF` tenha sido significativamente mais rápido com 0.66 segundos, a memória utilizada foi a maior entre as bibliotecas, 94.04 MB.

---

## 🔍 Considerações e Conclusões

1. **Desempenho e Eficiência:**
   - **Extração de Texto:** `PyMuPDF` oferece o melhor desempenho em termos de tempo, mas com um maior uso de memória. Se a prioridade é a velocidade, `PyMuPDF` é a melhor escolha.
   - **Separação de Páginas:** `PyMuPDF` também é mais eficiente em termos de tempo, mas com um maior custo de memória. Se a eficiência de tempo é essencial, `PyMuPDF` é preferível.
   - **Merge Intercalado:** `PyMuPDF` supera `PyPDF` em velocidade, o que é vantajoso para operações de merge. O aumento no uso de memória deve ser considerado, mas a diferença de tempo é significativa.

2. **Uso de Memória:**
   - **Pdfplumber** apresenta o menor uso de memória para a extração de texto, tornando-o adequado para ambientes com recursos limitados.
   - **PyPDF** é mais eficiente em termos de memória para a separação de páginas, oferecendo uma boa relação entre tempo e consumo de memória.

3. **Escolha da Biblioteca:**
   - **Para desempenho máximo e menor tempo de processamento:** `PyMuPDF` é a escolha recomendada.
   - **Para menor consumo de memória e maior eficiência em ambientes restritos:** `Pdfplumber` e `PyPDF` podem ser mais apropriados, dependendo da tarefa específica.

## 📝 Recomendações

A rapidez não é o único critério para a escolha de uma biblioteca. É fundamental considerar também a complexidade da API e a facilidade de uso. Uma biblioteca pode ser mais rápida, mas se sua API for difícil de usar, isso pode não compensar a vantagem de desempenho. Além disso, a precisão da extração de texto e a capacidade de lidar com PDFs complexos são aspectos importantes a serem avaliados para garantir a adequação da biblioteca ao seu projeto.



---

Para mais detalhes, consulte o [arquivo de resultados completo](results/benchmark_results.txt).
