import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv('dashcongresso.csv')

st.set_page_config(layout='wide')
st.title ('Dash Congressos CENAT Junho - 2025')

 # Lista dos congressos 
lista_dos_congressos = sorted(df['Congressos'].unique().tolist())

# Filtro

congresso_escolhido = st.sidebar.selectbox('Selecione o congresso', lista_dos_congressos)


# Filtrar os dados

dados_filtrados = df[df['Congressos'] == congresso_escolhido]

# Exibir tabela

st.dataframe(dados_filtrados)

# Subheader

st.subheader(f'Dados do Congresso: {congresso_escolhido}')

#parte estética do projeto:

# Preparar dados para gráfico
dados_grafico = dados_filtrados.melt(
    id_vars=['Congressos'],
    value_vars=['Meta', 'vendas'],
    var_name='Métrica',
    value_name='Valor'
)

# Gráfico de barras com cores personalizadas
grafico = alt.Chart(dados_grafico).mark_bar().encode(
    x=alt.X('Métrica:N', title='Métrica'),
    y=alt.Y('Valor:Q', title='Valor'),
    color=alt.Color('Métrica:N', scale=alt.Scale(
        domain=['Meta', 'vendas'],
        range=["#287BB2", "#2B8141", "#CE8808"]  
    ))
)
st.altair_chart(grafico, use_container_width=True)