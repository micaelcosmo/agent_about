from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = os.getenv('BASE_DIR')
DB_DIR = os.getenv('DB_DIR')

def create_db():
    documents = load_documents()
    chunks = split_chunks(documents=documents)
    vectorize_chunks(chunks)
    print("Banco de dados vetorial criado com sucesso!")

def load_documents():
    _loader = PyPDFDirectoryLoader(BASE_DIR, glob="*.pdf")
    documents = _loader.load()
    return documents

def split_chunks(documents):
    document_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True
    )
    chunks = document_splitter.split_documents(documents=documents)
    return chunks

def vectorize_chunks(chunks):
    # Utilizando um modelo open-source e gratuito que roda localmente
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    db = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings_model, 
        persist_directory=DB_DIR
    )

if __name__ == "__main__":
    create_db()