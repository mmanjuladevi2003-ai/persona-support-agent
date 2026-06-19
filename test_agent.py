from src.classifier import classify_customer_persona
from src.rag_pipeline import search_documents
from src.generator import generate_response
from src.escalator import should_escalate

query = input("Enter your support query: ")

persona = classify_customer_persona(query)

print("\nPersona:", persona)

if should_escalate(query):
    print("\nEscalation Required!")
else:
    context = search_documents(query)

    response = generate_response(
        query,
        persona,
        context
    )

    print("\nResponse:")
    print(response)