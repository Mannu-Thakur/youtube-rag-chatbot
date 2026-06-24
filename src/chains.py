from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate


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
{input}
"""
    )

    document_prompt = PromptTemplate.from_template(
        "[video_id={video_id} | {time_range}]\n{page_content}"
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt,
        document_prompt=document_prompt,
    )

    return create_retrieval_chain(retriever, document_chain)