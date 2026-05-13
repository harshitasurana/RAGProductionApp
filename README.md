# 🤖 Local RAG AI Assistant Platform  

Smart PDF Question-Answering System with Local LLMs, Semantic Search & Vector Database 🚀  
Making document understanding smarter, faster, and fully local ❤️  

---

# 🏷️ Badges

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Qdrant](https://img.shields.io/badge/VectorDB-Qdrant-red)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)
![Llama3](https://img.shields.io/badge/Model-Llama3-purple)
![Status](https://img.shields.io/badge/Status-Active-success)

---

# 🎥 Demo

<p align="center">
  <img src="assets/RAG.gif" width="900"/>
  <br>
  <b>Local RAG AI Assistant Demo</b>
</p>

---

# 🧠 Problem Statement  

Traditional document systems face several problems:

❌ Manual searching through PDFs  
❌ Slow information retrieval  
❌ No semantic understanding  
❌ Difficulty handling large documents  
❌ Expensive cloud AI APIs  

---

# 💡 Solution  

This project provides a **fully local AI-powered RAG (Retrieval-Augmented Generation) system** that:

✔ Allows users to upload PDFs  
✔ Converts documents into semantic embeddings  
✔ Stores vectors in Qdrant Vector Database  
✔ Retrieves relevant document chunks intelligently  
✔ Uses Llama3 to generate grounded answers  
✔ Runs completely locally without paid APIs  

---

# 🏗️ System Architecture  

Streamlit UI ↔ FastAPI + Inngest ↔ Qdrant Vector Database  
                                 ⬇  
                       Ollama + Llama3  
                                 ⬇  
                      Semantic AI Answers  

---

# ✨ Key Features  

## 🔥 Core Features  

✔ Upload and ingest PDFs  
✔ Intelligent semantic search  
✔ Local AI-powered question answering  
✔ Context-aware responses  
✔ Real-time vector retrieval  
✔ Source tracking & citations  

---

## 🧠 AI Features  

✔ Retrieval-Augmented Generation (RAG)  
✔ Local Llama3 integration  
✔ Embedding generation using nomic-embed-text  
✔ Chunk-based document indexing  
✔ Similarity search using cosine distance  

---

## ⚡ Workflow Features  

✔ Event-driven architecture using Inngest  
✔ Async document processing  
✔ Polling-based workflow tracking  
✔ Scalable ingestion pipeline  

---

## 🌐 Frontend Features  

✔ Modern Streamlit UI  
✔ ChatGPT-style chat interface  
✔ Sidebar dashboard  
✔ PDF upload system  
✔ Streaming AI responses  
✔ Source document display  

---

## 🔐 Backend Features  

✔ FastAPI-powered APIs  
✔ Modular code structure  
✔ Vector database integration  
✔ Local AI inference  
✔ Clean workflow orchestration  

---

# 🧪 Tech Stack  

| Layer | Technologies Used |
|------|------------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Workflow Engine | Inngest |
| Vector Database | Qdrant |
| LLM Runtime | Ollama |
| AI Model | Llama3 |
| Embedding Model | nomic-embed-text |
| PDF Processing | LlamaIndex |
| Language | Python |

---

# 📊 Performance & Design Highlights  

⚡ Fast semantic document retrieval  
🧠 Fully local AI inference (offline capable)  
📦 Modular & scalable architecture  
🔎 Accurate context retrieval using embeddings  
🎯 Clean ChatGPT-style user experience  

---

# ⚙️ Installation  

## 1️⃣ Clone Repository  

```bash
git clone https://github.com/yourusername/rag-ai-assistant.git

cd rag-ai-assistant
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv

```
Activate environment:
```
.venv\Scripts\activate
```

## 3️⃣ Install Dependencies

Using uv:
```
uv sync

pip install -r requirements.txt

```

## 4️⃣ Install Ollama

Download Ollama:

👉 https://ollama.com/download

Pull required models:

```

ollama pull llama3

ollama pull nomic-embed-text

```
## 5️⃣ Run Qdrant Vector Database

```
docker run -d --name qdrant -p 6333:6333 -v "${PWD}/qdrant_storage:/qdrant/storage" qdrant/qdrant
```

## 6️⃣ Start FastAPI Backend

```

python -m uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

## 7️⃣ Start Inngest Dev Server

``` 
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
```

## 8️⃣ Run Streamlit Frontend

```
streamlit run app.py
```

Frontend runs on:
```
http://localhost:8501
```

---

# Security & Best Practices

✔ Local AI execution (privacy focused)

✔ No cloud dependency required

✔ Modular backend architecture

✔ Environment variable configuration

✔ Async workflow orchestration

---

# 🚀 Future Enhancements

🤖 Multi-document conversational memory

📄 PDF highlighting for retrieved chunks

🧠 Hybrid search (BM25 + Vector Search)

🌍 Multi-language support

📱 Mobile-responsive UI

📊 Advanced retrieval analytics dashboard

🎤 Voice-based document questioning

---

# 📈 Use Cases

## This system can be used in:

📚 Research paper assistants

🏢 Enterprise internal knowledge bases

⚖️ Legal document search systems

🏥 Medical report analysis

🎓 AI learning assistants

📄 Resume & document intelligence platforms

---

# 🤝 Contributing

Contributions are welcome! 🚀

Fork the repository

Create a new branch

Commit your changes

Submit a Pull Request

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Harshita Surana

B.Tech AI-ML Student
