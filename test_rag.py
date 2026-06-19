from src.rag_pipeline import search_documents

query = "Why am I getting 401 Unauthorized?"

results = search_documents(query)

print(results)