import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
btc = pd.read_csv('BTC.csv')
sol = pd.read_csv('SOL.csv')
eth = pd.read_csv('ETH.csv')
usdt = pd.read_csv('USDT.csv')

# Preparar os dados
btc['date'] = pd.to_datetime(btc['date'])
sol['date'] = pd.to_datetime(sol['date'])
eth['date'] = pd.to_datetime(eth['date'])
usdt['date'] = pd.to_datetime(usdt['date'])

btc['coin'] = 'BTC'
sol['coin'] = 'SOL'
eth['coin'] = 'ETH'
usdt['coin'] = 'USDT'

df = pd.concat([btc, sol, eth, usdt])
df.sort_values(by='date', inplace=True)
df['volatilidade'] = df['high'] - df['low']

# Sidebar com seleção de moedas
moeda = st.sidebar.selectbox('💱 Escolha a Moeda:', ['BTC', 'SOL', 'ETH', 'USDT'])
dados = df[df['coin'] == moeda].copy()

# Filtro de ano
ano_filtro = st.sidebar.selectbox('🔄 Selecione o Ano:', sorted(df['date'].dt.year.unique(), reverse=True))
dados = dados[dados['date'].dt.year == ano_filtro]

st.sidebar.markdown(f"**Período:** {dados['date'].min().date()} → {dados['date'].max().date()}")
st.sidebar.markdown(f"**Total de Registros:** {dados.shape[0]}")

# Gráfico 1 - Preço de Fechamento
st.subheader(f'📉 Evolução do Preço de Fechamento - {moeda} ({ano_filtro})')
fig1, ax1 = plt.subplots(figsize=(12, 4))
sns.lineplot(data=dados, x='date', y='close', ax=ax1)
ax1.set_ylabel('Preço de Fechamento (USD)')
st.pyplot(fig1)

st.markdown("""
*Este gráfico apresenta a evolução do preço de fechamento da moeda ao longo do tempo. 
Ele permite observar as tendências de alta ou queda nos preços e identificar períodos de maior volatilidade.*
""")

# Gráfico 2 - Volatilidade Diária
st.subheader(f'⚡ Volatilidade Diária (High - Low) - {moeda} ({ano_filtro})')
fig2, ax2 = plt.subplots(figsize=(12, 4))
sns.lineplot(data=dados, x='date', y='volatilidade', color='orange', ax=ax2)
ax2.set_ylabel('Volatilidade (USD)')
st.pyplot(fig2)

st.markdown("""
*Este gráfico mostra a volatilidade diária, calculada pela diferença entre o preço mais alto e o mais baixo do dia. 
Alta volatilidade pode indicar grande incerteza ou mudança nas tendências do mercado.*
""")

# Gráfico 3 - Correlação entre Abertura e Fechamento
st.subheader(f'🔗 Correlação Abertura vs Fechamento - {moeda} ({ano_filtro})')
fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=dados, x='open', y='close', ax=ax3)
ax3.set_xlabel('Abertura (USD)')
ax3.set_ylabel('Fechamento (USD)')
st.pyplot(fig3)

st.markdown("""
*Este gráfico de dispersão nos ajuda a entender como o preço de abertura se relaciona com o preço de fechamento. 
Uma forte correlação pode indicar que a moeda tem uma tendência de continuar sua trajetória durante o dia.*
""")

# Gráfico 4 - Média Móvel de 30 dias
st.subheader(f'📈 Média Móvel de 30 dias - {moeda} ({ano_filtro})')
dados['media_movel'] = dados['close'].rolling(window=30).mean()
fig4, ax4 = plt.subplots(figsize=(12, 4))
sns.lineplot(data=dados, x='date', y='close', label='Fechamento', ax=ax4)
sns.lineplot(data=dados, x='date', y='media_movel', label='Média Móvel (30d)', ax=ax4)
ax4.set_ylabel('USD')
ax4.legend()
st.pyplot(fig4)

st.markdown("""
*A média móvel de 30 dias ajuda a suavizar flutuações diárias, mostrando a tendência subjacente do preço da moeda. 
Isso é útil para identificar mudanças no padrão de preço mais gradual ao longo do tempo.*
""")

# Gráfico 5 - Distribuição da Volatilidade
st.subheader(f'🎻 Distribuição da Volatilidade - {moeda} ({ano_filtro})')
fig5, ax5 = plt.subplots(figsize=(6, 4))
sns.violinplot(data=dados, x='coin', y='volatilidade', ax=ax5)
ax5.set_ylabel('Volatilidade')
st.pyplot(fig5)

st.markdown("""
*O violinplot é útil para comparar a distribuição da volatilidade entre diferentes moedas. Ele também mostra a mediana, 
os quartis e a forma geral da distribuição dos dados.*
""")

# Gráfico 6 - Boxplot de Preços
st.subheader(f'📦 Boxplot dos Preços de Fechamento - {moeda} ({ano_filtro})')
fig6, ax6 = plt.subplots(figsize=(6, 4))
sns.boxplot(data=dados, y='close', ax=ax6)
ax6.set_ylabel('Fechamento (USD)')
st.pyplot(fig6)

st.markdown("""
*O boxplot nos ajuda a visualizar a dispersão dos preços de fechamento e identificar outliers, 
ou seja, dias em que os preços foram anormalmente altos ou baixos.*
""")

# Gráfico 7 - Histograma + KDE dos preços
st.subheader(f'📊 Distribuição dos Preços de Fechamento - {moeda} ({ano_filtro})')
fig7, ax7 = plt.subplots(figsize=(8, 4))
sns.histplot(dados['close'], kde=True, bins=50, ax=ax7)
ax7.set_xlabel('Fechamento (USD)')
st.pyplot(fig7)

st.markdown("""
*Este histograma com a linha de densidade nos mostra a distribuição dos preços de fechamento. 
Pode ser útil para verificar a tendência central e a dispersão dos preços.*
""")

# Gráfico 8 - Heatmap de Correlação
st.subheader(f'🧪 Correlação entre Variáveis - {moeda} ({ano_filtro})')
fig8, ax8 = plt.subplots(figsize=(6, 4))
sns.heatmap(
    dados[['open', 'high', 'low', 'close', 'volatilidade']].corr(),
    annot=True, cmap='coolwarm', ax=ax8, fmt=".2f"
)
st.pyplot(fig8)

st.markdown("""
*Este heatmap mostra a correlação entre as principais variáveis, como o preço de abertura, fechamento e a volatilidade. 
Uma alta correlação entre duas variáveis indica que elas estão fortemente relacionadas.*
""")

# Conclusão do Notebook
st.markdown("---")
st.subheader("🔍 Conclusão")
st.markdown("""
A análise exploratória realizada mostrou como as criptomoedas BTC, SOL, ETH e USDT se comportam em termos de preços, volatilidade e outras variáveis importantes ao longo do tempo.

Com o uso de gráficos interativos, conseguimos explorar tendências, identificar períodos de alta volatilidade, e observar a relação entre os preços de abertura e fechamento. 

Através da **média móvel**, conseguimos suavizar os dados e visualizar tendências mais claras, enquanto o **boxplot** e o **violinplot** nos ajudaram a identificar outliers e entender melhor a distribuição dos dados.

Esses gráficos proporcionam uma visão clara e útil para investidores e analistas, permitindo tomar decisões mais informadas sobre os ativos.

Com a **selecção de anos** e a visualização dos dados para diferentes moedas, o aplicativo se torna uma ferramenta valiosa para a análise comparativa de diferentes criptomoedas.
""")