from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from docloader import load_documents
from splitter import split_documents
from embeddings import create_vectorstore
from retriever import get_retriever
from main import build_qa_chain


# UI Design

st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #0B1D2A;  /* deep navy blue */
    color: #E6EDF3;
}

/* Main container */
.main {
    background-color: #0B1D2A;
}

/* Input box */
.stTextInput > div > div > input {
    background-color: #132F4C;
    color: #E6EDF3;
    border: 1px solid #1F4E79;
    border-radius: 10px;
    padding: 10px;
}

/* Chat bubbles */
.user-msg {
    background-color: #1F4E79;  /* blue */
    color: #FFFFFF;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.bot-msg {
    background-color: #132F4C;  /* darker blue */
    color: #E6EDF3;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

/* Buttons */
.stButton button {
    background-color: #2E86C1;
    color: white;
    border-radius: 8px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0E2A3D;
}

/* Headers */
h1, h2, h3 {
    color: #4FC3F7;
}

/* Subtext */
p {
    color: #A9C0D9;
}

</style>
""", unsafe_allow_html=True)

#UI Design

#st.title("📄 Smart RAG Chatbot")

#st.title(" Smart RAG Chatbot")

st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>
📄 Smart RAG Chatbot
</h1>
<p style='text-align: center; color: gray;'>
Ask questions from your documents with AI-powered retrieval
</p>
""", unsafe_allow_html=True)

@st.cache_resource
def setup_pipeline():
    docs = load_documents()
    chunks = split_documents(docs)
    db = create_vectorstore(chunks)
    retriever = get_retriever(db)
    return build_qa_chain(retriever)

qa_chain = setup_pipeline()

query = st.text_input("Ask a question:")

if query:
    result = qa_chain(query)

    st.write("### Answer:")
    st.write(result["result"])



