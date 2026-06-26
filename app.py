import streamlit as st
from crew import run_crew

st.set_page_config(
    page_title="Análise de Mercado",
    page_icon="📊",
    layout="wide"
)

st.title("Agente de Análise de Mercado")
st.write("Digite um setor e o agente irá gerar uma análise completa.")

sector = st.text_input(
    "Setor",
    placeholder="Ex: Inteligência Artificial"
)

if st.button("Gerar análise"):
    if sector:
        with st.spinner("Executando agentes... isso pode levar alguns minutos."):
            resultado = run_crew(sector)
        st.success("Análise concluída!")
        st.markdown(resultado)
    else:
        st.warning("Digite um setor.")