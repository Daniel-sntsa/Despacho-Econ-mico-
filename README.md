# ⚡ Otimização de Custo de Geração de Energia  

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)  
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-orange.svg?logo=numpy&logoColor=white)](https://numpy.org/)  
[![SciPy](https://img.shields.io/badge/SciPy-1.10+-green.svg?logo=scipy&logoColor=white)](https://scipy.org/)  
[![Tabulate](https://img.shields.io/badge/Tabulate-Library-yellow.svg)](https://pypi.org/project/tabulate/)  
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Optional-lightblue.svg?logo=plotly&logoColor=white)](https://matplotlib.org/)

Este projeto implementa um algoritmo para **otimizar o custo total de geração de energia elétrica** utilizando o método `SLSQP` do SciPy.  
Ele considera **funções de custo quadráticas**, **perdas de transmissão**, **limites de geração** e calcula parâmetros como **potências ótimas, custos marginais (λ) e perdas**.

---

## 🚀 Funcionalidades
- ✅ Cálculo do **custo mínimo** de geração atendendo restrições de demanda  
- ✅ Consideração de **perdas nas linhas de transmissão**  
- ✅ Suporte a **limites mínimos e máximos** de potência para cada gerador  
- ✅ Cálculo de **λ (lambda)** para análise econômica (Custo Incremental) 
- ✅ Separação clara entre **funções reutilizáveis** e **códigos de teste**

---

## 📂 Estrutura do Projeto
```
📦 otimizacao-energia
 ┣ 📜 funcoes_otimizacao.py    # Módulo com as funções principais
 ┣ 📜 teste_otimizacao.py      # Script de testes e exemplos de uso
 ┗ 📜 README.md                # Documentação do projeto
```

---

## 🛠️ Tecnologias Utilizadas
- 🐍 **Python 3.8+**
- 📦 **NumPy** – operações numéricas
- 📦 **SciPy** – otimização numérica
- 📦 **Tabulate** – exibição de resultados em tabelas
- 📦 **Matplotlib** *(opcional, para gráficos futuros)*

---

## 📥 Instalação e Uso

1. Clone este repositório:
   ```bash
   git clone https://github.com/Daniel-sntsa/otimizacao-energia.git
   cd otimizacao-energia
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # Windows
   source venv/bin/activate     # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install numpy scipy tabulate matplotlib
   ```

4. Execute os testes:
   ```bash
   python teste_otimizacao.py
   ```

---

## 📊 Exemplo de Saída
```
===== RESULTADO PARA DEMANDA 200 =====
+---------+----------------+-------------+-----------+----------------------+
| Gerador | Potência (MW)  | Perdas (MW) | Custo (R$)| Custo Marginal (R$/MWh)|
+---------+----------------+-------------+-----------+----------------------+
| Gerador 1 | 80.0          | 0.0         | 2000.0    | 9.5                  |
| Gerador 2 | 70.0          | 0.0         | 1800.0    | 10.2                 |
| Gerador 3 | 50.0          | 0.0         | 1600.0    | 8.7                  |
| TOTAL     | 200.0         | 0.0         | 5400.0    | -                    |
+---------+----------------+-------------+-----------+----------------------+

Lambda Geração Mínima: [8.5, 9.1, 7.8]  
Lambda Geração Máxima: [12.3, 13.0, 11.5]  

Potências calculadas para λ mínimo: [80.0, 70.0, 50.0]
```

---

## 🔥 Próximos Passos
- [ ] Implementar **gráficos** da curva de custo e pontos ótimos  
- [ ] Adicionar **interface gráfica** simples para entrada de dados  
- [ ] Suporte para **mais tipos de funções de custo**  

---

## 👤 Autores
**Daniel dos Santos Amador**
**Pedro Nogueira Feijó**
**Rafael Nunes de Souza Lourenço Vieira**

📌 *Engenharia Elétrica* | *Computação Aplicada*  
🔗 [GitHub](https://github.com/Daniel-sntsa)  
