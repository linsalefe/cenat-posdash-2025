import streamlit as st
from PIL import Image

st.set_page_config(page_title="Dash Tráfego Pago", layout="wide")

# Título centralizado e estilizado
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1 style='font-size: 3em; color: #00BFFF;'>📊 Indicadores de Tráfego Pago - CENAT 2025</h1>
        <h3 style='color: #AAAAAA;'>Monitoramento de resultados e metas dos projetos em andamento</h3>
    </div>
""", unsafe_allow_html=True)

# Inserir uma imagem ilustrativa (se quiser)
# Exemplo: se tiver uma imagem "cenat_banner.png" na pasta raiz
# image = Image.open('cenat_banner.png')
# st.image(image, use_column_width=True)

# Separador de seção
st.markdown("<hr style='border:1px solid #444;'>", unsafe_allow_html=True)

# Instrução ao usuário
st.markdown("""
    <div style='text-align: center; font-size: 1.2em; color: #FFFFFF;'>
        👉 Selecione um dashboard no menu lateral esquerdo para começar a análise.
    </div>
""", unsafe_allow_html=True)

# Espaçamento final
st.markdown("<br><br>", unsafe_allow_html=True)
