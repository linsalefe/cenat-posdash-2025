import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv('posdash.csv')

st.set_page_config(layout='wide')
st. title('Dash Pós Graduação CENAT 2025')

st.dataframe(df)

lista_de_pos = sorted(df['Pós - graduação'].unique().tolist())

# mecanismo para selecionar as pós

pos_escolhida = st.selectbox('Selecione a Pós:', lista_de_pos) 

# Para filtrar os dados da pós escolhida

dados_filtrados = df[df['Pós - graduação']== pos_escolhida]

#exibir tabela

st.dataframe(dados_filtrados)

#para exibir os dados de barras com os dados

st.subheader(f'Dados da Pós: {pos_escolhida}')
st.bar_chart(dados_filtrados[['Meta', 'MQL', 'Valor investido', 'CPL']])




