import streamlit as st
from edp_extractor import extrair_dados
from calculator import calcular_economia
from pdf_generator import gerar_pdf

st.set_page_config(page_title="GreenFlex - Análise de Fatura", layout="centered")
st.title("GreenFlex - Análise de Fatura EDP")

uploaded_file = st.file_uploader("📎 Envie sua fatura EDP (PDF)", type="pdf")

if uploaded_file:
    dados = extrair_dados(uploaded_file)
    st.success("✅ Dados extraídos com sucesso!")
    st.write("### 📄 Dados da Fatura:")
    st.json(dados)

    economia = calcular_economia(dados)
    st.metric("💰 Economia estimada", f"R$ {economia['economia_reais']:.2f}")

    st.write("### 📥 Gerar nova fatura personalizada:")
    pdf_file = gerar_pdf(dados, economia)

    st.download_button(
        label="📄 Baixar fatura personalizada",
        data=pdf_file,
        file_name="fatura_greenflex.pdf",
        mime="application/pdf"
    )
