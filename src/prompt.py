prompt_template="""
<<<<<<< HEAD
Use the following pieces of information to answer the user's question you are medical assistent.
=======
Use the following pieces of information to answer the user's question.
>>>>>>> origin/main
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""