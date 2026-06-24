try:
    from langchain.retrievers.multi_query import MultiQueryRetriever
except Exception:
    MultiQueryRetriever = None


def create_retriever(vectorstore, llm, k: int = 3, use_multi_query: bool = True):
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": k})

    if use_multi_query and MultiQueryRetriever is not None:
        try:
            return MultiQueryRetriever.from_llm(
                retriever=base_retriever,
                llm=llm,
            )
        except Exception:
            pass

    return base_retriever