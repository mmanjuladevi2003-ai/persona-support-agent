import streamlit as st

from src.classifier import classify_customer_persona
from src.rag_pipeline import search_documents
from src.generator import generate_response
from src.escalator import should_escalate

st.title("Persona Support Agent")

query = st.text_area("Enter Customer Query")

if st.button("Submit"):

    if query:

        persona = classify_customer_persona(query)

        st.write("### Persona")
        st.write(persona)

        if should_escalate(query):
            st.error("Escalation Required")

        else:
            context = search_documents(query)

            response = generate_response(
                query,
                persona,
                context
            )

            st.write("### Response")
            st.write(response)