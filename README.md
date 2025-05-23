

```markdown
# 🧠 AI-Powered Insurance Policy Information Chatbot

This project is an AI-powered chatbot designed to assist users with queries related to various insurance policies such as health, life, auto, and home insurance. It uses natural language processing to provide accurate, instant, and relevant responses extracted from a PDF-based knowledge base.

---

## 📌 Problem Statement

Customers often struggle to understand the details of insurance policies — including coverage, premiums, and claims. Providing timely and accurate answers is crucial for customer satisfaction.

---

## 🎯 Objective

To develop a chatbot that:
- Understands natural language queries.
- Retrieves relevant information from an insurance policy PDF.
- Provides helpful, human-like responses.
- Can be embedded into websites or apps for real-time support.

---

## ⚙️ Tech Stack

| Component        | Technology                 |
|------------------|-----------------------------|
| Language Model   | LLaMA 2 via Ollama          |
| Vector Store     | FAISS (for similarity search) |
| Embeddings       | Ollama Embeddings           |
| Document Parsing | LangChain + PyPDFLoader     |
| Frontend UI      | Streamlit                   |
| Backend Logic    | Python                      |

---

## 🔁 Workflow

1. **User Query** is submitted via the chatbot.
2. **FAISS** performs a similarity search on vectorized PDF chunks.
3. The most relevant chunks are passed to the **LLM (LLaMA 2)**.
4. The LLM generates a **contextual, user-friendly response**.

---

## 💻 How to Run the Project

### 1. Install Dependencies
```bash
pip install streamlit langchain langchain-community langchain-ollama faiss-cpu
```

### 2. Start Ollama and Pull Model
Make sure you have [Ollama](https://ollama.com/) installed and run:
```bash
ollama run llama2
```

### 3. Run the Streamlit App
```bash
streamlit run app.py
```

## 📄 Features

- 🔍 Natural Language Query Understanding
- 📚 PDF-based Knowledge Base Integration
- 🤖 Smart Answers using LLaMA 2
- 💬 Chat History with Stylish UI
- 🧠 RetrievalQA with FAISS for Contextual Relevance

---

## 📽️ Demo

> 🎥 A video demonstration with voiceover is available in the `demo/` folder (or shared separately).

---

## 📁 Project Structure

```
.
├── app.py              # Streamlit UI
├── index.py            # LLM + FAISS Logic
├── health_insurance.pdf # Knowledge Base
├── faiss_index/        # Vector store directory
└── README.md           # Project Overview
```



