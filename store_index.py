from src.loader import store_in_faiss_vector_db, text_split_chunks, download_hugging_face_embeddings, load_pdf

import os 
from src.loader import load_pdf,text_split_chunks,download_hugging_face_embeddings,store_in_faiss_vector_db


pdf_directory = "C:/Users/shame/OneDrive/Documents/GitHub/Medical-Bot/Data/"  
pdf_documents = load_pdf(pdf_directory)

pdf_chunks = text_split_chunks(pdf_documents)
embedding_model = download_hugging_face_embeddings()
index_path = "FAISS_index"
vector_store = store_in_faiss_vector_db(pdf_chunks, embedding_model, index_path)


