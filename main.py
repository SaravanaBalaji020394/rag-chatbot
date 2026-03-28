from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer ONLY using the provided context.

    If the answer is not in the context, say:
    "I don't know based on the document."

    Context:
    {context}

    Question:
    {question}
    """,
    input_variables=["context", "question"]
)

def build_qa_chain(retriever):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain