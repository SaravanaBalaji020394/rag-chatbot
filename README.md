# 💬 Smart RAG Chatbot

An end-to-end **Retrieval-Augmented Generation (RAG)** chatbot that enables users to ask questions from their documents and receive **context-aware, accurate, and grounded responses**.

This project demonstrates how Large Language Models (LLMs) can be enhanced with external knowledge using vector search to reduce hallucination and improve reliability.

---

## 🚀 Key Highlights

- 🔍 Semantic search using embeddings
- 🧠 Context-aware responses using LLM
- 📄 Supports PDF-based knowledge retrieval
- ⚡ Built with modular and scalable architecture
- 💬 Interactive chat interface using Streamlit
- 📉 Reduces hallucination by grounding responses in source documents

---

## 🧱 Tech Stack

- **Python**
- **LangChain** – Orchestration framework
- **OpenAI API** – Embeddings & LLM
- **FAISS** – Vector database for similarity search
- **Streamlit** – Interactive UI

---

## 🧠 System Architecture

### 📄 Document Processing (Offline)
1. Load PDF documents
2. Split into meaningful text chunks
3. Convert chunks into vector embeddings
4. Store embeddings in FAISS vector database

### ❓ Query Processing (Runtime)
1. User inputs a question
2. Convert query into embedding
3. Perform similarity search in FAISS
4. Retrieve top relevant chunks
5. Pass context + query to LLM
6. Generate final grounded response

---

## 🔄 End-to-End Flow
