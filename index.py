from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings,ChatOllama

# Load and split the PDF
loader = PyPDFLoader("health_insurance.pdf")
pages_content = loader.load_and_split()

# Embed using Ollama
embeddings = OllamaEmbeddings(model="llama2")
#db = FAISS.from_documents(pages_content, embeddings)

# Save to disk
#db.save_local("faiss_index")

# Load back with deserialization warning bypassed
new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

query = "What is covered under the SBI Health Insurance Policy?"
# docs =new_db.similarity_search(query)
# print(docs)

# Use Ollama's LLaMA 2 for chat completion
llm = ChatOllama(model="llama2")  

# Set up Retrieval QA
from langchain.chains import RetrievalQA  
qa_chain = RetrievalQA.from_chain_type(llm, retriever=new_db.as_retriever())

# Ask a question
query = "What is covered under the SBI Health Insurance Policy?"

def ask(user_query):
    res = qa_chain({"query": user_query})
    print(res["result"])
    return res["result"]

