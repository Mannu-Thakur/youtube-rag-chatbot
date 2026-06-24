import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def load_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is missing. Put it in your .env file.")

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=api_key,
        temperature=0.2,
    )