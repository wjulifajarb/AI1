import os
import streamlit as st
from PyPDF2 import PdfReader
from nltk import sent_tokenize
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

st.set_page_config(page_title="chatbot con PDF", layout="wide")
st.markdown("""<style>.block-container {padding_top: 1rem;}</style>""", unsafe_allow_html=True)

# set OpenAI API key
OPENAI_API_KEY = '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'
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

@st.cache(suppress_st_warning=True)
def create_embeddings(pdf):
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extractText()

        # Utilizar nltk para dividir el texto en oraciones
        chunks = sent_tokenize(text)

        embeddings = OpenAIEmbeddings()
        # No se utiliza langchain.vectors

        return embeddings

st.sidebar.markdown("<h1 style='text-align: center; color: #176887;'>Cargar Archivo PDF</h1>", unsafe_allow_html=True)
st.sidebar.write("Carga el archivo PDF con el cual quieres interactuar")

pdf_doc = st.sidebar.file_uploader("", type="pdf")

st.sidebar.write("---")

if pdf_doc is not None:
    embeddings_pdf = create_embeddings(pdf_doc)
    st.write("Embeddings creados exitosamente.")
else:
    st.warning("Por favor, carga un archivo PDF.")

response_container = st.container()
textcontainer = st.container()

if 'requests' not in st.session_state:
    st.session_state.requests = []
    st.session_state.responses = []

with textcontainer:
    with st.form(key='my_form'):
       query = st.text_area("Tu:")
       submit_button = st.form_submit_button(label='Enviar')
    
    if query:
        with st.spinner("escribiendo..."):

            docs = embeddings_pdf.similarity_search(query)
            llm = OpenAI(model_name="text-davinci-003")
            chain = load_qa_chain(llm, chain_type="stuff")

            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)

        st.session_state.requests.append(query)
        st.session_state.responses.append(response)

with response_container:
    if st.session_state.responses:
        for i in range(len(st.session_state.responses)):
            st.text(f"Bot: {st.session_state.responses[i]}")
            if i < len(st.session_state.requests):
                st.text(f"Usuario: {st.session_state.requests[i]}")
