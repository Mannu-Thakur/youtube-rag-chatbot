from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


def create_rag_chain(llm, retriever):
    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful assistant answering questions about YouTube videos.

Use ONLY the supplied context.
If the context does not contain the answer, say you do not know.
When useful, mention the source video_id and timestamp range.

Context:
{context}

Question:
{question}
"""
    )

    def format_docs(docs):
        if not docs:
            return "No relevant context retrieved."

        return "\n\n".join(
            f"[video_id={doc.metadata.get('video_id', 'N/A')} | "
            f"{doc.metadata.get('time_range', 'N/A')}]\n"
            f"{doc.page_content}"
            for doc in docs
        )

    answer_chain = (
        RunnableLambda(
            lambda x: {
                "context": format_docs(x["context"]),
                "question": x["question"],
            }
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    chain = (
        RunnableParallel(
            context=retriever,
            question=RunnablePassthrough(),
        )
        | RunnablePassthrough.assign(answer=answer_chain)
    )

    return chain