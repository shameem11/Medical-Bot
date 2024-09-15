
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from src.prompt import prompt_template
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from src.loader import download_hugging_face_embeddings
from flask import Flask,render_template,jsonify, request


app = Flask(__name__)

# Prompt and LLM setup
embedding_model = download_hugging_face_embeddings()
vector_store = FAISS.load_local("FAISS_index", embedding_model)

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(
    model="Model\llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={'max_new_tokens': 512,'temperature': 0.8}
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

@app.route("/")
def index():
    return render_template('bot.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)