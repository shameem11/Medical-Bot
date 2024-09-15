from langchain.document_loaders import PyMuPDFLoader,DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
# this funtion for Load pdf 

def load_pdf(data):
   loader = DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)
   doc = loader.load()
   return doc



#text split 
def text_split_chunks(documents, chunk_size=500, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks 



#download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings


def store_in_faiss_vector_db(pdf_chunks,embedding_model, index_path):

