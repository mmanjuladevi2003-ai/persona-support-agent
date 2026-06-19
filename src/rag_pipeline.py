import os
import chromadb
from google import genai
from src.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="support_kb"
)


def get_embedding(text):
    result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
    )   
    return result.embeddings[0].values


def add_document(doc_id, text):
    embedding = get_embedding(text)

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )


def search_documents(query):
    embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    return results["documents"][0]