from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embeddings
from langchain.chains import RetrievalQA
from rag.loader import load_documents
from rag.vectorstore import build_faiss
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embeddings



def get_embeddings():
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
from langchain.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
import os

def load_documents(folder="data"):
    docs = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
        elif file.endswith(".txt"):
            docs.extend(TextLoader(path).load())
        elif file.endswith(".docx"):
            docs.extend(Docx2txtLoader(path).load())

    return docs

def build_faiss(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(documents)

    db = FAISS.from_documents(chunks, get_embeddings())
    db.save_local("faiss_index")

docs = load_documents("data")
build_faiss(docs)

print("FAISS criado com sucesso")

def get_qa_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0
    )

    db = FAISS.load_local("faiss_index", get_embeddings(), allow_dangerous_deserialization=True)

    retriever = db.as_retriever(search_kwargs={"k": 4})

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
