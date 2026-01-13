import streamlit as st
from rag_core import responder

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="CH | ASTREIN",
    page_icon="📄",
    layout="wide"
)

# =========================
# ESTADO DA SESSÃO
# =========================
if "historico" not in st.session_state:
    st.session_state.historico = []

# =========================
# HEADER
# =========================
st.title("📄 Assistente Inteligente de Documentos")

# =========================
# SENHAS POR SETOR
# =========================
setores = ['Diretoria']
pass_diretoria = '12345'
pass_helpdesk = 'ch'
# =========================
# AUTENTICAÇÃO POR SENHA
# =========================
st.sidebar.title("🧭 Menu de Setores")
setor = st.sidebar.radio("Escolha o setor:", setores)

st.subheader(f"🔑 Acesso ao setor {setor}")
senha = st.text_input("Digite a senha:", type="password")

if setor == 'Diretoria'and senha == pass_diretoria:
    st.success("✅ Acesso liberado!")
    st.divider()
    st.write("📂 Informações disponíveis:")
    st.markdown(
    """
    Consulte documentos internos (PDF e Word) de forma segura.

    - 🔍 Busca semântica  
    - 🧠 Memória de conversa  
    - 🔐 Dados locais  
        """
    )
    # =========================
    # INPUT DO USUÁRIO
    # =========================

    pergunta = st.text_input( "Digite sua pergunta:", placeholder=" 🔍 " )
    col1, col2 = st.columns(2)

    with col1:
        enviar = st.button("📤 Enviar")

    with col2:
        limpar = st.button("🧹 Limpar Histórico")

    # =========================
    # AÇÕES
    # =========================
    if limpar:
        resposta = responder("limpar")
        st.session_state.historico = []
        st.success(resposta)

    if enviar and pergunta:
        with st.spinner("🔍 Consultando documentos..."):
            resposta = responder(pergunta)

        st.session_state.historico.append(
            {"pergunta": pergunta, "resposta": resposta}
        )

    # =========================
    # HISTÓRICO
    # =========================
    st.divider()
    st.subheader("🧠 Histórico da Conversa")

    for item in reversed(st.session_state.historico):
        st.markdown(f"**📋 Resposta:**\n{item['resposta']}")
        st.markdown("---")

else:
    if senha != "":
        st.error("❌ Senha incorreta ou acesso não autorizado.")
    st.warning("🔐 Digite a senha correta para liberar o ambiente.")

# ====================================================================================================

if setor == 'Suporte HelpDesk'and senha == pass_helpdesk:
    st.success("✅ Acesso liberado!")
    st.divider()
    st.write("📂 Informações disponíveis:")
    st.markdown(
    """
    Consulte documentos internos (PDF e Word) de forma segura.

    - 🔍 Busca SQL  
    - 🧠 Lógica de programação  
    - 🔐 Dados locais  
        """
    )
    # =========================
    # INPUT DO USUÁRIO
    # =========================

    pergunta = st.text_input( "Digite sua pergunta:", placeholder=" 🔍 " )
    col1, col2 = st.columns(2)

    with col1:
        enviar = st.button("📤 Enviar")

    with col2:
        limpar = st.button("🧹 Limpar Histórico")
