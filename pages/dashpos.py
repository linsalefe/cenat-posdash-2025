import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv('posdash.csv')

st.set_page_config(layout='wide')
st.title('Dash Pós Graduação CENAT 2025')

# Lista de Pós
lista_de_pos = sorted(df['Pós - graduação'].unique().tolist())

# Filtro
pos_escolhida = st.sidebar.selectbox('Selecione a Pós:', lista_de_pos)

# Filtrar os dados
dados_filtrados = df[df['Pós - graduação'] == pos_escolhida]

# Exibir tabela
st.dataframe(dados_filtrados)

# Subheader
st.subheader(f'Dados da Pós: {pos_escolhida}')

#parte estética do projeto:

# Preparar dados para gráfico
dados_grafico = dados_filtrados.melt(
    id_vars=['Pós - graduação'],
    value_vars=['Meta', 'MQL', 'CPL'],
    var_name='Métrica',
    value_name='Valor'
)

# Gráfico de barras com cores personalizadas
grafico = alt.Chart(dados_grafico).mark_bar().encode(
    x=alt.X('Métrica:N', title='Métrica'),
    y=alt.Y('Valor:Q', title='Valor'),
    color=alt.Color('Métrica:N', scale=alt.Scale(
        domain=['Meta', 'MQL', 'CPL'],
        range=["#1F8F23", '#2196F3', '#FF9800']  # Cores: verde, azul, laranja
    ))
)
st.altair_chart(grafico, use_container_width=True)
