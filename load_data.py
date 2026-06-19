from src.rag_pipeline import add_document

with open("data/api_troubleshooting.md", "r", encoding="utf-8") as f:
    add_document("api_doc", f.read())

with open("data/billing_policy.txt", "r", encoding="utf-8") as f:
    add_document("billing_doc", f.read())

print("Documents loaded successfully!")