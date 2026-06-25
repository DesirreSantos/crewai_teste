import streamlit as st
import asyncio


st.set_page_config(
    page_title="Análise de Mercado",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Agente de Análise de Mercado")

st.write(
    "Digite um setor e o agente irá gerar uma análise completa."
)


sector = st.text_input(
    "Setor",
    placeholder="Ex: Inteligência Artificial"
)


if st.button("Gerar análise"):

    if sector:

        with st.spinner("Executando agentes..."):

            resultado = asyncio.run(
                (sector)
            )

        st.success("Análise concluída!")

        st.markdown(resultado)

    else:

        st.warning("Digite um setor.")