import logging

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

logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

VIDEO_INPUTS = [
    "rfscVS0vtbw",
]


def main():
    video_ids = [extract_video_id(item) for item in VIDEO_INPUTS]

    try:
        embeddings = load_embeddings()

        if vectorstore_exists(video_ids):
            vectorstore = load_vectorstore(embeddings)
        else:
            transcripts = load_transcripts(VIDEO_INPUTS)
            documents = split_text(transcripts)
            vectorstore = create_vectorstore(documents, embeddings, video_ids)

        llm = load_llm()
        retriever = create_retriever(vectorstore, llm, k=3, use_multi_query=True)
        rag_chain = create_rag_chain(llm, retriever)

        memory = ConversationMemory()

        print("\nYouTube RAG Chat Ready!")
        print("Type 'exit' to quit.\n")

        while True:
            query = input("Ask a question: ").strip()

            if not query:
                continue

            if query.lower() == "exit":
                print("Goodbye!")
                break

            retrieval_query = build_retrieval_query(query, memory)
            response = rag_chain.invoke({"input": retrieval_query})
            answer = response["answer"]

            print("\nAnswer:\n")
            print(answer)

            docs = response.get("context", [])
            if docs:
                print("\nSources:\n")
                for i, doc in enumerate(docs, start=1):
                    meta = doc.metadata or {}
                    print(f"{i}. video_id={meta.get('video_id')} | {meta.get('time_range')}")
                    print(doc.page_content[:240])
                    print("-" * 80)

            memory.add_turn(query, answer)
            print("\n" + "=" * 100 + "\n")

    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye.")
    except Exception as exc:
        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()