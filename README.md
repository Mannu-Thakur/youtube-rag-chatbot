# 🎥 YouTube RAG Chatbot

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
* LangChain
* Groq (Llama 3.3 70B)
* FAISS
* HuggingFace Embeddings
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

```text
youtube-rag-chatbot/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
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

**Mannu Kumar Thakur**

B.Tech Computer Engineering
 
