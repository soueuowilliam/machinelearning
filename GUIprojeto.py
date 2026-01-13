import streamlit as st
import os
from rag.chain import get_qa_chain

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

st.set_page_config("RAG Gemini", layout="wide")

st.title("📄 Chat com seus Documentos")

qa = get_qa_chain()

pergunta = st.text_input("Pergunte algo:")

if pergunta:
    with st.spinner("Pensando..."):
        resposta = qa.invoke({"query": pergunta})
        st.write(resposta["result"])
