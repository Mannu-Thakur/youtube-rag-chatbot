# 🎥 YouTube RAG Chatbot

<<<<<<< HEAD
A Retrieval-Augmented Generation (RAG) application that allows users to chat with YouTube videos using transcript-based semantic search and Groq LLMs.

## Features

* Extract transcripts from YouTube videos
* Recursive text chunking
* HuggingFace sentence-transformer embeddings
* FAISS vector database
* Groq LLM integration
* Conversation memory
* Multi-video support
* Source citations with timestamps
* Streamlit chat interface
* Persistent vector store caching

## Tech Stack

* Python
=======
A Retrieval-Augmented Generation (RAG) application that allows users to chat with YouTube videos using transcript-based semantic search, vector databases, and Large Language Models.

The system extracts transcripts from YouTube videos, converts them into embeddings, stores them in a FAISS vector database, retrieves relevant chunks for user queries, and generates grounded answers using Groq-powered LLMs.

---

# 🚀 Features

* YouTube Transcript Extraction
* Transcript Caching
* Recursive Text Chunking
* HuggingFace Embeddings
* FAISS Vector Database
* Semantic Search
* MultiQuery Retrieval
* Conversation Memory
* Multi-Video Support
* Source Citations
* Clickable Timestamp Links
* Persistent Vector Store
* Streamlit Chat Interface
* Error Handling & Retry Logic

---

# 🛠️ Tech Stack

## Backend

* Python 3.11
>>>>>>> 7d525a9 (Add project documentation)
* LangChain
* Groq (Llama 3.3 70B)
* FAISS
* HuggingFace Embeddings
<<<<<<< HEAD
* Streamlit
* YouTube Transcript API

## Architecture

```text
YouTube Video
      ↓
Transcript Extraction
      ↓
Text Chunking
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
Retriever
      ↓
Groq LLM
      ↓
Answer + Sources
```

## Installation

```bash
git clone https://github.com/Mannu-Thakur/youtube-rag-chatbot.git

cd youtube-rag-chatbot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

## Run

### Terminal Version

```bash
python app.py
```

### Streamlit Version

```bash
streamlit run streamlit_app.py
```

## Example Questions

* What is Python?
* Why is Python beginner friendly?
* Summarize the video.
* What modules are discussed?
* Compare what both videos say about Python.

## Project Structure
=======

## Frontend

* Streamlit

## APIs & Libraries

* youtube-transcript-api
* sentence-transformers
* langchain-community
* langchain-groq
* langchain-huggingface
* python-dotenv
* torch
* torchvision

---

# 🏗️ System Architecture

```text
YouTube Video(s)
        ↓
Transcript Extraction
        ↓
Transcript Caching
        ↓
Recursive Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Store
        ↓
Retriever / MultiQueryRetriever
        ↓
Relevant Chunks
        ↓
Conversation Memory
        ↓
Groq LLM
        ↓
Answer Generation
        ↓
Source Citations & Timestamps
```

---

# ⚙️ How It Works

## 1. Transcript Extraction

The application accepts either:

* YouTube Video URL
* YouTube Video ID

The transcript is fetched using the YouTube Transcript API.

Example:

```text
https://www.youtube.com/watch?v=rfscVS0vtbw
```

or

```text
rfscVS0vtbw
```

---

## 2. Transcript Caching

Fetched transcripts are stored locally.

Benefits:

* Faster startup
* Reduced API calls
* Offline reuse

---

## 3. Chunking

The transcript is split into smaller chunks using recursive text splitting.

Why?

* LLMs have context limits
* Smaller chunks improve retrieval quality
* Overlap preserves context

---

## 4. Embedding Generation

Each chunk is converted into a vector representation using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Embeddings capture semantic meaning rather than keyword matching.

---

## 5. FAISS Vector Store

Generated embeddings are stored inside a FAISS vector database.

Benefits:

* Fast similarity search
* Scalable retrieval
* Efficient storage

---

## 6. Retrieval

When the user asks a question:

```text
Why is Python beginner friendly?
```

the retriever finds the most semantically relevant transcript chunks.

---

## 7. MultiQuery Retrieval

Instead of searching using only one query, the system can generate multiple alternate search queries.

Example:

User Query:

```text
Why is Python beginner friendly?
```

Generated Queries:

```text
Why is Python easy to learn?

What makes Python beginner friendly?

Why do new programmers choose Python?

What are the advantages of learning Python?
```

This improves retrieval quality and recall.

---

## 8. Conversation Memory

The chatbot remembers previous interactions.

Example:

User:

```text
What is Python?
```

Follow-up:

```text
Why is it beginner friendly?
```

The chatbot understands that "it" refers to Python.

---

## 9. Answer Generation

Retrieved transcript chunks are passed to:

```text
Groq Llama 3.3 70B
```

The model generates an answer grounded in the retrieved context.

---

## 10. Source Citations

Every answer includes the source transcript chunk and timestamp.

Example:

```text
Video: rfscVS0vtbw
Timestamp: 00:00 - 00:49
```

Users can verify where the answer came from.

---

# 📁 Project Structure
>>>>>>> 7d525a9 (Add project documentation)

```text
youtube-rag-chatbot/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── chains.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── loader.py
│   ├── memory.py
│   ├── prompts.py
│   ├── retriever.py
│   ├── splitter.py
│   └── vector_store.py
│
<<<<<<< HEAD
└── utils/
    ├── helper.py
    └── video_utils.py
```

## Future Improvements

* Hybrid Search (BM25 + FAISS)
* Reranking
* PDF + YouTube RAG
* LangGraph Agents
* Streaming Responses

## Author
=======
├── utils/
│   ├── helper.py
│   └── video_utils.py
│
├── faiss_index/
│
└── data/
    └── cache/
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Mannu-Thakur/youtube-rag-chatbot.git
cd youtube-rag-chatbot
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Running the Project

## Terminal Version

```bash
python app.py
```

## Streamlit Version

```bash
streamlit run streamlit_app.py
```

---

# 💬 Example Questions

* What is Python?
* Why is Python beginner friendly?
* Summarize this video.
* What modules are discussed?
* What does the instructor recommend?
* Compare what both videos say about Python.

---

# 🎯 Key Concepts Demonstrated

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embeddings
* FAISS
* Prompt Engineering
* LLM Integration
* MultiQuery Retrieval
* Conversation Memory
* Source Grounding

---

# 🚧 Future Improvements

* Hybrid Search (BM25 + FAISS)
* Cross-Encoder Reranking
* PDF + YouTube Combined RAG
* LangGraph Integration
* Streaming Responses
* Cloud Deployment
* User Authentication
* Persistent Chat History

---

# ⚠️ Limitations

* Requires transcript availability
* Accuracy depends on transcript quality
* Very large video collections may require optimized indexing
* Generated answers are limited by retrieved context

---

# 📄 Resume Summary

Built a Retrieval-Augmented Generation (RAG) chatbot that enables users to query YouTube video transcripts using semantic search and Large Language Models. Implemented transcript extraction, recursive chunking, HuggingFace embeddings, FAISS vector storage, MultiQuery retrieval, conversation memory, source-linked citations, and a Streamlit-based chat interface using LangChain and Groq Llama 3.3.

---

# 👨‍💻 Author
>>>>>>> 7d525a9 (Add project documentation)

**Mannu Kumar Thakur**

B.Tech Computer Engineering
<<<<<<< HEAD
 
=======
 
>>>>>>> 7d525a9 (Add project documentation)
