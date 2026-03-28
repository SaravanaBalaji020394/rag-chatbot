import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders import PyPDFLoader
print('ok')


import os

def load_documents(data_path="."):
    documents = []
    
    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(data_path, file))
            documents.extend(loader.load())
    
    return documents

documents = load_documents()

print(f"Total pages loaded: {len(documents)}\n")