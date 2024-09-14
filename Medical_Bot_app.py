import streamlit as st
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from src.prompt import prompt_template
from langchain.chains import RetrievalQA
from src.loader import store_in_faiss_vector_db, text_split_chunks, download_hugging_face_embeddings, load_pdf
from langchain.vectorstores import FAISS

# Load your PDF data and process it
pdf_directory = "C:/Users/shame/OneDrive/Documents/GitHub/Medical-Bot/Data/"  
pdf_documents = load_pdf(pdf_directory)
pdf_chunks = text_split_chunks(pdf_documents)
embedding_model = download_hugging_face_embeddings()
index_path = "FAISS_index"
vector_store = store_in_faiss_vector_db(pdf_chunks, embedding_model, index_path)

# Prompt and LLM setup
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(
    model="D:/Medical-Bot/Model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={'max_new_tokens': 512, 'temperature': 0.8}
)

qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=vector_store.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs
)

# Custom CSS for design
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .stTextInput > div > input {
        border: 2px solid #007acc;
        border-radius: 5px;
        padding: 10px;
        color: #333;
    }
    .css-1v0mbdj {
        color: #007acc;
        font-size: 1.2em;
    }
    .stButton > button {
        background-color: #007acc;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Page layout
st.set_page_config(page_title="Medical Chatbot", page_icon="💡", layout="wide")

# Sidebar for App Info
with st.sidebar:
    st.title("🤖 Medical Chatbot")
    st.write("""
    This chatbot is designed to assist users with medical questions by providing answers based on a trained dataset.
    Simply type in your question, and the chatbot will analyze the data to provide an answer.
    """)
    st.image("https://image.shutterstock.com/image-vector/medical-assistance-bot-using-ai-600w-1713207452.jpg", use_column_width=True)
    st.markdown("---")
    st.markdown("Developed by **Mohammed Shameem**")

# Main content layout
st.markdown("<h2 style='text-align: center; color: #007acc;'>Medical Assistance Chatbot 💬</h2>", unsafe_allow_html=True)

st.write("""
This chatbot is designed to assist patients and medical professionals with quick, reliable answers to common medical questions.
Type your medical question below, and the chatbot will respond with an answer based on its medical dataset and training.
""")

# Text input for user's medical question
user_input = st.text_input("🔍 Type your medical question here:")

# Process the user's question
if user_input:
    with st.spinner("🤔 Analyzing your question..."):
        # Get answer from the LLM QA chain
        result = qa({"query": user_input})
        
        st.markdown(f"<h4 style='color: #007acc;'>🔍 Question:</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 1.1em; color: #333;'>{user_input}</p>", unsafe_allow_html=True)
        
        st.markdown(f"<h4 style='color: #007acc;'>💡 Answer:</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 1.1em; color: #333;'>{result['result']}</p>", unsafe_allow_html=True)
        
        st.markdown("---")

# Display some health tips (enhance user interaction)
st.subheader("💡 Quick Medical Tips")
tips = [
    "💧 Drink plenty of water to stay hydrated.",
    "🍎 Eat a balanced diet rich in fruits and vegetables.",
    "🚶‍♂️ Engage in at least 30 minutes of physical activity daily.",
    "😴 Get 7-8 hours of sleep every night.",
    "🧠 Mental health is just as important as physical health."
]
for tip in tips:
    st.write(tip)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Developed by Mohammed Shameem | © 2024</p>", unsafe_allow_html=True)
