import streamlit as st

st.set_page_config(page_title="Página de Olá", layout="centered")

# Título principal
st.title("👋 Olá!")

# Mensagem de boas-vindas
st.write("## Bem-vindo ao nosso aplicativo Streamlit!")

st.write("""
Esta é uma página de saudação simples.

### 🎉 Olá, mundo!

Obrigado por visitar nossa aplicação.
""")

# Adiciona uma imagem de boas-vindas (emoji)
st.markdown("# 😊")

# Mensagem adicional
st.info("Esta é uma página de demonstração criada com Streamlit.")
