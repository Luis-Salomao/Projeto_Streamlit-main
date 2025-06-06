import streamlit as st
import pandas as pd
import plotly.express as px

# Carregando os dados
dados = pd.read_excel('Vendas_Base_de_Dados.xlsx')

# Calcula o faturamento em cada linha
dados['Faturamento'] = dados['Quantidade'] * dados['Valor Unitário']

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("📊 Dashboard de Faturamento")

# Sidebar com filtros
st.sidebar.header("Filtros")

# Opção "Todos" para lojas
lojas = ['Todos'] + sorted(dados['Loja'].unique())
loja_escolhida = st.sidebar.selectbox('Escolha o estado:', lojas)

# Produtos filtrados pela loja escolhida (ou todos)
if loja_escolhida == 'Todos':
    produtos = ['Todos'] + sorted(dados['Produto'].unique())
else:
    produtos = ['Todos'] + sorted(dados[dados['Loja'] == loja_escolhida]['Produto'].unique())

produto_escolhido = st.sidebar.selectbox('Escolha o produto:', produtos)

# Filtrar os dados conforme a escolha
if loja_escolhida == 'Todos' and produto_escolhido == 'Todos':
    dados_filtrados = dados.copy()
elif loja_escolhida == 'Todos':
    dados_filtrados = dados[dados['Produto'] == produto_escolhido]
elif produto_escolhido == 'Todos':
    dados_filtrados = dados[dados['Loja'] == loja_escolhida]
else:
    dados_filtrados = dados[(dados['Loja'] == loja_escolhida) & (dados['Produto'] == produto_escolhido)]

# Faturamento total da seleção
faturamento_total = dados_filtrados['Faturamento'].sum()
st.metric(label="💰 Faturamento Total", value=f"R$ {faturamento_total:,.2f}")

# Gráfico de pizza com todos os produtos da loja escolhida (ou todos)
if loja_escolhida == 'Todos':
    dados_grafico = dados_filtrados.groupby('Produto')['Faturamento'].sum().reset_index()
    titulo_grafico = 'Participação dos Produtos no Faturamento Geral'
else:
    dados_grafico = dados[dados['Loja'] == loja_escolhida].groupby('Produto')['Faturamento'].sum().reset_index()
    titulo_grafico = f'Participação dos Produtos no Faturamento da Loja {loja_escolhida}'

fig_pizza = px.pie(dados_grafico, names='Produto', values='Faturamento', title=titulo_grafico)
st.plotly_chart(fig_pizza)

# Texto de resumo
st.write(f"🛍️ Faturamento total para a seleção atual é **R$ {faturamento_total:,.2f}**.")

# Exibir dados filtrados
with st.expander("📋 Ver dados detalhados da seleção"):
    st.dataframe(dados_filtrados)
