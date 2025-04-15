# 📈 Seaborn & Streamlit - Análise de Criptomoedas

Este projeto utiliza **Streamlit** para criar uma aplicação interativa que permite a análise de dados históricos de criptomoedas, incluindo **BTC**, **SOL**, **ETH** e **USDT**. Através de **Seaborn** e **Matplotlib**, os dados são visualizados de maneira dinâmica e interativa, permitindo que usuários explorem a evolução dos preços e a volatilidade ao longo do tempo.

---

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Para criar uma aplicação interativa de visualização de dados.
- **Seaborn**: Para criar gráficos e visualizações estatísticas.
- **Pandas**: Para manipulação e transformação dos dados.
- **Matplotlib**: Para customização de gráficos.
- **Python**: Para processamento de dados e execução dos scripts.

---

## 📂 Estrutura de Pastas

Seaborn&Streamlit / ├── A5_VD_Seaborn&Streamlit.ipynb # Notebook com a análise e visualizações 
                    ├── app.py # Aplicação Streamlit 
                    ├── BTC.csv # Dados históricos de BTC 
                    ├── ETH.csv # Dados históricos de ETH 
                    ├── SOL.csv # Dados históricos de SOL 
                    ├── USDT.csv # Dados históricos de USDT 
                    └── Outros arquivos de análise # Scripts adicionais e arquivos relacionados


---

## 🔄 Fluxo do Projeto

1. **ETL dos Dados**: Os dados de cada criptomoeda (BTC, SOL, ETH, USDT) são carregados, transformados e concatenados em um único DataFrame.
   
2. **Análise Exploratória**: Visualizações são feitas utilizando **Seaborn** para identificar padrões de preços e volatilidade, com gráficos de linha, boxplot, e histograma.

3. **Aplicação Interativa**: Usando **Streamlit**, a aplicação permite que o usuário selecione a moeda e o ano desejado para análise, visualizando gráficos dinâmicos de evolução de preços, volatilidade e correlação entre variáveis.

---

## 🚀 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seaborn-streamlit-crypto-analysis.git

2. **Instale as dependências:**:
   pip install -r requirements.txt
3. **Execute o app Streamlit:**:
   streamlit run app.py

## 📝 Conclusão
Através dessa análise, conseguimos identificar os padrões de comportamento das criptomoedas selecionadas, como o preço de fechamento e a volatilidade diária. A aplicação interativa desenvolvida com Streamlit torna mais fácil para os investidores explorar os dados e tomar decisões informadas.

As visualizações criadas permitem uma compreensão clara das flutuações dos preços e da volatilidade, ajudando na identificação de tendências, correlações e padrões de risco.