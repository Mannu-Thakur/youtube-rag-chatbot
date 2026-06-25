import streamlit as st

from src.chains import create_rag_chain
from src.embeddings import load_embeddings
from src.llm import load_llm
from src.loader import load_transcripts, extract_video_id
from src.memory import ConversationMemory, build_retrieval_query
from src.retriever import create_retriever
from src.splitter import split_text
from src.vector_store import (
    create_vectorstore,
    load_vectorstore,
    vectorstore_exists,
)

st.set_page_config(page_title="YouTube RAG Chat", page_icon="🎥", layout="wide")
st.title("🎥 YouTube RAG Chat")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

video_input_text = st.sidebar.text_area(
    "YouTube URLs / IDs (one per line)",
    value="rfscVS0vtbw",
    height=160,
)

video_inputs = [line.strip() for line in video_input_text.splitlines() if line.strip()]
video_ids = [extract_video_id(item) for item in video_inputs]

if st.sidebar.button("Build / Refresh Index"):
    with st.spinner("Building or loading the index..."):
        try:
            embeddings = load_embeddings()

            if vectorstore_exists(video_ids):
                vectorstore = load_vectorstore(embeddings)
            else:
                transcripts = load_transcripts(video_inputs)
                documents = split_text(transcripts)
                vectorstore = create_vectorstore(documents, embeddings, video_ids)

            llm = load_llm()
            retriever = create_retriever(
                vectorstore,
                llm,
                k=3,
                use_multi_query=True,
            )

            st.session_state.rag_chain = create_rag_chain(llm, retriever)

            st.sidebar.success("Ready")

        except Exception as exc:
            st.sidebar.error(str(exc))

if st.session_state.rag_chain is None:
    st.info("Build or load the index from the sidebar first.")
    st.stop()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_query = st.chat_input("Ask a question about the videos")

if user_query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query,
        }
    )

    with st.chat_message("user"):
        st.write(user_query)

    with st.spinner("Searching and answering..."):

        retrieval_query = build_retrieval_query(
            user_query,
            st.session_state.memory,
        )

        response = st.session_state.rag_chain.invoke(retrieval_query)

        answer = response["answer"]

        docs = response.get("context", [])

    st.session_state.memory.add_turn(user_query, answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.chat_message("assistant"):

        st.write(answer)

        if docs:
            with st.expander("Sources"):

                for i, doc in enumerate(docs, start=1):

                    meta = doc.metadata or {}

                    vid = meta.get("video_id", "")

                    start_sec = int(meta.get("start_seconds", 0))

                    time_range = meta.get("time_range", "")

                    youtube_link = (
                        f"https://www.youtube.com/watch?v={vid}&t={start_sec}s"
                    )

                    st.markdown(
                        f"**{i}.** [`{vid}`]({youtube_link}) — `{time_range}`"
                    )

                    st.write(doc.page_content[:300])