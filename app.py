import streamlit as st
from api_chatpdf import upload_pdf, ask_question

st.title("📄 ChatPDF Interativo")

# Inicializa o estado da sessão
if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload do PDF
uploaded_file = st.file_uploader("Carregue seu PDF", type=["pdf"])

if uploaded_file and not st.session_state.pdf_uploaded:
    with st.spinner("Processando PDF..."):
        try:
            st.session_state.source_id = upload_pdf(uploaded_file)
            st.session_state.pdf_uploaded = True
            st.success("PDF pronto para perguntas!")
        except Exception as e:
            st.error(f"Erro: {e}")

# Chat
if st.session_state.pdf_uploaded:
    question = st.chat_input("Faça uma pergunta sobre o PDF...")
    
    if question:
        with st.spinner("Pensando..."):
            try:
                answer = ask_question(st.session_state.source_id, question)
                st.session_state.chat_history.append({"pergunta": question, "resposta": answer})
            except Exception as e:
                st.error(f"Erro na resposta: {e}")

        # Exibir histórico
        for chat in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(chat["pergunta"])
            with st.chat_message("assistant"):
                st.write(chat["resposta"])