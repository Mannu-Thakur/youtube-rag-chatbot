# 🎥 YouTube RAG Chatbot
 

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

 

# 👨‍💻 Author
 
**Mannu Kumar Thakur**

B.Tech Computer Engineering
 
